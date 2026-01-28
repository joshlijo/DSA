class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []

        for op in operations:
            if op == '+':
                arr.append(arr[-1] + arr[-2])
            elif op == 'C':
                arr.pop()
            elif op == 'D':
                arr.append(2 * arr[-1])
            else:
                arr.append(int(op))
        
        return sum(arr)