class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict
        import bisect

        rows = defaultdict(list)  # Map to store all buildings row-wise
        cols = defaultdict(list)  # Map to store all buildings column-wise

        # Fill the rows and columns with buildings
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        # Sort all rows and columns for binary search
        for y_list in rows.values():
            y_list.sort()
        for x_list in cols.values():
            x_list.sort()

        count = 0  # Initialize covered buildings counter

        # Check each building one by one
        for x, y in buildings:
            row = rows[x]
            idx_row = bisect.bisect_left(row, y)  # Find building position in row
            left = idx_row > 0                    # Check if left building exists
            right = idx_row < len(row) - 1         # Check if right building exists

            col = cols[y]
            idx_col = bisect.bisect_left(col, x)   # Find building position in column
            above = idx_col > 0                   # Check if above building exists
            below = idx_col < len(col) - 1         # Check if below building exists

            # If there are buildings on all four sides, increment the counter
            if left and right and above and below:
                count += 1

        return count
