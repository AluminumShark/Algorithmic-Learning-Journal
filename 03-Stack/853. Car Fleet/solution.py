from typing import List

class Solution:
    """
    Car Fleet
    Determine how many car fleets will arrive at the destination.
    """
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars by position (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []  # Stack to track fleet arrival times
        
        for p, s in cars:
            # Calculate time to reach target
            t = (target - p) / s
            
            # If this car would arrive after or at the same time as the car in front,
            # they form a fleet (skip adding this car)
            if stack and t <= stack[-1]:
                continue
            
            # This car forms a new fleet
            stack.append(t)
        
        return len(stack)

