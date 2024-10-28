class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    
        # selection sort
        for i in range(len(names)):
            ind=i
            for j in range(i+1,len(names)):
                if heights[ind]< heights[j]:
                    ind=j
            heights[i], heights[ind] = heights[ind], heights[i]
            names[i], names[ind] = names[ind], names[i]
        return names

        # bubble sort
        # for i in range(len(names)):
        #     for j in range(1,len(names)):
        #         if heights[j]> heights[j-1]:
        #             heights[j], heights[j-1] = heights[j-1], heights[j]
        #             names[j], names[j-1] = names[j-1], names[j]
        # return names



        # insertion sort
        # for i in range(1,len(names)):
        #     ind=names[i]
        #     key=heights[i]
        #     j= i-1
        #     while j>=0 and key > heights[j]:
        #         names[j + 1] = names[j]
        #         heights[j+1]= heights[j]
        #         j -= 1
        #     heights[j + 1] = key
        #     names[j+1] = ind
        