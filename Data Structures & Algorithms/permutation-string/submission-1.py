class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_len = len(s1)
        sorted_s1 = "".join(sorted(s1))
        for i in range(len(s2)):
            sub_s = s2[i:i+s1_len]
            if ("".join(sorted(sub_s))) == sorted_s1:
                return True
        return False
