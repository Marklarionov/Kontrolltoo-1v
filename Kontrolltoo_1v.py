from random import randint
#1

#tree = ['    /V\    ',
#       '   / V \   ',
#       '  / V V \  ',
#       ' /VV V VV\ ']
#n=int(input())
#for i in tree:
#    print(i * n)

#2  
#R=int(input())
#for i in range(0,R):
#    if i%2 != 0:
#        (i * i)
        
#3#b=1
p=0
while p!=10 :
    n=int(randint(-20,20))
    for i in range(1):
        print(n,end=" ")
    if n > 0:
        p += 1
print("num:", p)


#4
n=int(input())
even=0
odd=0
while n>0:
    if n%2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print("четных - %d, нечетных - %d" % (even, odd))
#5

a=int(input())
c=int(input())
b=0
while a!=c:
    b=c+a
    a=a+1
print(b)

