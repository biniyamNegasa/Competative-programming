class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={s:i for i,s in enumerate(order)}
        for i in range(1,len(words)):
            prev=words[i-1]
            now=words[i]

            a=0
            b=0
            while a<len(prev) and b<len(now):
                if dic[prev[a]]<dic[now[b]]:
                    break
                elif dic[prev[a]]>dic[now[b]]:
                    return False
                a+=1
                b+=1
            if b==len(now) and a<len(prev):
                return False

        return True
