def main():
    initial = is_safe (customer, avail, allot)
    if initial:
        print('Initial state: ',initial)
        granted = can_granted(allot, avail)
        if granted:
            print('Request granted: ',granted)
        else:
            print('Request cannot be granted')
    else:
        print('Initial sequence is not in safe state')
        

def need_matrix():
    n_matrix = []
    for lst in range (len(allot)):
        c = [s - b for s, b in zip(maxm[lst], allot[lst])]
        n_matrix.append(c)

    return n_matrix

def safe_state(customer, avail, allot):
    n_matrix = need_matrix()
    seq = []
    for times in range (customer):
        for i in range (len(n_matrix)):
            if n_matrix[i] != 0:
                u = [n <= av for n, av in zip(n_matrix[i], avail)]
                if sum(u) == resources:
                    avail = [a + b for a, b in zip(avail, allot[i])]
                    n_matrix[i] = 0
                    seq.append(i)
                else:
                    pass
    return seq


def is_safe(customer, avail, allot):
    s = safe_state(customer, avail, allot)
    if len(s) == customer:
        return True, s
    else:
        return False
    

def can_granted (allot, avail):
    updated_allot = allot
    updated_avail = avail
    n = need_matrix()
    process = int(input('Enter the process requesting resources: '))
    request = list(map(int,input('Enter request: ').
                     strip().split()))[:resources]
    x = [r <= nn for r, nn in zip(request, n[process])]
    y = [r <= av for r, av in zip(request, updated_avail)]
    
    if sum(x)== resources:
        if sum(y)== resources:
            avail = [a - b for a, b in zip(updated_avail, request)]
            allot[process] = [c + d for c, d in zip(updated_allot[process], request)]
            n[process] = [e - f for e, f in zip(n[process], request)]
            return is_safe(customer, updated_avail, updated_allot)
        else:
            return False
            
    else:
            return False
            
                    


if __name__ =="__main__": 
      
    customer = 5
    resources = 3
  
    # Available instances of resources  
    avail = [3,3,2]  
  
    # Maximum R that can be allocated  
    # to processes  
    maxm = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
  
    # Resources allocated to processes  
    allot = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
    


main()
     
