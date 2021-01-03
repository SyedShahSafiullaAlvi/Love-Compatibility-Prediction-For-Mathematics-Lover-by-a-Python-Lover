# Love-Prediction-Calculator-For-Fun

I am going to write a program that tests the compatibility between two people and displays a love message.

Finding love score between two beautiful people:
Take two name's as input and ask the user to enter a love phrase through which he/she wanna their love compatibility. Now the code checks number of times the alphabets in first word of love phrase occurs in names of both peoples and gives a count of occurence. Similarly for n number of words in love phrase. Then it combines these count occurences to make a n digit number. where n is number of words in a love phrase that gives a love score.


How it works:
name1 = "John Cena"      (If length of name is less than four characters, it asks user to again enter the name)
name2 = "Emma watson        "
love_phrase="True Love"

T occurs 1 times
R occurs 0 times
U occurs 0 times
E occurs 2 times
count1 = 3

L occurs 0 time
O occurs 2 times
V occurs 0 times
E occurs 2 times
count2 = 4

Now concatenating all counts
Love Score = 34
Now firstly check whether the love score is palindrome number, if it is palindrome then print respective love message. If it is not palindrome, then check whether it is a Armstrong number. If it is a armstrong number, print respective love message. If love score is neither palindrome nor Armstrong, check whether it is a prime number. If it is a prime number,print respective love message. If not go for odd even check. 

Final Output: Hey Emma Watson your one is all that is needed to complete John Cena. All the very best for your future life.


Example input: 
name1 = 'Shahrukh Khan'
name2 = 'Gauri Khan'
love_phrase="Get rich together"
Output: True love doesn't just fills heart, it overflows into whole soul.
        Hey Shahrukh Khan and Gauri Khan, you look beautiful together. 