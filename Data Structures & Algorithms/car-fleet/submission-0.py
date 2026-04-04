class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, key =lambda x: x[0], reverse = True)

        for pair in pairs:
            time = (target-pair[0])/pair[1] 
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        
        return len(stack)