""" 
1. Regex
"""
import re
from collections import defaultdict

def solution(word, pages):
    url_regex = r'(?<=<meta property=\"og:url\" content=\"https://).*?(?=\")'
    link_regex = r'(?<=a href=\"https://).*?(?=\")'
    page_info = defaultdict(lambda : [None, 0]) # [page number, total score] 
        
    for i, page in enumerate(pages):
        url = re.findall(url_regex, page)[0]
        links = re.findall(link_regex, page)
        
        basic_score = re.split(r'[^a-z]', page.lower()).count(word.lower())
        page_info[url][0] = i
        page_info[url][1] += basic_score
        
        for linked_page in links:
            if len(links) != 0:
                page_info[linked_page][1] += basic_score / len(links)
    
    page_info = [page for page in page_info.values() if page[0] != None]
    
    return sorted(page_info, key=lambda x:(-x[1], x[0]))[0][0]
