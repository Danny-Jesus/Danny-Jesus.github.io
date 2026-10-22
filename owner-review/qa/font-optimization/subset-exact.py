exec(open('/workspace/v73-premium-review/font-optimization/optimize.py').read().split('for opt in [True,False]:')[0])
import uharfbuzz as hb
from io import BytesIO
def hbfont(tt):
 tt=TTFont(tt);tt.flavor=None;buf=BytesIO();tt.save(buf);return hb.Font(hb.Face(buf.getvalue()))
for label,char_set in [('latin1',keep),('english',actual|set(range(0x20,0x7F))|set(map(ord,'–—‘’“”•·…©®™−')))]:
 font=TTFont(source)
 options=subset.Options();options.flavor='woff2';options.layout_features=['*'];options.name_IDs=['*'];options.name_legacy=True;options.name_languages=['*'];options.recalc_bounds=True
 sub=subset.Subsetter(options=options);sub.populate(unicodes=char_set);sub.subset(font);font.flavor='woff2'
 out=root/f'newsreader-exact-fullaxes-{label}.woff2';original_names=font.getGlyphOrder();font.save(out)
 check=TTFont(out);assert actual_supported <= set(check.getBestCmap())
 report={'file':out.name,'size':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'axes':[(a.axisTag,a.minValue,a.defaultValue,a.maxValue) for a in check['fvar'].axes],'glyphs':len(check.getGlyphOrder()),'characters':len(check.getBestCmap()),'actual_cmap_coverage':True,'original_supported_actual_characters':sorted(actual_supported),'comparison':[]}
 for w in [400,420]:
  for opsz in [24,48,72]:
   loc={'wght':w,'opsz':opsz};a=original.getGlyphSet(location=loc);b=check.getGlyphSet(location=loc)
   max_diff=0.;max_width_diff=0.;mismatches=[];coords=0;badstruct=[]
   cmap=check.getBestCmap(); compare=list(zip(original_names,check.getGlyphOrder()))
   def flatten(v):
    if isinstance(v,(tuple,list)):
     out=[]
     for x in v:out.extend(flatten(x))
     return out
    return [v]
   for original_gn,gn in compare:
    pa=DecomposingRecordingPen(a);pb=DecomposingRecordingPen(b);a[original_gn].draw(pa);b[gn].draw(pb)
    fa=flatten(pa.value);fb=flatten(pb.value)
    if len(fa)!=len(fb):badstruct.append(gn);continue
    local=0
    for ca,cb in zip(fa,fb):
     if isinstance(ca,(int,float)) and isinstance(cb,(int,float)):local=max(local,abs(ca-cb));coords+=1
     elif ca!=cb:badstruct.append(gn)
    max_diff=max(max_diff,local);wd=abs(a[original_gn].width-b[gn].width);max_width_diff=max(max_width_diff,wd)
    if local>1e-9 or wd>1e-9:mismatches.append({'glyph':gn,'outline_delta':local,'advance_delta':wd})
   r={'location':loc,'compared_glyphs':len(compare),'coordinate_values':coords,'max_outline_difference_font_units':max_diff,'max_advance_difference_font_units':max_width_diff,'outline_structure_mismatch':sorted(set(badstruct)),'mismatches_over_1e_9':mismatches}
   print(out.name,loc,max_diff,max_width_diff,len(badstruct),flush=True);report['comparison'].append(r)
 # Shape complete extracted route text, comparing glyph identity and positioning.
 of=hbfont(source);nf=hbfont(out);shaping=[]
 for w in [400,420]:
  for opsz in [24,48,72]:
   var={'wght':w,'opsz':opsz};of.set_variations(var);nf.set_variations(var)
   shaped=[]
   for f,is_new in [(of,False),(nf,True)]:
    b=hb.Buffer();b.add_str(text);b.guess_segment_properties();hb.shape(f,b)
    names=original_names if is_new else original.getGlyphOrder()
    shaped.append([(names[i.codepoint],i.cluster,p.x_advance,p.y_advance,p.x_offset,p.y_offset) for i,p in zip(b.glyph_infos,b.glyph_positions)])
   assert shaped[0]==shaped[1], 'SHAPING MISMATCH'
   shaping.append({'location':var,'glyphs':len(shaped[0]),'exact_glyph_sequence_and_positions':True})
 report['shaping']=shaping;report['extracted_route_text_characters']=len(text)
 (root/f'report-exact-{label}.json').write_text(json.dumps(report,indent=2))
 print('SIZE',out.stat().st_size,'AXES',report['axes'],flush=True)
