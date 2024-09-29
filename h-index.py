class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort(reverse=True)
        # res=0
        # for i in range(len(citations)):
        #     if i+1 <= citations[i]:
        #         res+=1
        # return res
        count_ = [0]* (len(citations)+1)
        for i in citations:
            count_[min(i,len(citations))]+=1
                   
        c_paper= 0
        for j in range(len(count_)-1,-1,-1):
            c_paper+= count_[j]
            if c_paper >= j:
                return j

        # print(count_)