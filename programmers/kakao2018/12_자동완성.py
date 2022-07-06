"""
1. Trie
2. BFS
"""

from collections import deque

class Node:
    def __init__(self):
        self.children = dict()
        self.count = 0


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        cur = self.head

        for w in word:
            if cur.children.get(w) == None:
                cur.children[w] = Node()

            cur = cur.children[w]
            cur.count += 1


def solution(words):
    answer = 0
    trie = Trie()

    for word in words:
        trie.insert(word)
    
    Q = deque([trie.head])

    while Q:
        cur = Q.popleft()

        for char, next_node in cur.children.items():
            if next_node.count > 1:
                Q.append(next_node)
            answer += next_node.count
    
    return answer
