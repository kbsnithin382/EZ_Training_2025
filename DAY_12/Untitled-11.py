
subseq = []
def recur(s, i, store):
    if i == len(s):
        return
    recur(s, i+1, store)
    store += s[i]
    subseq.append(store)
    recur(s, i+1, store)

recur("hello", 0, "")
print(subseq)
