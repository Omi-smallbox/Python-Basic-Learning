#indentations in Python
magicians=['alice','david','carolina']
for magician in magicians:
        print(f'I can not wait to see you,{magician.title()}')
print("Thank you!")
#Have a try
pizzas=["New Orleans Pizza","Supreme Pizza","Seafood Pizza"]
for pizza in pizzas:
        print(f"I like {pizza}pizza")
print("I really love pizza!")

animals=['alpaca','dog','cat']
for animal in animals:
        print(f"{animal} is cute")
print("Any of these animals would make a great pet!")
#create a number list
#Do not forget the colon in for cycle
'''
Use the function range()
'''
for value in range(1,5):
 print(value)
'''
Use the function range() to create the number list
use the function list() to tranfer the result of list
'''
numbers=list(range(1,6))
print(numbers)
'''
Set the step length
'''
even_numbers=list(range(2,11,2))
print(even_numbers) 
'''
Do not forget the colon
'''
squares=[]
for value in range(1,11):
   square=value**2
   squares.append(square)
print(squares)
'''
functions to deal with numbers
'''
digits=[1,2,3,4,5,6,7,8,9,0]
min=min(digits)
max=max(digits)
sum=sum(digits)
print(min)
print(max)
print(sum)
'''
list comprehension
suqare number lists
'''
squares=[value**2 for value in range(1,11)]
print(squares)
#Have a try
for value in range(1,21):
      print(value)
#for num in range(1,1000001):
 #     print(num)   
 #Be mindful of the order of the parameters in range()
for odd_number in range(1,20,2):
      print(odd_number)
'''
4-7
'''    
numbers=[num for num in range(3,31) if num%3==0]
for number in numbers:
      print(number)
'''
4-8
make a list and print it
'''
lists=[]
for value in range(1,11):
    lists.append(value**3)
for num in lists:
      print(num)
'''
4-9
'''
list=[value**3 for value in range(1,11)]
print(list)
#handle certain elements of the list"
'''
 Output: the elements which  indexes are from 0 to 2-1
'''
dances=['momo','lisa','karina']
print(dances[0:2])
print(dances[-2:])
'''
copy the list
'''
my_hobbies=['kpop','robots','makeup']
my_friend_hobbies=my_hobbies[:]
my_hobbies.append('games')
my_friend_hobbies.append('Binge-watching on Netflix')
print(my_hobbies)
print((my_friend_hobbies))
#Have a try
my_hobbies=['kpop','robots','makeup','music','rap']
print(f'The first three items in the list are:')
print(my_hobbies[0:3])
print(f'Three items from the middle of the list are:')
print(my_hobbies[1:4])
print(f'The last three items in the list are:')
print(my_hobbies[-3:])
'''
4-11
'''
pizzas=["New Orleans Pizza","Supreme Pizza","Seafood Pizza"]
friend_pizzas=pizzas[:]
pizzas.append("Fruit Pizza")
friend_pizzas.append("Vegetable Pizza")
print("My favorite pizzas are: ")
for pizza in pizzas:
      print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
      print(friend_pizza)
'''
for cycle
'''
foods=['cakes','sandwiches','KFC']
print(foods)