"""
1. Regex
"""
import re

def solution(files):
    return sorted(files, key=lambda x : (re.search(r'[^\d]+', x.lower()).group(), int(re.search(r'\d+', x).group())))
