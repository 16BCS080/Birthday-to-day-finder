li=[int(i) for i in input("eneter date(dd-mm-yyyy):").split("-")]
date=str(li)
k=[5,3,1,0]
li[0]=li[0]
li[2]=(li[2]%400)
if li[2]%4==0 :
    i=1
else:
    i=0
m=[6-i,2-i,2,5,0,3,5,1,4,6,2,4]
r2=k[(li[2]//100)-1]
y=li[2]%100
r1=abs(((y//4)*2)+(y-(y//4)))
li[1]=m[li[1]-1]
li[2]=r1+r2
anse=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("date:{} is {}".format(date,anse[sum(li)%7-1]))
