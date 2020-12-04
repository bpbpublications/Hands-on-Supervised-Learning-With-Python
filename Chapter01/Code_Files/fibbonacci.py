num_terms = input("Enter the number of terms")
n = int(num_terms)
a = 0 #First Term
b = 1 #Second Term

i = 0

if(n <= 0):
    print("Please enter a valid number of terms")

if(n==1):
    print("Fibonacci series",a)

else:
    print("Fibonacci sequence upto",n,":")
    while i < n:
        print(a,end='  ')
        next = a + b
        #Update values
        a = b
        b = next
        i += 1
print("\n")

