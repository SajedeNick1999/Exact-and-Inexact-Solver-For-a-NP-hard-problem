import numpy as np
import random

number_of_try=1000
number_of_restart=10

# number_of_try=100
# number_of_restart=5


FileName="large"

with open(FileName+".txt") as f:
    file=f.readlines()
f.close()

minizinc=""

file = [x.strip() for x in file]
file = [x.split(" ") for x in file]
#file = [x.split("\t") for x in file]
print(file)

max=0;
for x in file:
    for y in x:
        if int(y)>max:
            max=int(y)


def fitness(array,file,max):
    unsatisfied=0
    sum=0
    number_of_ones=0
    for x in file:
        for y in x:
            sum+=array[int(y)-1]
            #print("sum ="+str(sum))
        if(sum%2!=0):
            unsatisfied+=1
            #print(unsatisfied)
        sum=0
    for i in array:
        if i==1:
            number_of_ones+=1
    if(number_of_ones==0):
        #print(len(file)*max*max)
        return len(file)*max*max
    return unsatisfied*max+number_of_ones


def getbetter(array,file,max):
    index=-1
    index_fitness=fitness(array,file,max)
    unsatisfied=index_fitness/max
    sum=0
    unsat=[]
    for i in range(0,len(file)):
        for y in file[i]:
            sum+=int(y)
        if(sum%2!=0):
            unsat.append(i)
        sum=0

    #constraint=random.randrange(len(unsat))
    for z in unsat:
        for m in file[z]:
            x=int(m)-1
            if array[x]==1:
                array[x]=0
            else :
                array[x]=1

            a=fitness(array,file,max)
            # print(array)
            # print("change index "+str(x)+"for fitness"+str(a))
            if a<index_fitness:
                index_fitness=a
                index=x

            if array[x]==1:
                array[x]=0
            else :
                array[x]=1
    return index


x=0
best=[];
best_fitness=max*max
while x<number_of_restart:
    x+=1
    first=np.random.choice([0,1], size=(max,))
    print(first)
    print(fitness(first,file,max))

    #print(fitness([1,1,0,1,1],file,max))

    a=max*max
    while a>=max:

        b=getbetter(first,file,max)
        print(b)
        # if b==-1:
        #     b=random.randrange(max)
        # first[b]^=1
        if b!=-1:
            first[b]^=1
        else:break
        print("----------------------------------------")
        print(first)
        a=fitness(first,file,max)
        print(a)
        if a<best_fitness:
            best_fitness=a
            # best.clear()
            best=first.copy()


print("***************************************************************")
print(best)
print(best_fitness)

f = open(FileName+"_inexact_solution.txt", "w")
for j in range(1,max):

    f.write("x"+str(j)+"=")
    f.write(str(best[j]))
    f.write("\n")
f.write("\nfitness="+str(best_fitness))
# unsatisfied=0
# sum=0
# for x in file:
#     for y in x:
#         sum+=best[int(y)-1]
#         #print("sum ="+str(sum))
#     if(sum%2!=0):
#         unsatisfied+=1
#         #print(unsatisfied)
#     sum=0
f.write("\nnumber of unsatisfied="+str(int(best_fitness/max)))
f.close()
