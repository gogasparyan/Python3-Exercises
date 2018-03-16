###################################################################################
###		Required: write a Python program to display the current date and time   ###
###################################################################################
###																			 	###
###          Sample Output:     1. 25-11-2018 14:34:46						 	###
###                             2. 25-Nov-18 12:34:46	  				 	 	###
###                             3. 25.Nov.2018 Sunday 02:34:46 PM 			 	###
###																			 	###
###################################################################################

import datetime

now = datetime.datetime.now()

print ("Current date and time:")
print ("1. " + str(now.strftime("%d-%m-%Y %H:%M:%S")))
print ("2. " + str(now.strftime("%d-%b-%y %H:%M:%S")))
print ("3. " + str(now.strftime("%d.%b.%Y %A %I:%M:%S %p"))+"\n\n")
