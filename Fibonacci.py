nterms = 25
n1,n2 = 0, 1
count = 0

x=open('C:\Codestage\Python\Outputs\Fibonacci.txt','w')

while count < nterms:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    x.write(str(n1)+str(chr(13)))
    count +=1
    
x.close()

    