class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openClose={']':'[','}':'{',')':'('}
        for i in s:
            if i in openClose:
                if stack and stack[-1]==openClose[i]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)
        return True if not stack else False