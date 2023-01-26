#Create a variable called 'number' and assign it the three-digit number.
number = 678
#Find the 'number' first digit and assign to x1.
x1 = 8
#Find the 'number' second digit and assign to x2.
x2 = 7
#Find the 'number' third digit and assign to x3.
x3 = 6
#Create a variable called 'answer' and assign it the sum of the three digits x1, x2, x3.
x1 = number%10
x2 = number//10%10 
x3 = number//100 
answer =(x1+x2+x3)
#Print the value of the 'answer.
print(answer)