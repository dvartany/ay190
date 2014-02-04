import random

runs=10000 #repeat 1000 times
people=23

overlap=0
for j in range(runs):
    taken={} #create empty list
    for j in range(people):
        day=random.randint(0,365) #random integers corresponding to b-days
        if day in taken:
            overlap+=1
            break #cross reference list, end at exactly 2 matches
        taken[day]='overlap' #allocate definition

print float(overlap)/runs