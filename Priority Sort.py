
## list of all data 
l =[]

## User inputs number of processes
p = int(input("Enter total number of processes: "))
for process in range (1,p+1):
    arrival_time = int(input("Enter process arrival time for %d: " %process))
    burst_time = int(input("Enter process burst time for %d: " %process))
    priority = int(input("Enter process priority for %d: " %process))
    t = [process, arrival_time, burst_time, priority]
    l.append(t)


## calculating completion time
cat = l[0][1] + l[0][2]

for i in range (len(l)):
    if i == 0:
        cat = l[0][1] + l[0][2]
        l[i].insert(4,cat)
    else:
        cat = cat + l[i][2]
        l[i].insert(4,cat)


## calculating Total turn out time
for k in range (len(l)):
    l[k].insert(5,(l[k][4] - l[k][1]))


## calculating Total wait time
for w in range (len(l)):
    l[w].insert(6,(l[w][5] - l[w][2]))

print()

## printing the table in original form
dash = '-' * 75
print(dash)
print('{:<10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}'.format
            ('Process','AT','BT','priority','CT','TAT','WT'))
print(dash)

for ss in range(len(l)):
      print('{:<10d}{:>10d}{:>10d}{:>10d}{:>10d}{:>10d}{:>10d}'.format
            (l[ss][0], l[ss][1],l[ss][2],l[ss][3],l[ss][4],l[ss][5],l[ss][6]))



## prints average wait time and avg turn out time
avg_wt = 0
avg_tat = 0
for kk in range (len(l)):
    avg_wt = avg_wt+l[kk][6]
    avg_tat = avg_tat + l[kk][5]

print()
print("Average wait time: ", avg_wt/p)
print("Average turn out time: ", avg_tat/p)




## Sorting based on priority
      
l.sort(key=lambda sublist: sublist[1]) #1: arrival time
l.sort(key=lambda sublist: sublist[3]) #3: Priority 

print()


#calculating completion time
scat = l[0][1] + l[0][2]

for si in range (len(l)):
    if si == 0:
        scat = l[0][1] + l[0][2]
        l[si].insert(4,scat)
    else:
        scat = scat + l[si][2]
        l[si].insert(4,scat)


#calculating Total turn out time
for sk in range (len(l)):
    l[sk].insert(5,(l[sk][4] - l[sk][1]))


#calculating Total wait time
for sw in range (len(l)):
    l[sw].insert(6,(l[sw][5] - l[sw][2]))

print()

## print sorted table 
dash = '-' * 75
print(dash)
print('{:<10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}'.format
            ('Process','AT','BT','priority','CT','TAT','WT'))
print(dash)

for r_s in range(len(l)):
      print('{:<10d}{:>10d}{:>10d}{:>10d}{:>10d}{:>10d}{:>10d}'.format
            (l[r_s][0], l[r_s][1],l[r_s][2],l[r_s][3],l[r_s][4],l[r_s][5],l[r_s][6]))

savg_wt = 0
savg_tat = 0
for skk in range (len(l)):
    savg_wt = savg_wt+l[skk][6]
    savg_tat = savg_tat + l[skk][5]

print("Average wait time: ", savg_wt/p)
print("Average turn out time: ", savg_tat/p)


