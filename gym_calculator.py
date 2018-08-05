import math
import numpy

modifiers = .09 #Percentage
gym_dots = 5.5
energy_per_train = 10
happy = 4750
stat_total = 15574504

def ask_gym_input():

    user_option = raw_input("Enter your weight class here: ")
    print "1 - Lightweight"
    print "2 - Mediumweight"
    print "3 - Heavyweight"

    if user_option(1):
        print ""

gym_gain = ((0.0000003480061091*numpy.log(happy+250)+0.000003091619094)*stat_total+0.0000682775184551527*(happy+250)-0.0301431777)*(modifiers+1)*gym_dots*energy_per_train
total_gain = gym_gain * 15
print"Single Gains: %f" % (gym_gain)
print"Total Gains: %f" % (total_gain)

