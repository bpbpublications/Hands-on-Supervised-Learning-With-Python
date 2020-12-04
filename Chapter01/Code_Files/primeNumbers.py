input1 = input("What is the range of numbers? Enter the first number")
input2 = input("What is the range of numbers? Enter the second number")

input1 = int(input1)
input2 = int(input2)

for i in range(input1,input2):
    if i > 1:
        for j in range(2,i//2):
            if(i%j == 0):
                break
        else:
            print(i)
