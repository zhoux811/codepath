

def degreeOfArray(arr):
    # Write your code here
    L = len(arr)
    d = dict()

    for n in arr:
        if n not in d:
            d[n] = 0
        else:
            d[n] += 1

    degree = (max(d.values()))


    l =[]
    for e in d:
        if d[e]==degree:
            l.append(e)


    dd = dict()
    for ee in l:
        #print(arr[::-1])
        left = arr.index(ee)
        right = L -1-arr[::-1].index(ee)
        print(ee, left,right)
        dd[ee] = right - left +1
    return min(dd.values())



print(degreeOfArray([0,1,2,1,3,2]))
print(degreeOfArray([5,1,2,2,3,1]))