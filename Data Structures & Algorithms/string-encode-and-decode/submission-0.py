class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        return "".join(result)



    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            delimiter = s.find("#", i)

            if delimiter == -1:
                raise ValueError("Invalid encoded string")

            length = int(s[i:delimiter])
            start = delimiter + 1
            end = start + length

            if end > len(s):
                raise ValueError("Invalid encoded string")

            result.append(s[start:end])
            i = end
        return result

            