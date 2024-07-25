#Have a try
dinner='beef'
print("Is dinner==beef?I predict True")
print(dinner=='beef')
# if statement
age=19
if age>=18:
    print("You are old enough to vote")
    print("Have you registerd to vote yet?")
# if-else statement
age=17
if age>=18:
    print("You are old enough to vote")
    print("Have you registerd to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
#if-elif-else
age=12
if age<4:
    print("Your admission is $0")
elif age<18:
    print("Your admission is $25")
else:
    print("Your admission is $40")
#Have a try
'''
color of aliens
'''
alien_color='green'
if alien_color=='green':
    print("You get five points")
else:
    print("You get ten points")
#version one
print('T5-5:(assume the color of the alien is green)')
alien_color="green"
if alien_color=='green':
    print("\t\t\tYou get 5 points!")
elif alien_color=='yellow':
    print("You get 10 points")
elif alien_color=='red':
    print("You get 15 points")

print('T5-5:(assume the color of the alien is yellow)')
alien_color="yellow"
if alien_color=='green':
    print("\t\t\tYou get 5 points!")
elif alien_color=='yellow':
    print("\t\t\tYou get 10 points")
elif alien_color=='red':
    print("\t\t\tYou get 15 points")

print('T5-5:(assume the color of the alien is red)')
alien_color="red"
if alien_color=='green':
    print("\t\t\tYou get 5 points!")
elif alien_color=='yellow':
    print("\t\t\tYou get 10 points")
elif alien_color=='red':
    print("\t\t\tYou get 15 points")

print("T5-6 diffrent stages of life")
age=18
if age<2:
    print("Baby!")
elif age<4:
    print("Toddler!")
elif age<13:
    print("Kid!")
elif age<20:
    print("\t\t\t\tTeenager!")
elif age<65:
    print("Adult!")
else:
    print("Elder!")
print("5-7 favorite fruits")
favorite_fruits=['Apple','Banana',"Peach"]
fruit='watermelon'
if 'Apple' in favorite_fruits:
    print("\t\t\tYou really like Apples!")
if fruit not in favorite_fruits:
    print("\t\t\tYou do not like Watermelon!")
#use if statement to handle list
#Have a try
print("T5-8 Say Hello to managers in a special way")
namelists=['admin','Sassybox','Pumi','Sexybox','Omi']
for name in namelists:
    if name=='admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {name} ,thank you for logging in again")
    
print("T5-9 deal with the situation without users")
namelists=[]
if namelists:
  for name in namelists:
    if name=='admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {name} ,thank you for logging in again")
else:
        print("\t\t\tWe need to add some users first!")

print("5-10  check the username")
current_users=['a','B','C','D','E']
new_users=['A','F','G','H','I']
current_users_lower=[current_user.lower() for current_user in current_users]
for new_user in new_users:
    if new_user.lower()  in current_users_lower:
        print(f"the name {new_user}  is not available")
    else:
        print(f"the name {new_user}  is available")
print("5-11")
numberlists=[1,2,3,4,5,6,7,8,9]
for number in numberlists:
    if (number==1):
        print(f'{number}st')
    elif(number==2):
        print(f'{number}nd')
    elif(number==3):
        print(f'{number}rd')
    else:
        print(f'{number}th')