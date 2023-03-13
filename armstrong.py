## wap to print armstrong number
a =129
l=len(str(a))
temp=a
print(l)

sum=0
while(a!=0):
    b= a%10
    sum= sum + (b**l)
    a=a//10
print(sum)
if(sum ==temp):
    print("armstrong")
else:
    print("not")