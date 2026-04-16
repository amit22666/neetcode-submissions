class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for a in asteroids:

            while stack and stack[-1] > 0 and a < 0:
                if abs(a) > abs(stack[-1]): # size 
                    stack.pop()      # stack asteroid explodes
                    continue         # a may still collide
                elif abs(a) == abs(stack[-1]):
                    stack.pop()      # both explode
                    break
                else:
                    break            # a explodes

            else:
                stack.append(a)
        return stack

        