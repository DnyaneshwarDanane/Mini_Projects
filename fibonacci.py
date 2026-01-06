nterm = int(input("How many terms: "))

n1 = 1
n2 = 1
count = 2

if nterm <= 0:
    print("print positive number")

elif nterm == 1:
    print("fibonacci series upto", nterm,":")
    print(n1)

else:
    print("fibonacci series upto",nterm,":")
    print(n1,", ",n2,end=" ,")

    while count<nterm:
        nth = n1 + n2
        print(nth,end=" ,")
        n1=n2
        n2=nth
        count+=1

        
