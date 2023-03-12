class Solution:
    def simplifyPath(self, path: str) -> str:
        levels, stack = path.split('/'), []

        for level in levels:
            if(len(level) > 0 and level != '.'):
                if level == '..' and stack:
                    stack.pop()
                elif(level != '..'):
                    stack.append(level)

        return "/"+"/".join(stack)