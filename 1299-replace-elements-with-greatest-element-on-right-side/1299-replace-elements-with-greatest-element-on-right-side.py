class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        larg = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            tmp = larg
            if arr[i] > larg: larg = arr[i]
            arr[i] = tmp
        arr[-1] = -1
        return arr
        