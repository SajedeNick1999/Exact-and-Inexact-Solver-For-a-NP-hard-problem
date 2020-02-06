from minizinc import Instance, Model, Solver

gecode = Solver.lookup("gecode")
max=0

trivial = Model()

FileName="small"

with open(FileName+".txt") as f:
    file=f.readlines()
f.close()

minizinc=""

file = [x.strip() for x in file]
file = [x.split(" ") for x in file]
#file = [x.split("\t") for x in file]
print(file)

for x in file:
    for y in x:
        if int(y)>max:
            max=int(y)

for y in range(0,max+1):
    minizinc=minizinc+"var 0..1:x"+str(y)+";\n"

minizinc=minizinc+"\n"
minizinc=minizinc+"var int: a;\n\n"
minizinc=minizinc+"\n constraint x0=0;\n"
for x in file:
    minizinc=minizinc+"constraint ("
    for y in x:
        minizinc=minizinc+"x"+y+"+"
    minizinc=minizinc[:-1]
    minizinc=minizinc+") mod 2=0 ;\n"

minizinc2="a = "
for i in range(1,max+1):
    minizinc2=minizinc2+"x"+str(i)+"+"
minizinc2=minizinc2[:-1]

minizinc+="\n"+minizinc2+";\n\n"

minizinc+="\nconstraint a!=0 ;\n"

minizinc+="\nsolve minimize a;\n"

print(max)
print(minizinc)

sum=0;

trivial.add_string(minizinc)
instance = Instance(gecode, trivial)

# Find and print all intermediate solutions
result = instance.solve(intermediate_solutions=True)

f = open(FileName+"_solution.txt", "w")


for j in range(1,max+1):
    #print("x"+str(j)+" = ")
    print(result[len(result)-1, "x"+str(j)])
    f.write("x"+str(j)+"=")
    f.write(str(result[len(result)-1, "x"+str(j)] )+"\n")
    sum+=result[len(result)-1, "x"+str(j)]

f.write("\nnumber = "+str(sum))
print(sum)
f.close()
