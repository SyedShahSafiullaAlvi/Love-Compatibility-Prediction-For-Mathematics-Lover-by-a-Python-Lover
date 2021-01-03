#Taking two names as input 
name1=input("Enter your name:") 
while len(name1):                                # number of letters in name entered by user should compramize more than three letters
    if len(name1)<4:                        # if not asking the user to enter a name with minimum of four letters
        print("Please enter a name consisting a minimum of 4 letters.")
        name1=input("Enter your name:")
    if len(name1)<4:
        continue
    else:
        break
                
name2=input("Enter your partner's name:")
while len(name2):                             # similarly number of letters in name entered by user should compramize more than three letters
    if len(name2)<4:                    # if not asking the user to enter a name with minimum of four letters
        print("Please enter a name consisting a minimum of 4 letters.")
        name2=input("Enter your partner's name:")
    if len(name2)<4:
        continue
    else:
        break
#Asking user to enter love phrae through which he/she wanna test compatibility
love_phrase=input("Enter the testing phrase through which you wanna check your compatibility.")

phrase_list=love_phrase.split()          # Type casting the string into list for further operations
term=len(phrase_list)               # Gives number of elements in list i.e number of words in love_phrase
name=name1.upper()+' '+name2.upper()    # Concatenating both names into a single name
count_list=[ ]                  # defining an empty list to store count of each alphabet in each word in love phrase
j=0                             # defining a variable j to iterate through the list
while term!=0:
    count=0                    # variable to store count individually of a word and allocated a zero value at start of loop
    for i in phrase_list[j].upper():
        count+=name.count(i)

    count_list.append(count)        # storing the count in the list
    term=term-1
    j=j+1                           # incrementing j by one in order to access next element of list

love_score=''                      # initializing an empty string to concatenate count_list elements into a single string
for element in count_list:
    love_score=love_score+str(element)

love_score=int(love_score)            # type casting string into integer for condition checking
print(f"Love score of {name1} and {name2}, based of love phrase '{love_phrase}' is {love_score}")

# Functions for PALINDROME, ARMSTRONG, PRIME & ODD_EVEN checking 

def odd_even(num):  
    if num%2==0:                # function to check whether love_score is even or odd 
        print(f"True love doesn't just fills heart, it overflows into whole soul.\nHey {name1} and {name2}, you look beautiful together.")
    elif num%2!=0:
        print(f"In the arithmetic of love, one plus one equals everything, and two minus one equals nothing.")
        print(f"Hey you lovely people {name1} and {name2}, Be always together.") 


def prime(num):                 # function to check whether love_score is prime
    count=0
    for i in range(2,(num//2)+1):
        if num%i==0:
            count+=1
            break

    if count==0:                    # if love_score is a prime number, print this message
        print(f"Hey {name2} your love is all that is needed to complete {name1}. All the very best for your future life.")
    else:
        num=love_score
        odd_even(num)               # or else check for whethwr it is a even or odd number



def armstrong(num):              # function to check whether love_score is Armstrong number
    num,sum=love_score,0
    while num!=0:
        rem=num%10
        sum=sum+rem**3
        num=num//10 
    if sum==love_score:              # if love_score is a Armstrong, print this message 
        print(f"Hey {name2}, loving you was never an option for {name1}, It was a necessity.")
    else:
        num=love_score              
        prime(num)                  # or else check for whethwr it is a prime number

def palindrome(num):         # function to check whether love_score is palindrome
    rev=0
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if rev==love_score:                 # if love_score is a palindrome, print this message 
        print(f"True love cannot be found where it does not exist, nor can it be denied where it does.")
        print(f"Hey you the lovely people {name1} and {name2}, You can't deny the beautiful love between you.")
    else:                                           
        num=love_score
        armstrong(num)              # or else check for whether it is a armstrong number

palindrome(love_score)

print("\n\n-------------------------------------------------")
print("Hey! This was just for fun, Don't take it seriously hehehe.\nYou people are great! BIG LOVE.")