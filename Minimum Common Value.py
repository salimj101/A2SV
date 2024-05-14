class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        ptr1 = 0
        ptr2 = 0
        common = []

        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                common.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        if common:
            return min(common)
        else:
            return -1
