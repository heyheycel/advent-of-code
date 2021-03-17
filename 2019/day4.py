"""
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:
111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
"""

#input 134564-585159

FROM=134566
TO=579999
count=0
for num in range(FROM, TO+1):
	digits=str(num)
	adjacent=any(digits[i]== digits[i+1] for i in range(5))
	increase=all(digits[i]<=digits[i+1] for i in range(5))
	count += int(adjacent and increase)


print("Solution day 4 part 1: "+str(count))




FROM=134566
TO=579988
pass1=[]
for num in range(FROM, TO+1):
	digits=str(num)
	if all(digits[i]<=digits[i+1] for i in range(5)):
		pass1.append(digits)


pass2=[]
for num in pass1:
	digits=str(num)
	for digit in digits:
		count=digits.count(digit)
		if count==2:
			pass2.append(digits)
			break






print("Solution day 4 part 2: "+str(len(pass2)))

