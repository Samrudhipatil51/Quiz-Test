import time
import sys
from replit import db

print("Quiz:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = [
    "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
    "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
    "[■■■■■■■■■□]", "[■■■■■■■■■■]"
]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
import quiz

print("*****************Quiz*********************")
print("WELCOME TO TODAYS QUIZ")


def bio():
    while True:
        name = str(input("Please Enter your Name: -"))
        print("Hello" + "," + name)
        Age = input("Enter your Age: -")
        print("Select your subject you want to play")
        print("Subject options: PP,MP,AoA,DBMS,OS")
        quiz = str(input(" Enter the name of the subject you want:"))
        if quiz == "PP":
            print(Python())
        elif quiz == "MP":
            print(Microprocessor())
        elif quiz == "AoA":
            print(Analysisof_Algorithm())
        elif quiz == "DBMS":
            print(Databasemanagement_System())
        elif quiz == "OS":
            print(Operating_System())
        break


def Python():
    while True:
        print("Answer the following Questions ")
        print("Question 1:Who developed the python language")
        print("\n1.Guido Van Rossum \t2.Zim Den \t3.Niene Stom \t4.Wick van Rossum")
        sol = str(input("Enter your Answer:"))
        if sol == "Guido Van Rossum":
            print("correct answer")
        else:
            print("wrong answer")

        print("Question 2:In Which year was the python language developed")
        print("\n1.1992 \t.1972 \t3.1981 \t4.1989")
        sol2 = str(input("Enter your answer:"))
        if sol2 == "1989":
            print("correct answer")
        else:
            print("wrong answer")
        print("Question 3:It tuple mutable?")
        sol3 = str(input("Answer Yes Or No: -"))
        if sol3 == "No":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 4: Which one of the following has highest precedence in the expression"
        )
        print("\n1.Exponitial \t2.Addition \t3.Mutiplication \t4.Parentheses")
        sol4 = str(input("Enter your answer: -"))
        if sol4 == "Parentheses":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 5: Which of the following data types is not supported in python"
        )
        print("\n1.List \t2.String \t3.Slice \t4.Numbers")
        sol5 = str(input("Enter your answer: -"))
        if sol5 == "Slice":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 6: Which one of following us not a python predefined data type?"
        )
        print("\n1.Class \t2.List \t3.Attribute \t4.Arragument")
        sol6 = str(input("Enter your answer: -"))
        if sol6 == "Class":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 7: Which operator has higher precedence in the list")
        print("\n1.+Addition \t2.**Exponent \t3.-Substraction \t4.*Mutiply")
        sol7 = str(input("Enter your answer: -"))
        if sol7 == "**Exponent":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 8: What is the method inside the class in python language"
        )
        print("\n1.String \t2.Function \t3.Class \t4.List")
        sol8 = str(input("Enter your answer: -"))
        if sol8 == "Function":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 9: Which of the operation is the correct for power(ab)")
        print("\n1.a^b \t2.a**b \t3.a^^b \t4.a^*b")
        sol9 = str(input("Enter your answer: -"))
        if sol9 == "a**b":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 10:Are nested if-else are allowed in python")
        sol10 = str(input("Answer Yes or No: -"))
        if sol10 == "Yes":
            print("correct answer!")
        else:
            print("wrong answer")
            playagain = input("would you like to play again:Yes or No: -")
        if playagain == "yes":
          print(bio())
        else:
            print("Thanks for playing the quiz Goodbye!")
            break
def Microprocessor():
    while True:
        print("Answer the following Questions ")
        print("Question 1:What is the size of intel 8086 microprocessor")
        print("\n1.4 bit \t2.8 bit \t3.16 bit \t4.20 bit")
        sol = str(input("Enter your Answer:"))
        if sol == "8 bit":
            print("correct answer")
        else:
            print("wrong answer")

        print("Question 2:What is size of Address bus in 8086 microprocessor")
        print("\n1.16 bit \t2.8 bit \t3.32 bit \t4.20 bit")
        sol2 = str(input("Enter your answer:"))
        if sol2 == "20 bit":
            print("correct answer")
        else:
            print("wrong answer")
        print("Question 3:In Which year,8086 microprocessor was introduced?")
        print("\n1.1976 \t2.1978 \t3.1981 \t4.1977")
        sol3 = str(input("Enter your Answer: -"))
        if sol3 == "1978":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 4: The work of EU is")
        print("\n1.Encoding \t2.Decoding \t3.Processing \t4.Calculation")
        sol4 = str(input("Enter your answer: -"))
        if sol4 == "Decoding":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 5:The CF is known as")
        print("\n1.Carry Flag \t2.Common Flag \t3.Condition Flag \t4.Single Flag")
        sol5 = str(input("Enter your answer: -"))
        if sol5 == "Single Flag":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 6:The index are used to hold______")
        print("\n1.Memory Resigter \t2.Offset Address \t3.Segment Memory \t4.Offset Memory")
        sol6 = str(input("Enter your answer: -"))
        if sol6 == "Memory Resigter":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 7: The first digital electronic computer was built in the year______"
        )
        print("\n1.1920 \t2.1940 \t3.1030 \t4.1925")
        sol7 = str(input("Enter your answer: -"))
        if sol7 == "1930":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 8:The register AX is formed by grouping_______")
        print("\n1.BH and BL \t2.AH and AL \t3.CH and CL \t4.DH and DL")
        sol8 = str(input("Enter your answer: -"))
        if sol8 == "AH and AL":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 9:IMUL source is a signed_______")
        print("\n1.Addition \t2.Division \t3.Mutiplication \t4.Substraction")
        sol9 = str(input("Enter your answer: -"))
        if sol9 == "Mutiplication":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 10:8085 microprocessor has how many pins")
        print("\n1.31 \t2.33 \t3.40 \t4.30")
        sol10 = str(input("Enter your Answer: -"))
        if sol10 == "40":
            print("correct answer!")
        else:
            print("wrong answer")
        playagain = input("would you like to play again:Yes or No: -")
        if playagain == "yes":
            print(bio())
        else:
            print("Thanks for playing the quiz Goodbye!")
            break
def Analysisof_Algorithm():
    while True:
        print("Answer the following Questions ")
        print(
            "Question 1:What is the worst case time complexity of linear search algorithm?"
        )
        print("\n1.O(nlogn) \t2.O(n) \t3.O(n^2) \t4.O(logn)")
        sol = str(input("Enter your Answer:"))
        if sol == "O(n)":
            print("correct answer")
        else:
            print("wrong answer")

        print("Question 2:An algorithm is")
        sol2 = str(input("Enter your answer:"))
        if sol2 == "A step by step procedure to solve problem.":
            print("correct answer")
        else:
            print("wrong answer")
        print(
            "Question 3:Which of these algorithmic approach tries to achieve localized optimum solution −"
        )
        print("\n1.Greedy approach \t2.Divide and conquer approach \t3.Dynamic approach \t4.All the above")
        sol3 = str(input("Enter your Answer: -"))
        if sol3 == "Greedy approach":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 4:Which of the following uses memoization?")
        print("\n1.Greedy approach \t2.Divide and conquer approach \t3.Dynamic programming approach \t4.None of the above")
        sol4 = str(input("Enter your answer: -"))
        if sol4 == "Dynamic programming approach":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 5:The time complexity of quick sort is …………..")
        print("\n1.O(nlogn) \t2.O(n) \t3.O(n^2) \t4.O(logn)")
        sol5 = str(input("Enter your answer: -"))
        if sol5 == "O(nlogn)":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 6:The two main resources that we consider for an algorithm are__________."
        )
        print("\n1.Memory space and processor time \t2.Space complexity and time complexity \t3.Input and output properties \t4.None of the above")
        sol6 = str(input("Enter your answer: -"))
        if sol6 == "Memory space and processor time":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 7:In the analysis of algorithms, what plays an important role?"
        )
        print("\n1.Time Analysis \t2.Growth factor \t3.Time \t4.None of the above")
        sol7 = str(input("Enter your answer: -"))
        if sol7 == "Growth factor":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 8:A function in which f(n) is Ω(g(n)), if there exist positive values k and c such that f(n)>=c*g(n), for all n>=k. This notation defines a lower bound for a function f(n):"
        )
        print("\n1.Big Omega (f) \t2.Big Theta (f) \t3.Big Oh (f) \t4.None of the above")
        sol8 = str(input("Enter your answer: -"))
        if sol8 == "Big Omega  (f)":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 9:The amount of time the computer needs to run to completion is known as_____."
        )
        print("\n1.Space complexity \t2.Time complexity \3. Recursive function \t4.None of the above")
        sol9 = str(input("Enter your answer: -"))
        if sol9 == "Time complexity":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 10:Which of the following sorting algorithms does not have a worst case running time of O(n2)?"
        )
        print("\n1.Quick sort \t2.Merge sort \t3.Bubble sort \t4.Mix sort")
        sol10 = str(input("Enter your Answer: -"))
        if sol10 == "Merge sort":
            print("correct answer!")
        else:
            print("wrong answer")
        playagain = input("would you like to play again:Yes or No: -")
        if playagain == "yes":
            print(bio())
        else:
            print("Thanks for playing the quiz Goodbye!")
            break


def Databasemanagement_System():
    while True:
        print("Answer the following Questions ")
        print("Question 1:Which of the following in not a function of DBA?")
        print("\n1.Network Maintenance \t2.Schema Definition \t3. Authorization for data access \t4. Routine Maintenance ")
        sol = str(input("Enter your Answer:"))
        if sol == "Network Maintenance":
            print("correct answer")
        else:
            print("wrong answer")

        print(
            "Question 2:Which of the following is based on Multi Valued Dependency?"
        )
        print("\n1.Seconth \t2.Fourth \t3.Third \t4.Sixth")
        sol2 = str(input("Enter your answer:"))
        if sol2 == "Fourth":
            print("correct answer")
        else:
            print("wrong answer")
        print(
            "Question 3:In order to use a DBMS, it is important to understand")
        print("\n1.Physical schema \t2. All subschemas \t3.One subschema \t4.Both 1 and 2")
        sol3 = str(input("Enter your Answer: -"))
        if sol3 == "One subschema":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 4:In SQL, which command(s) is(are) used to redefine an index's future storage allocation"
        )
        print("\n1.ALTER INDEX \t2.REDEFINE INDEX \t3.MODIFY INDEX \t4.DO INDEX")
        sol4 = str(input("Enter your answer: -"))
        if sol4 == "ALTER INDEX":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 5: _________ refers to the correctness and completeness of the data in a database?"
        )
        print("\n1.Data security \t2.Data integrity \t3.Data constraint \t4.Data independence")
        sol5 = str(input("Enter your answer: -"))
        if sol5 == "Data integrity":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 6:What name is given to the collection of facts, items of information or data which are related in some way?"
        )
        print("\n1.Database \t2. Directory information \t3. Information tree \t4. Information provider")
        sol6 = str(input("Enter your answer: -"))
        if sol6 == "Database":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 7:Which command is used to remove a table from the database in SQL?"
        )
        print("\n1.1920 \t2.1940 \t3.1030 \t4.1925")
        sol7 = str(input("Enter your answer: -"))
        if sol7 == "1930":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 8:The register AX is formed by grouping_______")
        sol8 = str(input("Enter your answer: -"))
        print("\n1.ALTER TABLE \t2.MODIFY TABLE \t3.UPDATE TABLE \t4.DROP TABLE")
        if sol8 == "DROP TABLE":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 9:A Database Management System (DBMS) is")
        sol9 = str(input("Enter your answer: -"))
        if sol9 == "Collection of interrelated data":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 10:Which of the following represents a relationship among a set of values?"
        )
        print("\n1.A Row \t2.A Column \t3.A Table \t4.A Table")
        sol10 = str(input("Enter your Answer: -"))
        if sol10 == " A Row":
            print("correct answer!")
        else:
            print("wrong answer")
        playagain = input("would you like to play again:Yes or No: -")
        if playagain == "yes":
            print(bio())
        else:
            print("Thanks for playing the quiz Goodbye!")
            break


def Operating_System():
    while True:
        print("Answer the following Questions ")
        print("Question 1:When was the first operating system developed?")
        print("\n1.1945 \t2.1950 \t3.1949 \t4.1947")
        sol = str(input("Enter your Answer:"))
        if sol == "1950":
            print("correct answer")
        else:
            print("wrong answer")

        print("Question 2:Banker's algorithm is used?")
        sol2 = str(input("Enter your answer:"))
        if sol2 == "To prevent deadlock":
            print("correct answer")
        else:
            print("wrong answer")
        print(
            "Question 3:Which of the following is a single-user operating system?"
        )
        print("\n1.Window \t2.Ms-Dos \t3.MAC \t4.None of the above")
        sol3 = str(input("Enter your Answer: -"))
        if sol3 == "Ms-Dos":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 4:Who provides the interface to access the services of the operating system?"
        )
        print("\n1.System call \t2.API \t3.Libaray \t4. Assembly instructions")
        sol4 = str(input("Enter your answer: -"))
        if sol4 == "System call":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 5:Where are placed the list of processes that are prepared to be executed and waiting?"
        )
        print("\n1.Job queue \t2.Ready queue \t3.Execution queue \t4.Process queue")
        sol5 = str(input("Enter your answer: -"))
        if sol5 == "Ready queue":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 6:What type of scheduling is round-robin scheduling?")
        print("\n1.Linear data scheduling \t2.Non-linear data scheduling \t3.Preemptive scheduling \t4.Non-preemptive scheduling")
        sol6 = str(input("Enter your answer: -"))
        if sol6 == "Preemptive scheduling":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 7:What type of memory stores data in a swap file on a hard drive?"
        )
        print("\n1.Secondary memory \t2.Virtual memory \t3.Low memory \t4.RAM")
        sol7 = str(input("Enter your answer: -"))
        if sol7 == "Virtual memory":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 8:Which of the following semaphore can take the non-negative integer values?"
        )
        print("\n1.Binary Semaphore \t2.Counting Semaphore \t3.Real Semaphore \t4.All of the these")
        sol8 = str(input("Enter your answer: -"))
        if sol8 == "Counting Semaphore":
            print("correct answer!")
        else:
            print("wrong answer")
        print("Question 9:What is the paging in the operating system?")
        sol9 = str(input("Enter your answer: -"))
        if sol9 == "Memory management scheme":
            print("correct answer!")
        else:
            print("wrong answer")
        print(
            "Question 10:Which of the following scheduling reduces process flow time?"
        )
        print("\n1.FCFS \t2.SJF \t3.LIFO \t4.All the above")
        sol10 = str(input("Enter your Answer: -"))
        if sol10 == "SJF":
            print("correct answer!")
        else:
            print("wrong answer")
        playagain = input("would you like to play again:Yes or No: -")
        if playagain == "yes":
            print(bio())
        else:
            print("Thanks for playing the quiz Goodbye!")
            break
bio()
