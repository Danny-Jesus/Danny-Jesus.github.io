#!/usr/bin/env bash
set -eu
cd /workspace/portfolio-v7-rebuilt
node -e "const n=Number(process.versions.node.split('.')[0]);if(n<24)throw new Error('Use the prepared Node 24 toolchain')"
npm ci --cache /workspace/rebuild-evidence/npm-cache --no-fund --no-audit
npm run build
