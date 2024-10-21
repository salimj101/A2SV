class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        min_sum=float('inf')
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum = i + j
                    if index_sum < min_sum:
                        min_sum = index_sum 
                        ans = [list1[i]] 
                    elif index_sum == min_sum:
                        ans.append(list1[i]) 

        return ans