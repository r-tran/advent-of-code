sequence = [int (x) for x in open('input/input.txt', 'r').readline()]
sum_of_all_digits = 0

n = len(sequence)
for i in range(n):
	jump_index = (i + (n // 2)) % n
	if sequence[i] == sequence[jump_index]:
		sum_of_all_digits += sequence[i]
print(sum_of_all_digits)
