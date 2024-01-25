alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in = input("Enter message , like hello:")


n=len(str_in)
str_out =""


for i in range(n):
    c= str_in[i]
    loc= alpha.find(c)
    print (i,c,loc)
    newloc=loc+3
    str_out += alpha[newloc]
    print (newloc ,str_out)
print ("abfuscated version", str_out  )  