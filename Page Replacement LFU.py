from queue import Queue

def page_fault ():
    np = int(input('Number of pages: '))
    pages = list(map(int,input('Enter pages: ').strip().split()))[:np]
    frame = int(input('Size of Page Frame: '))
    q = Queue()
    memory = set()
    pagefault = 0
    d ={}
    
    for i in range (len(pages)):
        if len(memory) < frame:
            if pages[i] not in memory:
                memory.add(pages[i])
                q.put(pages[i])
                pagefault += 1
                if i not in d:
                    d[i] = pages[i]
                else:
                    d[i] = d[i] + 1
                print(d)
                
    
        else:
            if pages[i] not in memory:
                val = q.queue[0]  
                q.get()  
                memory.remove(val)  
                memory.add(pages[i])    
                q.put(pages[i])
                pagefault += 1

                
    print('Page Hit: ',np - pagefault)
    print('Page Faults: ',pagefault)
            


page_fault ()
