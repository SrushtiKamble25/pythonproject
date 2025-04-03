from bisect import bisect_left, bisect_right

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)  

    def add(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index  

    def get_prefix_sum(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index  
        return total

    def get_range_sum(self, left, right):
        return self.get_prefix_sum(right) - self.get_prefix_sum(left - 1)

def process_maintenance_queries(logs, queries):
    # Extract unique dates and map them to indices
    sorted_dates = sorted(set(date for _, date, _ in logs))
    date_index_map = {date: idx + 1 for idx, date in enumerate(sorted_dates)}

    # Initialize Fenwick Tree
    fenwick_tree = FenwickTree(len(sorted_dates))

    # Populate tree with maintenance costs
    for _, date, cost in logs:
        fenwick_tree.add(date_index_map[date], cost)

    # Process range sum queries
    results = []
    for start, end in queries:
        left_idx = bisect_left(sorted_dates, start) + 1
        right_idx = bisect_right(sorted_dates, end)

        # If no valid range found, return 0
        if left_idx > len(sorted_dates) or sorted_dates[left_idx - 1] > end:
            results.append(0)
        else:
            results.append(fenwick_tree.get_range_sum(left_idx, right_idx))

    return results


# Example usage
maintenance_logs = [
    (101, "2024-01-01", 500),
    (102, "2024-01-10", 300),
    (101, "2024-01-15", 700)
]
queries = [
    ("2024-01-01", "2024-01-10"),
    ("2024-01-01", "2024-01-15")
]

print(process_maintenance_queries(maintenance_logs, queries))
