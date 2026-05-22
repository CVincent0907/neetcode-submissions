class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "\t"

        result = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                result += strs[i]
            else: 
                result += strs[i] + "\n"
        return result


    def decode(self, s: str) -> List[str]:
        if s == "\t":
            return []
        return s.split('\n')

