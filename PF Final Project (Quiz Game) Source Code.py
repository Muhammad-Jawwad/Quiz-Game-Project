#  بِسمِ اللہِ الرَّحمٰنِ الرَّحِيم
def info(name,roll_number,depart):
    with open("info.txt","a") as f:
        f.write(f"\nName: {name}\n Roll Number: {roll_number}\n Department: {depart}")
        
    
'''______________________________________________________________________________________________________________________________'''
def round1():
    print("ROUND-1")
    round1.add1_total = 100
    round1.add1=0
    with open("r1.txt","r") as f :
        with open("w1.txt","r") as w:
            a=w.readlines()
            for i in range (10):
                for j in range(6):
                    print(f.readline())
                n=input("Enter your answer[a/b/c/d]:\n")
                if n in a[i]:
                    print("Your answer is correct")
                    round1.add1+=10
                else:
                    print("Your answer is incorrect")
    print("You have passed the Round 1.")
    print("Your total round-1 score: ",round1.add1)

'''______________________________________________________________________________________________________________________________'''
def round2():
    print("ROUND-2")
    round2.add2_total = 100
    round2.add2=0
    with open("r2.txt","r") as f :
        with open("w2.txt","r") as w:
            a=w.readlines()
            for i in range (5):
                for j in range(6):
                    print(f.readline())
                n=input("Enter your answer[a/b/c/d]:\n")
                if n in a[i]:
                    print("Your answer is correct")
                    round2.add2+=20
                else:
                    print("Your answer is incorrect")
    print("You have passed the Round 2.")
    print("Your Total Round-2 score: ",round2.add2)
'''______________________________________________________________________________________________________________________________'''
def round3():
    print("ROUND-3")
    round3.add3_total = 150
    round3.add3=0
    with open("r3.txt","r") as f :
        with open("w3.txt","r") as w:
            a=w.readlines()
            for i in range (3):
                for j in range(6):
                    print(f.readline())
                n=input("Enter your answer[a/b/c/d]:\n")
                if n in a[i]:
                    print("Your answer is correct")
                    round3.add3+=50
                else:
                    print("Your answer is incorrect")
    print("Your Total Round-3 score: ",round3.add3)
    
'''______________________________________________________________________________________________________________________________'''
def result():
    with open("info.txt","r") as f:
        print(f.readline())
        
'''______________________________________________________________________________________________________________________________'''

def score():
    program.final_score = round1.add1+round2.add2+round3.add3
    print("NAME:",program.name)
    print("ROLL # ",program.roll_number)
    print("DEPARTMENT:",program.depart)
    print("Your final score is ",program.final_score)
    
'''______________________________________________________________________________________________________________________________'''

def program():
    print("------Welcome to Quiz Game------")
    a = input("Are you ready to play? [Yes/No]:\n")
    if a.lower() == "yes":
        print('''RULES:\n1.There will be total Three rounds .\n2.ROUND 1 wil have 5 questions . if you get more then --%  You will be promoted to round 2\n3.Round 2 will have three questions.\n4.If you get more then --%  in round 2 you will be promoted to round 3\n5.In Round 3, If you given all 3 answers correct you will get your Final score, else you will be disqualified in the final round.''')
        print("Enter your information")
        program.name = input("Enter your name:\n")
        program.roll_number = input("Enter your roll number:\n")
        program.depart = input("Enter your department:\n")
        info(program.name,program.roll_number,program.depart)
        print("Let's start!")
        round1()
        l=input("press ENTER to continue:\n")
        if ((round1.add1/round1.add1_total)*100)>=70:
            round2()
            l=input("press ENTER to continue:\n")
             
            if ((round2.add2/round2.add2_total)*100)>=80:
                round3()
                if round3.add3 >= round3.add3_total:
                    print("Congratulation! :-)")
                    b = input("Press 'ENTER' to see your final score:\n")
                    
                    score()
                else:
                    print("Oops! You Are Disqualified. Better Luck Next Time :( ")
            else:
                    print("Oops! You Are Disqualified. Better Luck Next Time :( ")
        else:
                print("Oops! You Are Disqualified. Better Luck Next Time :( ")
    else:
        print(" Bye Bye! ")
              
'''______________________________________________________________________________________________________________________________'''
# now calling the whole program here!
print(program())
print("ALLAH HAFIZ")