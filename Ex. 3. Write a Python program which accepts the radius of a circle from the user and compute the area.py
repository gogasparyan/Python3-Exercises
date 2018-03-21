####################################################################################################################
###   Required: Write a Python program which accepts the radius of a circle from the user and compute the area   ###
####################################################################################################################
###																								####################
###			Sample Output:																		####################
###							Input radius of a circle: r = 4										####################
###																								####################
###							Radius of a circle is: 	r = 4										####################
###							Area of a circle: 		S = 50.24									####################
###																								####################
####################################################################################################################
####################################################################################################################

from math import pi

r = ""

while r!=0:
	try:
		r = int(input("\nEnter radius of a cirlce:\t"))
		if r<=0:
			print("\nYou must enter positive integer")
			continue
		r = float(r)
		s = pi*(r**2)

		print("\nRadius of a circle is:\tr = " + str(r))
		print("Area of a circle:\tS = " + str(s))
		print("(Enter '0' for exit)")
		
	except (ValueError, TypeError):
		print("\n\t*** Error occurred ***\n\n You must enter positive integer")
		continue

print("\nAdios!")
