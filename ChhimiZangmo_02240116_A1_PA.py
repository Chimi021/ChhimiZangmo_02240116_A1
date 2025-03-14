# PART A : Python Functions Assignment

def sum_of_primenumbers():
    from primePy import primes #importing the primePy library for prime numbers
    S = int(input("Enter the strat range:"))
    E = int(input("Enter the end range: "))
    s = primes.between (S,E)
    s2 = primes.between (E,S)
    t = 0
    for sum in s or s2:
        t += sum # putting the sum of the prime numbers in the t variable
    print("The sum of the prime numbers is, ", t)
#sum_of_primenumbers()

def length_converter ():
    MF = str(input ("Would you like to convert meter to feet(M) or feet to meter (F) : "))
    if MF == 'M':
       l = float(input ("Enter length: "))
       #1 meter = 3.28084 feet
       print ("Your length in feet is, " , round((l*3.28084),2) , "feet")
        #rounding off the value to 2 decimal places
    elif MF == 'F':
       f = float(input ("Enter length: "))
       print ("Your lenght in meter is,", round((f/3.28084),2) , "m")
    else:
        print("Please enter 'M' or 'F'. ")
#length_converter()

def Consonant_counter ():
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    #putting both upper case and lowercase consonants in the same variable
    t = input("Enter the sentence: ")
    c = sum(1 for x in t if x in consonants ) #summing up the consonants in the sentence
    print ("Your sentence have ", c ,"consonants")
#Consonant_counter ()

# Min-Max Number Finder
def MM_finder ():
    No = float(input("How many numbers would you like to input?: "))
    if No <= 0:#checking if the number is greater than zero
        print ("Please enter a number greater than zero.")
        return 
    n = input ("Enter the numbers speprated by a coma:")
    list = [float(number) for number in n.split(",")]#splitting the numbers by coma
    L = max(list) 
    S = min(list)
    print ("Largest number is", L , "and the smallest number is, ", S ,".")
#MM_finder ()

# Palindrome checer
def PalindromeChecker():
    pd = str(input("Enter the string: "))
    if bool(pd == pd[::-1]):
         # [::-1] a slicing technique(extracts of a part of a string, list, or tuple)
         #- reverses the string
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
#PalindromeChecker()

def read_file(filename):
    file = open(filename, 'r')#r = read mode(for reading only) ,
    #similiarly w = write mode and a= append mode
    content = file.read()#
    file.close()# closes the file after getting the content
    return content

def count_words(content):
    dictionary = {'the': 0, 'and': 0, 'was': 0}#creating a dictionary to count the given words
    words = content.lower().split()#changing all the words in the file to lowercase for easy counting
    for w in words:
        if w in dictionary:
            dictionary[w] += 1#counting each words words(w)+ 1 = words
    return dictionary

def W_counter():
    filename = input("Enter the filename: ")
    c = read_file(filename)
    print(f"Length of the content: {len(c)}")
    #f - f-strings it allows us to embed expressions(like len()inside {} brackets
    word_counts = count_words(c)
    print(f"Word counts: {word_counts}")
# W_counter()

def MENU():
    print("You have six different functions to choose from!! The functions are given bellow.")
    print("1) Calculate the sum of prime numbers.")
    print("2) Convert meter to feet or feet to meter.")
    print("3) Find consonants in a string.")
    print("4) Find the maximum and minimum number.")
    print("5) Check for palindrome.")
    print("6) Word counter.")
    print("7) Exit")
#MENU ()

while True:#looping the menu until the user wants to exit
    MENU()         
    c = input("What would you like to do? Enter a number(1-7):")
    if c == '1':
        sum_of_primenumbers()
    elif c == '2': 
        length_converter()
    elif c == '3': 
        Consonant_counter()
    elif c == '4': 
        MM_finder()
    elif c == '5':
        PalindromeChecker()
    elif c == '6':
        W_counter()
    elif c == '7':
        print("Thank you for visiting. ^U^")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 7.")
    try_again = input("Would you like to try again? (Y/N): ")
    if try_again == 'Y' :
        continue
    elif try_again == 'N':
        print("Thank you for visiting. ^U^")
        break 
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")



