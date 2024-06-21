# trie
"""
n => number of queries => 7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch

1 insert
2 search
3 prefix search
4 find all words with given prefix
5 find prefix with largest string
"""

class node:
    def __init__(self):
        self.d = {}
        self.flag = 0

class tries:
    def __init__(self):
        self.root = node()
        
    def insert(self, s):
        t = self.root
        for i in s:
            if i not in t.d:
                t.d[i] = node()
            t = t.d[i]
        t.flag = 1

    def search(self, word):
        t = self.root
        for i in word:
            if i not in t.d:
                return False
            t = t.d[i]
        if t.flag == 1:
            return True
        return False

    def search_prefix(self, prefix):
        t = self.root
        for i in prefix:
            if i not in t.d:
                return False
            t = t.d[i]
        return True

    def all_words_with_prefix(self, prefix):
        t = self.root
        for i in prefix:
            if i not in t.d:
                return False
            t = t.d[i]
        def recur(a, prefix, t):
            if t.flag == 1:
                a.append(prefix)
            for i in t.d:
                recur(a, prefix+i, t.d[i])
        a = []
        recur(a, prefix, t)
        return a

    def prefix_with_longest_string(self, prefixes):
        dic = {}
        length = 0
        prefix = False
        for i in prefixes:
            dic[i] = self.all_words_with_prefix(i)
            dic[i].sort()
            if len(dic[i][-1]) > length:
                length = len(dic[i][-1])
                prefix = i
            elif len(dic[i][-1]) == length:
                prefix = min(prefix, i)
        return prefix


n = int(input())
queries = []
for i in range(n):
    queries.append(input().split())
    queries[i][0] = int(queries[i][0])

trie = tries()
for i in queries:
    if i[0] == 1:
        trie.insert(i[1])
    elif i[0] == 2:
        print(trie.search(i[1]))
    elif i[0] == 3:
        print(trie.search_prefix(i[1]))
    elif i[0] == 4:
        print(trie.all_words_with_prefix(i[1]))
    elif i[0] == 5:
        print(trie.prefix_with_longest_string(["n", "a"]))
