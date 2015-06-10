"""EX 12 - Prompting People. 
Same as previous exercise but much DRYer"""

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("how much do you weigh? ")

print("so, you're %r years old, %r tall, and weigh %r lbs.") % (
	age, height, weight)
	