class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined =[]
        for i in range(len(position)):
            combined.append([position[i], speed[i]])
        combined.sort(reverse=True)
        fleets =[]
        for pos,sp in combined:
            time = (target-pos)/sp
            fleets.append(time)
            if(len(fleets)>=2 and fleets[-2] >= fleets[-1]):
                fleets.pop()
        return len(fleets)