def day9(n_players, highest_marble):
	scores = {n : 0 for n in range(n_players)}
	player = 0
	index = -1
	marble = 1
	marbles = [0]
	
	while marble <= highest_marble:
		if marble % 23 == 0:
			scores[player] += marble
			index -= 7
			scores[player] += marbles.pop(index)
		else:
			if index + 2 == len(marbles):
				marbles.append(marble)
				index = marbles[-1]
			else:
				index = (index + 2) % len(marbles)
				marbles.insert(index, marble)
		
		marble += 1	
		player = (player + 1) % n_players
		print(index)
	
	return max(scores.values())
		
print('Expecting 32: {}'.format(day9(9, 25)))
#print('Expecting 8317: {}'.format(day9(10, 1618)))
#print('Expecting 146373: {}'.format(day9(13, 7999)))
#print('Expecting 2764: {}'.format(day9(17, 1104)))
#print('Expecting 54718: {}'.format(day9(21, 6111)))
#print('Expecting 37305: {}'.format(day9(30, 5807)))
