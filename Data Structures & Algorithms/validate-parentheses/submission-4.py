class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        mapping = dict()

        mapping['{'] = '}'
        mapping['('] = ')'
        mapping['['] = ']'

        for sym in s:

            if sym == '{' or sym == '(' or sym == '[':
                stack.append(sym)

            else:
                if len(stack) == 0:
                    return False

                popout = stack[-1]

                if sym != mapping[popout]:
                    return False

                stack.pop()

        return len(stack) == 0




