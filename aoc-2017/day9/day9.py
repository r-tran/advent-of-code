stream = open('input/input.txt').readline()

def total_group_score(stream):
	depth = 0 
	score = 0
	in_garbage = False
	garbage_count = 0

	i = 0
	while i < len(stream):	
		if stream[i] == '<' and not in_garbage:
			in_garbage = True
		elif stream[i] == '>':
			in_garbage = False
		elif stream[i] == '!':
			i += 1
		elif in_garbage:
			garbage_count += 1
		elif not in_garbage:	
			if stream[i] == '{':
				depth += 1
				score += depth
			if stream[i] == '}':
				depth -= 1
		i += 1

	return score, garbage_count

print(total_group_score(stream))