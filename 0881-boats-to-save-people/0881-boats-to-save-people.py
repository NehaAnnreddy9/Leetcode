class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l, r = 0, len(people) - 1
        while l <= r:
            val = people[l] + people[r]
            if val <= limit: l += 1
            r -= 1
            count += 1
        return count
        