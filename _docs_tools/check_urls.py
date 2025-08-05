#!/usr/bin/env python3
"""Check if all hyperlinks in all markdown documents are valid.

## Prerequisite:
npm install -g markdown-link-check
"""

import os

from md_utils import get_markdown_files, DOCS_DIR, MLC_CONF

for md_file in get_markdown_files():
    command = f"markdown-link-check -c {MLC_CONF} -q {md_file}"
    # print(command)
    os.system(command)
