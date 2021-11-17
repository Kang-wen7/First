#Generate a hailstone sequence
number_str = input("Enter a positive integer:")
number = int(number_str)
count = 0

print("Starting with number:", number)
print("Sequence is:", end = ' ')

while number > 1: #Stop when sequence reaches 1

	if number%2:	#Number is odd
		number = number*3 + 1
	else:	#Number is even
		number = number/2
	print(number, ",", end = ' ')	#Add number to sequence
	
	count += 1	#add count with 1
	
else:
	print()
	print("Sequence is ", count, "numbers long")
