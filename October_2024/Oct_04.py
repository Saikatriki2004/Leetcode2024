class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort the array to easily form pairs
        skill.sort()
        
        # Total sum of the skills
        total_skill = sum(skill)
        
        # Number of players
        n = len(skill)
        
        # Each team should have this sum of skills
        team_skill_sum = total_skill // (n // 2)
        
        # If the total skill isn't divisible by the number of teams, return -1
        if total_skill % (n // 2) != 0:
            return -1
        
        chemistry_sum = 0
        
        # Form teams by pairing smallest with largest
        i, j = 0, n - 1
        while i < j:
            # Calculate the sum of the current pair
            current_team_sum = skill[i] + skill[j]
            
            # If the sum of the current pair doesn't match the expected team sum, return -1
            if current_team_sum != team_skill_sum:
                return -1
            
            # Calculate the chemistry (product) of this pair and add to the total chemistry
            chemistry_sum += skill[i] * skill[j]
            
            # Move towards the next pair
            i += 1
            j -= 1
        
        # If all pairs are valid, return the total chemistry sum
        return chemistry_sum
