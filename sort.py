def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
 
def insertionSort(a): 
    for i in range(1, len(a)):
        holdIt=a[i]   
        j = i-1
        while j >=0 and holdIt < a[j] : 
                a[j+1] = a[j] 
                j -= 1
        a[j+1] = holdIt

def selectionSort(a):
    for i in range(len(a)):
        minA=i
        for j in range(i+1,len(a)):
            if a[minA]>a[j]:
                minA=j
        a[i], a[minA]=a[minA], a[i]


b = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(b)
c = [64, 34, 25, 12, 22, 11, 90]
insertionSort(c)
d = [64, 34, 25, 12, 22, 11, 90]
selectionSort(d)

print("Bubble Sort:    "),
for i in range(len(b)):
    print ("%d" %b[i]),
print("\nInsertion Sort: "),
for i in range(len(c)):
    print ("%d" %c[i]), 
print("\nSelection Sort: "),
for i in range(len(d)):
    print ("%d" %d[i]), 

def quickSort(a):

    less = []
    equal = []
    greater = []

    if len(a) > 1:
        pivot = a[0]
        for x in a:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)  
    else:  
        return a

e = [64, 34, 25, 12, 22, 11, 90]
e=quickSort(e)

print("\nQuick Sort:     "),
for i in range(len(e)):
    print ("%d" %e[i]),