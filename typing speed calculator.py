from time import *
import random as r

#print(time())
#the above print statement prints the seconds in time that occured from 1972 to till the second went noow


def mistake(par, user):
    error=0
    for i in range(len(par)):
        try:
            if par[i]!=user[i]:
                error+=1
        except:
            error+=1
    return error


def speed_time(t1,t2,user):

    time_difference=t2-t1
    time_roundof=round(time_difference,2)
    print(len(user))
    speed=len(user)/time_roundof
    return round(speed)


test=["A paragraph is a self-contianed unit of discourse in writing as blas las blah ddsdk","It is fukl","ghj bhjn jkhhjhhjhkj"]
test1=r.choice(test)
print("***************Typing speed calculator***********")
print(test1)
print()
print()
time1=time()
testInput=input("Enter the input : ")
time2=time()

print('typing SpeeD (in word per sec) :',speed_time(time1,time2,testInput))
print("Error : ",mistake(test1,testInput))

#test second commit