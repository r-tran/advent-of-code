import sys
import string

text = open(sys.argv[1]).readline().strip()

def day5(text):
	stack = []
	for i in range(len(text)):
		if len(stack) > 0 and stack[-1].lower() == text[i].lower() and stack[-1] != text[i]:
			stack.pop()
		else:
			stack.append(text[i])
	return len(stack)

def part2(text):
	min_length = float('inf')
	chars = string.ascii_lowercase[:26]
	print(chars)
	for c in chars:
		text_string = text.replace(c, '').replace(c.upper(),'')
		res = day5(text_string)
		min_length = min(min_length, res)
	return min_length

print(part2(text))
