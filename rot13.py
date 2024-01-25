import base64
alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in = input("Enter message , like hello:")
shft= 13

n=len(str_in)
str_out =""


for i in range(n):
    c= str_in[i]
    loc= alpha.find(c)
    print (i,c,loc)
    newloc=(loc+shft)%26
   
    str_out += alpha[newloc]
a= str_out
z= a.encode("UTF-8")  
c= base64.b64encode(z)
k= c.decode("UTF-8")  
print ("abfuscated version", k)  