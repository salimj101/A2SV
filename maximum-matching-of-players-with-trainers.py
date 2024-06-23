class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players=sorted(players,reverse=True)
        trainers=sorted(trainers,reverse=True)
        
        p = 0
        t = 0
        m_n =0

        while p < len(players) and t < len(trainers):

            if players[p] <= trainers[t]:
                p+=1
                t+=1
                m_n+=1
            else :
                p+=1
        return m_n