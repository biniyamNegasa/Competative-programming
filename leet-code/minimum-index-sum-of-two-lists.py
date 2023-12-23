class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans={}
        for i,word in enumerate(list1):
            if word in list2:
                ans[word]=i+list2.index(word)
        mn=min([ans[x] for x in ans])
        real_ans=[]
        for w in ans:
            if ans[w]==mn:
                real_ans.append(w)
        return real_ans