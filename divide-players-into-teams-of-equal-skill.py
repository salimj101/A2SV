class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_skill = sum(skill)
        left, right = 0, len(skill) - 1
        pair_sum = skill[left] + skill[right]
        s = 0

        while left < right:
            current_sum = skill[left] + skill[right]
            if current_sum != pair_sum:
                return -1
            s += skill[left] * skill[right]
            left += 1
            right -= 1

        return s
