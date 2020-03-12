
def swap(p):
    a = p[0]
    b = p[-1]
    p[0] = b
    p[-1] = a
    
def funA(x):
    a = 3
    b = 5
    c = [1,2,a,b]
    a = 100
    print(c)
    swap(c)
    print(c)
    x = 200

def startHere():
    x = 5
    funA(x)
    print(x)
    
startHere()
print('Done')

a = [1,2,3]
a.append(a)

print(a[0])
print(a[3])
print(a[3][3][3][3][3][3][3][3][3][3][3][3][0])
