def check_pattern(sentence , pattern , dict_pattern_letters):
	start_sentence = 0
	end_sentence = 0

	if(len(pattern) == 1):
		if(pattern[0] in dict_pattern_letters and dict_pattern_letters[pattern[0]] != sentence[start_sentence : ]):
			return False
		return True

	if(pattern[0] in dict_pattern_letters.keys()):
		if(dict_pattern_letters[pattern[0]] != sentence[start_sentence : len(dict_pattern_letters[pattern[0]])]):
			return False
		elif(dict_pattern_letters[pattern[0]] == sentence[start_sentence : len(dict_pattern_letters[pattern[0]])]):
			a = check_pattern(sentence[len(dict_pattern_letters[pattern[0]]) : ] , pattern[1:] , dict_pattern_letters)
			return a

	while(end_sentence < len(sentence)):	
		dict_pattern_letters[pattern[0]] = sentence[start_sentence : end_sentence + 1]
		if(check_pattern(sentence[end_sentence + 1 :] , pattern[1:] , dict_pattern_letters)):
			return True
		end_sentence += 1

	if(pattern[0] in dict_pattern_letters.keys()):
		del dict_pattern_letters[pattern[0]]

	return False


def print_answer(check_status):
	for status in check_status:
		if(status):
			print("Yes")
		else:
			print("No")


sentence = ""
pattern = ""
dict_pattern_letters = {}
check_status = []

num_sentences = int(input())

for _ in range(num_sentences):
	sentence = input()
	pattern = input()
	check_status.append(check_pattern(sentence , pattern , dict_pattern_letters))

print_answer(check_status)