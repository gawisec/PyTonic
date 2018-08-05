import math
import numpy

modifiers = .09 #Percentage
gym_dots = 5.5
energy_per_train = 10
happy = 4750
stat_total = 16000000 

def ask_gym_input():

    user_option = raw_input("Enter your weight class here: ")
    print "1 - Lightweight"
    print "2 - Mediumweight"
    print "3 - Heavyweight"

    if user_option(1):
        print ""

#gym_gain = ((0.0000003480061091*numpy.log(happy+250)+0.000003091619094)*stat_total+0.0000682775184551527*(happy+250)-0.0301431777)*(modifiers+1)*gym_dots*energy_per_train
#total_gain = gym_gain * 15


#print ("Single Gains: {:,.2f}".format(gym_gain))
#print ("Total Gains:{:,.2f}".format(total_gain))
#test = (stat_total + total_gain)


gym_gain = ((0.0000003480061091*numpy.log(happy+250)+0.000003091619094)*stat_total+0.0000682775184551527*(happy+250)-0.0301431777)*(modifiers+1)*gym_dots*energy_per_train
total_gain = gym_gain * 15
print ("Single Gains: {:,.2f}".format(gym_gain))
print ("Total Gains:{:,.2f}".format(total_gain))

initial_gain = total_gain + stat_total
print ("Initial Gain:{:,.2f}".format(initial_gain))
for days in range(0, 30):
    print days

    initial_gain = total_gain + stat_total
    gg = initial_gain + total_gain
    print gg
    print initial_gain
