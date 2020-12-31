
#Taking two names as input 
name1=input("Enter your name:")             
name2=input("Enter your partner's name:")

# Making both names in upper case and concatenating them into a single string
name=name1.upper()+' '+name2.upper() 

count1,count2=0,0  #one count for TRUE and another for LOVE

# Applying for loop, checking each letter of 'TRUE' against the name.
# Incrementing count on each match
for i in 'TRUE':
    count1 += name.count(i)

# Applying for loop, checking each letter of 'LOVE' against the name.
# Incrementing count on each match
for i in 'LOVE':
    count2 += name.count(i)

#Concatenating counts of TRUE and LOVE. 
count=str(count1)+str(count2)
count=int(count)            #Type casting string into integer.


if 0<count<=25:             #Condition checking
    print(f"Your love score is {count},  you go together like coke and mentos.")
elif 25<count<=50:
    print(f"Your love score is {count}, you are alright together.")
elif 50<count<=75:
    print(f"Your love score is {count}, you are perfect together.")
elif 75<count<=100:
    print(f"Your love score is {count}, you are made for each other.")

print("-------------------------------------------------")
print("Hey! This was just for fun, Don't take it seriously hehehe.\nYou people are great! BIG LOVE.")