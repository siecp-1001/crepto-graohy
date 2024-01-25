alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in = input("Enter message , like hello:")
shft= int(input("shift value , like 3:"))

n=len(str_in)
str_out =""


for i in range(n):
    c= str_in[i]
    loc= alpha.find(c)
    print (i,c,loc)
    newloc=(loc+shft)%26
   
    str_out += alpha[newloc]
    
print ("abfuscated version", str_out  )  