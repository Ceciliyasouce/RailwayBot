n=input()
a=[0 for x in range(50)]
a=input().split()
c=0
for i in range(int(n)):
    if int(a[i])>0:
        c+=1
f=0
for i in range(int(n)):
    if a[i]==n:
        f=1
        break
if f==1 and int(c)==int(n):
    print("True")
else:
    print("False")
