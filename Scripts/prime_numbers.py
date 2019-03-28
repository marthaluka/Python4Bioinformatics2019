#! /home/user/anaconda2/envs/bioinf/bin/python
	
	print("square of all numbers divisible by 3 between 1 and 100")
	
	mult3 = [i**2 for i in range (100) if i%3==0]
	print(mult3)
	
	
	print ("square of prime numbers between 1 and 100")
	
	divisor = [2, 3, 5, 7]
	prime = [i for i in range (1,100) if (i in divisor)\
	 or i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0]
	prime2 = [i**2 for i in prime]
	print(prime2)