import os

def replace_all_mds():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".md")]
    for f in files:
        replace_formula(f)

import re

def replace_formula(file_name : str):
    with open(file_name, 'r', encoding='utf-8') as f:
        pattern = r'!\[\]\(https://cdn\.nlark\.com/yuque/__latex/[^&]*&code=([^&]*)&[^)]*\)'
        content = f.read()
        new = re.sub(pattern, replace, content)
        with open('replaced_' + file_name, 'w', encoding='utf-8') as fout:
            fout.write(new)

import urllib.parse

def replace(matched):
    formula = matched.group(1)
    formula = urllib.parse.unquote(formula)
    return '$' + formula + '$'
    
replace_all_mds()