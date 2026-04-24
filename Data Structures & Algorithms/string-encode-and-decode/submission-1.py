class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                print('1.',j)
                j += 1
                print('2.',j)
            length = int(s[i:j])
            print(length,i,j)
            i = j + 1
            print('3.',i,j)
            j = i + length
            print('4.',i,j)
            res.append(s[i:j])
            i = j

        return res