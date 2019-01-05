phrases = open('input/input.txt', 'r').readlines()
valid_phrase = 0

for phrase in phrases:
    words = [''.join(sorted(word)) for word in phrase.split()]
    if len(set(words)) == len(words):
            valid_phrase += 1
print(valid_phrase)



