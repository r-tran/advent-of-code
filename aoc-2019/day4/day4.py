from collections import defaultdict

def check_rules(num):
	repeat_counts = defaultdict(int)
	decreases = False

	for i in range(len(num)):
		if i > 0 and num[i] == num[i - 1]:
			repeat_counts[num[i]] += 1
		if i > 0 and num[i] < num[i - 1]:
			decreases = True
	return repeat_counts, decreases 

nums = map(str, range(123257, 647016))

# part 1
num_pw_candidates_part1 = 0
for num in nums:
	repeat_counts, decreases = check_rules(num)
	if len(repeat_counts) > 0 and not decreases:
		num_pw_candidates_part1 += 1	
print(num_pw_candidates_part1)

# part 2
num_pw_candidates_part2 = 0
for num in nums:
	repeat_counts, decreases = check_rules(num)
	has_adjacent = 1 in repeat_counts.values()
	if has_adjacent and not decreases:
		num_pw_candidates_part2 += 1
print(num_pw_candidates_part2)
