w = int(raw_input())
n = map(int, raw_input().rstrip().split())
max_index = w - 1
min_index = 0

for i in range(1, w):
    if n[min_index] >= n[i]:
        min_index = i

for i in range(w - 1, -1, -1):
    if n[max_index] <= n[i]:
        max_index = i

max_i_gt_min_i = 1 if min_index < max_index else 0

print max_index + (w - 1 - min_index) - max_i_gt_min_i