class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
       # col_hm, subbox_hm = defaultdict(int), defaultdict(int)
        hash_map = defaultdict(list)
        c = 0
        for i in range(n):
            for j in range(n):
                if (value := board[i][j]) == ".": continue
                hash_map[f"row{i}"].append(value)
                curr_row = hash_map[f"row{i}"]
                if len(curr_row) != len(set(curr_row)): return False

                hash_map[f"col{j}"].append(value)
                curr_col = hash_map[f"col{j}"]
                if len(curr_col) != len(set(curr_col)): return False
               
                box_idx = (i // 3) * 3 + (j // 3)
                hash_map[f"subbox{box_idx}"].append(value)
                curr_subbox = hash_map[f"subbox{box_idx}"]
                if len(curr_subbox) != len(set(curr_subbox)): return False
        return True
