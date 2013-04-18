#! /usr/bin/env python
#
#	Seongjin Cho (Josh)
#	Student Number: 1130690
#	Math 480A
#
#	This is a program that determines wheter the given positive integer
#	is Prime or not. It has two usable method: isPrime(n) and test().
#

from __future__ import division
from math import sqrt, log, floor, ceil, pow
from fractions import gcd

def isPrime(n):
	"""This is an implementation of algorithm that determines whether
	an imput number is prime number of not. Manindra Angrawal, Neeraj
	Kayal, and Nitin Saxena first published the algorithm. The algorithm
	presents unconditional deterministic polynomial-time."""
	try:
		if not isinstance(n, (int, long, Integer)):
			raise TypeError("n must be an int")
		elif n <= 1:
			raise ValueError("n must be greater than 1")
		else:
			result1 = step1(n)
			if result1 == "Possibly Prime":
				r = step2(n)
				result2 = step3(n,r)
				if result2 == "Possibly Prime":
					return step4(n,r)
				else:
					return result2
			else:
				return result1
	except:
		raise
	
def step1(n):
	"""First Step: Check wheter given integer n is perfect power, i.e. 
	n = a^b. If it is not then n is possibly Prime."""
	if n == 2:
		return "Prime"
	elif n%2 == 0:
		return "Composite"
	else:
		# Now we only have odd integers
		b = range(2, int(round(log(n, 3))) + 1)
		# To Do: we can make this loop better because we know:
		# Suppose $a,b$ are in $\N$ and $\sqrt[b]{a} \ne integer$.
		# Then for all n in $\N$, $\sqrt[bn]{a} \ne integer$.
		# So we only need to check 2,3,5,7,11,... <= int(log(n,3))
		for i in b:
			if  int(round(n**(1/i)))**i == n:
				return "Composite"
		return "Possibly Prime"

def step2(n):
	"""Second Step: Find smallest r s.t. o_r(n) > log^2(n) where o_r(n) is
	defined by min{k: n^k = 1 (mod r)}"""
	for r in range(2, int(ceil(log(n, 2)**5)) + 1):
		if gcd(r,n) == 1:
			for k in range(1, int(log(n, 2)**2) + 1):
				if n**k % r == 1:
					break
			else:
				return r

def step3(n, r):
	"""Third Step: if 1 < (a,n) < n for some a <= r, then return Composite
	But if n <= r, return Prime. Otherwise, return Possibly Prime."""
	for a in range(2,r+1):
		if gcd(a,n) > 1 and gcd(a,n) < n:
			return "Composite"
	else:
		if n <= r:
			return "Prime"
		else:
			return "Possibly Prime"

def step4(n, r):
	"""Final Step: for 1 <= a <= floor(sqrt(euler_phi(r))*log(n)), check
	whether 'a' satisfies the Fermet's little Theorem. If it satisfies for
	all a, then it is definetely Prime!"""
	# To Do: requires euler_phi function implementation in python
	# this step is very heavy..... i need a method to optimize it
	for a in range(1, int(floor(sqrt(euler_phi(r))*log(n,2))) + 1):
		if a**n % n != a:
			return "Composite"
	else:
		return "Prime"

def test():
	"""Test whether my program works all right. Compares to the built in
	sage method Primes(). WARNING: It takes lots of time"""
	print "Checking whether it finds all the front few primes."
	count1 = 0
	badcount = 0
	for i in Primes():
		a = isPrime(i)
		if a != "Prime":
			badcount += 1
		if i > 10**4:
			break
		print i,
		count1 += 1
	print "result:", badcount, "Baddies"
	
	print "Checking whether there is any false positive"
	count2 = 0
	for i in range(2,10**4):
		if isPrime(i) == "Prime":
			count2 += 1
		print i,
	if count2 == count1:
		print "Seems like everything is good!"
