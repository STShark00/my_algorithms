'''Count number of subarray (continuous) that adds up to certain number'''
'''Two Pointer Algorithm'''
'''
    input:
    number of input = 5
    data = [1, 2, 3, 2, 5] (positive numbers)
    target_num = 5

    {[2, 3], [3, 2], [5]} satisfy
    --> output: 3
'''

num = 8
target = 6
data = [2, 4, 1, 3, 2, 4, 6, 9]

count = 0
interval_sum = 0
end = 0

for start in range(num):
    while interval_sum < target and end < num:
        interval_sum += data[end]
        end += 1
    if interval_sum == target:
        count += 1
    interval_sum -= data[start]

print(count)