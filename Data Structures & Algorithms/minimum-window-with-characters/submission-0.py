class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        cnt_t, window = {}, {}

        for c in t:
            cnt_t[c] = 1 +cnt_t.get(c,0)
        
        have, need  = 0, len(cnt_t)

        res, res_len = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if  c in cnt_t and window[c] == cnt_t[c]:
                have += 1

            while have == need:
                if(r -l +1 < res_len):
                    res = [l,r]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in cnt_t and window[s[l]] <  cnt_t[s[l]]:
                    have -= 1
                l += 1

        l, r =  res
        return s[l : r + 1] if res_len != float("infinity") else ""