import copy
from texttable import Texttable

data_list = []
gantt_list = {}
pro=[]
time =[]

## User inputs number of processes, burst time and quantum time
p = int(input("Enter total number of processes: "))

for process in range (1,p+1):
    burst_time = int(input("Enter process burst time for %d: " %process))
    t = [process, burst_time]
    data_list.append(t)

quantum_time = int(input("Enter qunatum time: "))

## contents of data_list is copied in data_list orginal for further calculations
data_list_o = copy.deepcopy(data_list)



##calculating turnaround time
## The process (i) and the runing time (s) is stored in lists pro and time 
s = 0
while any(j[1] != 0 for j in data_list):
        for i in range (len(data_list)):
            if data_list[i][1] > 0:
                if data_list[i][1] <= quantum_time:
                    v = data_list[i][1] - quantum_time
                    if v < 0:
                        s = s + data_list[i][1]
                        pro.append(i+1)
                        time.append(s)
                        gantt_list[i+1] = s
                        data_list[i][1] = 0
                        
                    else:
                        data_list[i][1] = data_list[i][1] - quantum_time
                        s = s + data_list[i][1]
                        pro.append(i+1)
                        time.append(s)
                        gantt_list[i+1] = s
                else:
                    data_list[i][1] = data_list[i][1] - quantum_time
                    s = s + quantum_time
                    pro.append(i+1)
                    time.append(s)
                    gantt_list[i+1] = s


## adding turnaround time to data_list_o
for value in range (len(data_list_o)):
    data_list_o[value].insert(2,gantt_list[value+1])

## calculating wait time
for k in range (len(data_list_o)):
    wt = data_list_o[k][2] - data_list_o[k][1]
    data_list_o[k].insert(3,wt)


## Printing gantt chart
    
table = Texttable()
table.add_rows([pro,time])
print(table.draw())


## print table 
dash = '-' * 50
print(dash)
print('{:<12}{:>12}{:>12}{:>12}'.format
            ('Process','Burst Time','TAT','WT'))
print(dash)

for r_s in range(len(data_list_o)):
      print('{:<12d}{:>12d}{:>12d}{:>12d}'.format
            (data_list_o[r_s][0], data_list_o[r_s][1],
             data_list_o[r_s][2],data_list_o[r_s][3]))



# Calculating average wait time
aw = 0

for w in range (len(data_list_o)):
    aw = aw+data_list_o[w][3]
    
print()
print("Average wait time: ", aw/p)


