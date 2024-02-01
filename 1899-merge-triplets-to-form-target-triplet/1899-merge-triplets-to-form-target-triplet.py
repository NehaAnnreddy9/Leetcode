class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i = 0
        tva = [False, False, False]
        
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]: 
                if triplets[i][0] == target[0]: tva[0] = True
                if triplets[i][1] == target[1]: tva[1] = True
                if triplets[i][2] == target[2]: tva[2] = True
        
        if False in tva: return False
        return True
        