#!/usr/bin/python3
""" Prime numer game"""


# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes


def SieveOfEratosthenes(n: int):
	'''
	list all prime number less than or equal to n
	Args:
	    n(int): maximum range for prime numbers
	'''

	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p*p, n+1, p):
				prime[i] = False
		p += 1
	for i in range(2, n+1):
		if prime[i]:
			print(i,',', end='')
				
# # Driver code
if __name__ == '__main__':
	n = 15
	print("Following are the prime numbers smaller"),
	print("than or equal to", n)
	SieveOfEratosthenes(n)
	print()
