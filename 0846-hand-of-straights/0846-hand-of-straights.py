class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand.sort()
    
        while len(hand):
            lis = []
            lis.append(hand.pop(0))
            i = 0
            while len(lis) < groupSize and i < len(hand):
                if lis[-1] == hand[i] - 1: lis.append(hand.pop(i))
                elif lis[-1] == hand[i]: i += 1
                else: return False
            if len(lis) != groupSize: return False
        
                
        return True
        