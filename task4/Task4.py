nums = []
with open("nums.txt") as file2:
    for line in file2:
        line = int(line.replace("\n", ""))
        nums.append(line)

minimum_number = min(nums)
moves = 0
for num in nums:
    if num > minimum_number:
        moves += num - minimum_number
    elif num < minimum_number:
        moves += minimum_number - num
print(moves)