from typing import List

class Solution:
    """
    Relative Ranks (Shell Sort version)
    Sort athletes by score (descending), then assign medals or numeric ranks.

    Approach:
    - Pair each score with its original index: (score, idx)
    - Sort by score descending using Shell Sort (a gapped insertion sort)
    - Reconstruct the result array assigning ranks by sorted order
    """

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Pair each score with its original index
        score_with_idx = [(s, i) for i, s in enumerate(score)]
        n = len(score)
        gap = n // 2  # initial gap for Shell Sort

        # Shell Sort: sort in descending order by score
        while gap > 0:
            for i in range(gap, n):
                temp = score_with_idx[i]  # tuple (score, idx)
                j = i
                # Shift elements that are smaller than current temp
                while j >= gap and score_with_idx[j - gap][0] < temp[0]:
                    score_with_idx[j] = score_with_idx[j - gap]
                    j -= gap
                score_with_idx[j] = temp
            gap //= 2  # reduce gap each round
        
        # Prepare the result array
        result = [""] * n
        for rank, (_, idx) in enumerate(score_with_idx):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        
        return result
