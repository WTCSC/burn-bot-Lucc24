print("Hello, dumbasses!")
name=input("what is your name? ")
age=int(input("how old are you? "))
hasHappened=input("have you had your birthday this year? (yes/no) ")
if hasHappened.lower()=="no":
    age+=1
elif hasHappened.lower()!="yes"or hasHappened.lower()!="no":
    hasHappened=input("have you had your birthday this year? (yes/no) ")
currentYear=2025
birthYear=currentYear-age
food = input("whats your favorite food? ")
color = input("whats your favorite color? ")
age =age -1
print("\nyour responses will now be considered.\n")
print (f"I could have chosen a better name then {name} back in the 1800s. Thats possibly the weirdest thing ive ever heard.\nAnd you're only {age}? Just wait for my age (345). It gets so much worse. Born in {birthYear} I see?. Well at least you missed everything cool thats ever happened in the course of history.\nAnd your favorite food is {food}, huh? I dont think i could think of a more basic food if I tried.\nAlso, imagine liking {color} in the big 2025. Come on, choose a cool color like phtalo green.\nThanks for sharing! All of your data will now be sent to your local police station. Expect a call soon :) \nBye nerds!")