def dec2k(number , k , num_digits):
	k_base = []
	while(number >= k):
		k_base.append(number % k)
		number = number // k
	k_base.append(number)
	if(len(k_base) < num_digits ):
		k_base.extend((num_digits - len(k_base)) * [0])
	return k_base[::-1]

k , n = list(map(int , input().split()))

n -= 1
i = 0
j = 1

while(True):
	if(n >= i and n <= (i + j * k ** j) - 1 ):
		n -= i
		print(chr((dec2k(n // j , k , j)[n % j]) + 97) )
		break
	i += j * k ** j
	j += 1