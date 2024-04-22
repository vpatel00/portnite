#
# Questions that the user will be asked
# Tody Liang, Vir Patel, Henry Vogel, Marc Fernando
# 4/16/2024
#Used MARC FERNANDOs notes for questions heheheh
#"There is a good chance the principal will be here for the presentation
# so you might want to change the name" -Russ

#CHAT GPT questions 11-20
#hand made questions though 1-10 cause im him -Marc


#PYTHON QUESTIONS GOOGLE DOC
#GO HERE TO FORMAT THE GOOGLE DOC QUESTIONS
#https://docs.google.com/document/d/1ao9ye-vZoJHJFg5z3CDp0eO_OTIyrYR9SVZdYJlr8EI/edit

#Hello, Marc Here
import random 


# Questions done by me (Henry)

#--------------------------Question database--------------------------
questions = ["Every expression you see in python you start from order of operations?",  # Question 1

             "\nfor num in range(10):\nprint(num)",  # Question 2
            
             "If Tody wants to break apart a string into a list what would he use?",  # Question 3
            
             "Subclasses do what from a python class?",  # Question 4
            
             "Tody does what in Fortnite?",  # Question 5
            
             "What would this code display? HINT: LOOK CLOSELY!\n"
             "my_string = 'This is a string'\n"
             "  x = my_string.split()\n"
             "  print(x)\n"
             "    for item in x:\n"
             "      if item.isdigit():\n"
             "        print(item)",  # Question 6
            
             "5 % 3?",  # Question 7
            
             "x = 65.20934856\n"
             "x = int(65.209348567)\n"
             "print(x)",  # Question 8
            
             "What needs to happen for EITHER x or y to be True?",  # Question 9
            
             "If x or y is true, and x is False? What will this give you?",  # Question 10
            
             "What is the difference between ‘==’ and ‘is’ in Python?",  # Question 11
            
             "How do you handle exceptions in Python?",  # Question 12
            
             "Explain the difference between lists and tuples in Python.",  # Question 13
            
             "How can you concatenate two dictionaries in Python?",  # Question 14
            
             "numbers = [1, 2, 3, 4, 5]\n"
             "squared_numbers = [x ** 2 for x in numbers]\n"
             "print(squared_numbers)\n\n"
             "What does this code snippet do?",  # Question 15
            
             "import random\n"
             "random_number = random.randint(1, 100)\n"
             "print('Random number:', random_number)\n\n"
             "What does this code snippet do?",  # Question 16
             "What is the purpose of the pass statement in Python?",  # Question 17
            
             "What is the purpose of the __str__ method in Python classes?",  # Question 18
            
             "How do you open and read a file in Python?",  # Question 19
            
             "text = 'Hello, world!'\n"
             "reversed_text = text[::-1]\n"
             "print('Reversed text:', reversed_text)\n\n"
             "What does this code snippet do?", # Question 20

             "What type of address is physically assigned to the NIC of a workstation?", # Question 21

             "Which characteristic defines a private cloud?", # Question 22

             "Which is a characteristic of a Type 2 hypervisor?", # Question 23

             "Which IPv4 header field is responsible for defining the priority of the packet?", # Question 24

             "A network engineer subnets the network 192.168.100.0 /24 into 16 subnets. \nHow many usable host addresses will be available on each of the subnets?", # Question 25
             
             "What does WAN stand for?", # Question 26

             

            ]


#----------------------------------------------------
choices = ["A. True \nB. False", # Answer Choices 1
           
           "A. 0 to 10 \nB. 0 to 9 \nC. 1 to 9 \nD. 1 to 10\n", # Answer Choices 2
           
           "A. Split \nB. Break \nC. Chop \nD. Sever \n", # Answer Choices 3
           
           "A. Take from a class above the subclass \nB. Take from a class below the subclass \nC. Take from a subclass class below the class \nD. Take from a class below the subclass \n", # Answer Choices 4
           
           "A. Win \nB. Lose \nC. Crank 90s on school laptop \nD. A and C \n", # Answer Choices 5
           
           "A. ['This', 'is', 'a', 'string'] \nB. (‘This’ ‘is’ ‘a’ ‘string) \nC. {'This', 'is', 'a', 'string'} \nD. ['This' 'is' 'a' 'string'] \n", # Answer 6
           
           "A. 2 \nB. 2.1 \nC. 2.09 \nD. What if I ask nicely? \n", # Answer Choices 7
           
           "A. 65.3 \nB. 65.2 \nC. 65.209348567 \nD. 65 \n", # Answer Choices 8
           
           "A. And \nB. Or \nC. Also \nD. Else   \n", # Answer Choices 9
           
           "A. True \nB. False \n", # Answer Choices 10
           
           "A. ‘==’ compares the values of two objects, ‘is’ checks if two objects refer to the same memory location. \nB. ‘==’ is used for assignment, while ‘is’ is used for comparison. \nC. ‘==’ is used for shallow comparison, while ‘is’ is used for deep comparison. \nD. ‘==’ checks for object identity, while ‘is’ checks for equality. \n", # Answer Choices 11
           
           "A. IGNORE THEM!!!! \nB. Using try-except blocks \nC. By writing defensive code to prevent exceptions \nD. Comment out the code \n", # Answer Choices 12
           
           "A. Lists are immutable, while tuples are mutable. \nB. Tuples can contain elements of different data types, while lists cannot. \nC. Lists are ordered collections, while tuples are unordered. \nD. Lists use square brackets [ ], while tuples use parentheses ( ). \n", # Answer Choices 13
           
           "A. Using the + operator. \nB. Using the extend() method. \nC. Using the concat() function. \nD. Using the update() method. \n", # Answer Choices 14
           
           "A. Prints the same 5 numbers. \nB. Generates a list of squared numbers from 1 to 5. \nC. Calculates the sum of squared numbers. \nD. Prints the original numbers list. \n", # Answer Choices 15
           
           "A. Generates a random number between 1 and 100 and prints it. \nB. Prints a predetermined random number. \nC. Imports the random module. \nD. Generates a random number between 1 and 10. \n", # Answer Choices 16
           
           "A. It is used to halt the execution of a program. \nB. It is used as a placeholder when no action is required. \nC. It is used to define a conditional block of code. \nD. It is used to raise an exception. \n", # Answer Choices 17

           "A. It converts a string to a numerical value. \nB. It is used to define a string representation of an object. \nC. It is a reserved method for internal use. \nD. It is used to compare two objects for equality. \n", # Answer Choices 18

           "A. Using the open() function with the mode r and then read() method. \nB. Using the read_file() function with the file path as an argument. \nC. Using the load_file() function from the io module. \nD. Using the open_file() function with the mode w and then write() method. \n", # Answer Choices 19

           "A. Removes all punctuation marks from the text. \nB. Prints the text in reverse order. \nC. Encrypts the text using a Caesar cipher. \nD. Reverses the given text string. \n", # Answer Choices 20

           "A. IP address. \nB. host address. \nC. MAC address. \nD. network address", # Answer Choices 21

           "A. intended for a specific organization \nB. available to the general public \nC. composed of two or more clouds \nD. created for a specific community", # Answer Choices 22

           "A. best suited for enterprise environments \nB. installs directly on hardware \nC. has direct access to server hardware resources \nD. does not require management console software", # Answer Choices 23

           "A. flow label \nB. flags \nC. differentiated services \nD. traffic class", # Answer Choices 24

           "A. 6 \nB. 14 \nC. 30 \nD. 62", # Answer Choices 25
           
           "A. Metropolitan Area Network \nB. Local Area Network \nC. Wide Area Network \nD. Wide Arena Network" #Answer choice 26
          ]


#-----------------ANSWER KEY-------------------------
answers = ["A", # Answer 1
           "B", # Answer 2
           "A", # Answer 3
           "A", # Answer 4
           "D", # Answer 5
           "A", # Answer 6
           "A", # Answer 7
           "D", # Answer 8
           "B", # Answer 9
           "A", # Answer 10
           "A", # Answer 11
           "B", # Answer 12
           "D", # Answer 13
           "D", # Answer 14
           "B", # Answer 15
           "A", # Answer 16
           "B", # Answer 17
           "B", # Answer 18
           "A", # Answer 19
           "D", # Answer 20
           "C", # Answer 21
           "A", # Answer 22
           "D", # Answer 23
           "C", # Answer 24
           "B", # Answer 25
           "C", # Answer 26
          ]


q_and_a = list(zip(questions, choices, answers))

def ask_question(q_and_a):
  random_question = random.choice(q_and_a)
  print(random_question[1])
  player_answer = input(f"What is the answer to '{random_question[0]}': ").upper()
  
  if player_answer == random_question[2] or player_answer == "M": #heheh dev cheat >:)
    # Bro why is there a dev cheat here 💀
    print("Correct!")
    return True
  else:
    print("Incorrect!")
    return False
  

