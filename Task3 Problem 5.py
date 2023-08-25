def largest_prime_factor(n):
	largest_prime = -1
	i = 2
	while i * i <= n:
		while n % i == 0:
			largest_prime = i
			n = n // i
		i = i + 1
	if n > 1:
		largest_prime = n
	return largest_prime

n = 12
print("The largest prime factor is" ,largest_prime_factor(n))
