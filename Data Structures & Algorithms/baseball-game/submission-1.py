class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        for i in operations:
            if(i=="+"):
                stack.append(stack[-1]+stack[-2])
            elif(i=="C"):
                stack.pop()
            elif(i=="D"):
                stack.append(stack[-1]*2)
            else:
                stack.append (int(i))
        x=0
        for i in stack:
            x=x+i
        return x
