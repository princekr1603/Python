x=int(input("enter no."))
y=t=x
count=0
while(x!=0):
    x=x//10
    count=count+1
print(count)
ans=0
while(y!=0):
    r=y%10
    ans=ans+(r**count)
    y=y//10
if(ans==t):
    print("palindrome no.")
    


   
