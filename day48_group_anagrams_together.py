from collections import defaultdict


def anagrams(arr):
    ans=defaultdict(list)
    for s in arr:
        count=[0]*26
        for c in s:
            count[ord(c)-ord("a")]+=1
        ans[tuple(count)].append(s)
    return list(ans.values())
    

arr = ["act", "god", "cat", "dog", "tac"]
    
res = anagrams(arr)
for group in res:
    for word in group:
        print(word, end=" ")
    print()