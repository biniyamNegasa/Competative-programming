class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed)<len(name):
            return False
        i = 0
        j = 0
        while i<len(name) and j < len(typed):
            dicj = defaultdict(int)
            dici = defaultdict(int)
            if j<len(typed) and typed[j]==name[i]:
                while j<len(typed) and typed[j]==name[i]:
                    dicj[typed[j]]+=1
                    j+=1
            else:
                j+=1
            val = name[i]
            if i<len(name) and name[i]==val:
                while i<len(name) and name[i]==val:
                    dici[name[i]]+=1
                    i+=1
            else:
                i+=1
            if dicj[val]<dici[val]:
                return False
        if j<len(typed) or i<len(name):
            return False
        return True