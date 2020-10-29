
#list of all data 
l =[]

# Input from user
p = int(input("Enter total number of processes: "))
for process in range (1,p+1):
    arrival_time = int(input("Enter process arrival time for %d: " %process))
    burst_time = int(input("Enter process burst time for %d: " %process))
    t = [process, arrival_time, burst_time]
    l.append(t)


#calculating completion time (arrival time + burst time)
cat = l[0][1] + l[0][2]

for i in range (len(l)):
    if i == 0:
        cat = l[0][1] + l[0][2]
        l[i].insert(3,cat)
    else:
        cat = cat + l[i][2] #looping for next values 
        l[i].insert(3,cat)


#calculating Total turn out time
for k in range (len(l)):
    l[k].insert(4,(l[k][3] - l[k][1]))


#calculating Total wait time
for w in range (len(l)):
    l[w].insert(5,(l[k][4] - l[k][2]))
    print()
print(" The list is as following :")
print("[[process number, arrival time, burst time, compeltion time, TAT, wait time]]")
print(l)




