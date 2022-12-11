#bill splitting with lucky guy option

import random
print("Enter the number of friends joining (including you):")
number = int(input())
friends = {}
if number == 0 or number < 0:
    print()
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(1, number+1):
        names = input()
        friends.update({names: 0})
    print("Enter the total bill value:")
    bill = input()
    friends_keys = list(friends.keys())
    for j in friends_keys:
        friends.update({j: round((int(bill)/len(friends)), 2)})
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer.capitalize() == "Yes":
        lucky = random.choice(friends_keys)
        print("{} is lucky one!".format(lucky))
        for j in friends_keys:
            if j == lucky:
                friends.update({j: 0})
            else:
                friends.update({j: round(((int(bill)/(len(friends)-1))), 2)})
        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)
        
        
    
        
        
        
        
              
   
        
