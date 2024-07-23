#self-learning python
#Chapter one to three
message="Hello!Jiayin"
print(message)
message="Hello!Smallbox"
print(message)
name="Jiayin"
print(name.title())
name="pUmi"
print(name.lower())
print(name.upper())
first_name="pumi"
last_name="omi"
full_name=f"{first_name}{last_name}"
print(f"Hello,{full_name.title()}!")
print("Python")
print("\nPython")
print("characters of Jiayin:\n\t\t\tKorea_dance\n\t\t\tRobots\n\t\t\tAcademic")
favorite_party='Yes '
favorite_party=favorite_party.rstrip()
print(favorite_party)
name="Eric"
print(f"Hello {name},would you like to learn Python today?")
name="jiAyin"
print(name.title())
print(name.lower())
print(name.upper())
name="Nayeon"
proverbs=f'{name} once said,"there are truly many girls prettier than me,But I love myself more"'
print(proverbs)
famous_person="Taloyerswift"
message="ever be shame of your efforts"
print(f'{famous_person} once said,"{message}"')
vocal,dance,rap="jennie","Lisa","jennie"
print(f"{vocal} is the vocal of Blackpink")
print(f"{dance} is the dance of Blackpink")
print(f"{rap} is the rapper of Blackpink")
Twice=['Nayeon','Sana','Tzuyu']
print(Twice)
print(Twice[-1])
Languages=['C plus plus','Java','Python']
print(Languages)
Languages.append('C#')
print(Languages)
#append elements to the blank list 
itzy=[]
itzy.append('Lia')
itzy.append('Liuzhen')
itzy.append('Yuna')
itzy.append('Chaeryeong')
print(itzy)
#insert element to the previous list
letters=['A','B','D']
letters.insert(2,'C')
print(letters)
#delete the element from the previous list
#Way one:delete through the del statement
itzy=['Chaeryeong','Yuna','Lizhi']
print(itzy)
del itzy[0]
print(itzy)
#Way Two:delete through the fuction pop()
motocycles=['honda','yamaha','suzuki']
print(motocycles)
popped_motocycles=motocycles.pop()
print(motocycles)
last_owned=popped_motocycles
print(last_owned)
print(f'The last motocycle I buy is {last_owned}')
#search the value and delete it
GirlGroup=['Twice','Blackpink','Red velvet','Babymonster']
print(GirlGroup)
Dislike='Babymonster'
GirlGroup.remove(Dislike)
print(GirlGroup)
print(f'What I dislike is GirlGroup "{Dislike}"')
#Have a try
dinnerlist=['Mom','Bob','Lucy']
print(f'Wanna have these ones to have a delicious meal with me,they are{dinnerlist}')
absent_person=dinnerlist[2]
del dinnerlist[2]
print(f'Cause {absent_person} is busy,I invite Tim')
#dinnerlist=dinnerlist.insert(2,'Tim')
#Hey!Wonder to know why the output of 'dinnerlist' is 'none'?Let me tell you,cause the function
#insert（）does not return the modified list,so the variable 'dinnerlist'can not receive the modified result
#That's why you get 'none'
#do like this you can get the right result you want
dinnerlist.insert(2,'Tim')
print(dinnerlist) 
#send invitations to everyone 
print(f"Hello,my dear {dinnerlist[0]},have dinner with me tonight")
print(f"Hello,my  friend {dinnerlist[1]},have dinner with me tonight")
print(f"Hello,my   friend {dinnerlist[2]},have dinner with me tonight")
#invite more cause I find a bigger dinning-table
print(f"Hello,guys!I've got a big table to contain more friends")
dinnerlist.insert(0,'Ketty')
print(dinnerlist)
dinnerlist.insert(2,'Anne')
print(dinnerlist)
dinnerlist.append('somi')
print(dinnerlist)
#send invitations to everyone 
print(f"Hello,my friend {dinnerlist[0]},have dinner with me tonight")
print(f"Hello,my dear {dinnerlist[1]},have dinner with me tonight")
print(f"Hello,my friend {dinnerlist[2]},have dinner with me tonight")
print(f"Hello,my friend {dinnerlist[3]},have dinner with me tonight")
print(f"Hello,my friend {dinnerlist[4]},have dinner with me tonight")
print(f"Hello,my friend {dinnerlist[5]},have dinner with me tonight")
#Sad to say that the new table can not arrive in time
#Sorry the table could just contain two
print(f'I am truly sorry to say that the table can only contain two people')
popped_person_one=dinnerlist.pop()
print(f'Sorry,{popped_person_one},let us have a meal next time')
popped_person_two=dinnerlist.pop()
print(f'Sorry,{popped_person_two},let us have a meal next time')
popped_person_three=dinnerlist.pop()
print(f'Sorry,{popped_person_three},let us have a meal next time')
popped_person_four=dinnerlist.pop()
print(f'Sorry,{popped_person_four},let us have a meal next time')
print(f'Lucky you!{dinnerlist[0]},you are still invited')
print(f'Lucky you!{dinnerlist[1]},you are still invited')
del dinnerlist[0]
print(dinnerlist)
#If I write dinnerlist[1],the traceback will show out of range,cause there is only one element
del dinnerlist[0]
print(dinnerlist)
#use sort() function to sort the list 
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#use sorted() function to show a temporary list
print('Here is the original list')
print (f"\t\t\t\t{cars}")
print('Here is the sorted list')
print (f"\t\t\t\t{sorted(cars)}")
print('Here is the original list')
print (f"\t\t\t\t{cars}")
#use reverse=True statement to change the order of the letters
#and use the function reverse() to reverse the original order of the list
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
#back to the original state,just use reverse() again
cars.reverse()
print(cars)
#Ensure the length of the list,use len()
length=len(cars)
print(length)
#Have a try
places=['B','A','E','D','C']
print(sorted(places))
print(places)
#print the list sorted in reverse alpabetical order
#Here just pass two arguments to the sorted() function
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
#How many guests
dinnerlist=['Tom','Bob','Ketty']
print(f"There are {len(dinnerlist)} guests to have dinner with me")
#try to use all the function this chapter learnt
favorite_kpop_dance=['Into the new world','Yes or Yes','Heart Shaker','Dalla Dalla']
favorite_kpop_dance.append('Forever Young')
print(favorite_kpop_dance)
favorite_kpop_dance.sort()
print(favorite_kpop_dance)
#there are too many functions in this chapter ,I am tired to list them all,sorry 
