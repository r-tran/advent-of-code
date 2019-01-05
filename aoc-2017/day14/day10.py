#lengths = [ord(c) for c in open('input/input.txt','r').readline()]

def knot_hash_algorithm(rounds, line):
	lengths = [ord(c) for c in line]
	end = [17, 31, 73, 47, 23]
	lengths = lengths + end
	sparse_hash = list(range(256))
	n = len(sparse_hash)
	current_idx = 0
	skip_size = 0
	for k in range(rounds):
		for length in lengths:
				temp1 = current_idx
				sub_list = []
				for i in range(length):
					sub_list.append(sparse_hash[temp1])
					temp1 = (temp1 + 1) % n
				sub_list = sub_list[::-1]

				temp2 = current_idx
				for i in range(length):
					sparse_hash[temp2] = sub_list[i]
					temp2 = (temp2 + 1) % n

				current_idx = (current_idx + length + skip_size) % n
				skip_size += 1

	dense_hash = []
	for i in range(0, len(sparse_hash), 16):
		sub = sparse_hash[i + 1 : i + 16]
		hash_num = sparse_hash[i]
		for j in sub:
			hash_num ^= j 
		dense_hash.append(hash_num)

	hash_str = ''
	for num in dense_hash:
		hash_str += format(num, '02x')
	return hash_str

