

question=["How many cntinents are there?","What is the capital of India?","Navgurukul me kon sa cource pdaya jata hai?"]
option=[["Four","Nine","Seven","eight"],["chandigarh","Bhopal","Chennai","Delhi"],["Software Engineer","Counseling","Tourism","Agricuture"]]
life_line=[["Four","Seven"],["Bhopal","Delhi"],["Software","Counseling"]]

solution1=[3,4,1]
solution2=[2,2,1]

c=0
def life_line5050(i):
        c=0:
        k=0
        if c==0:
            while k<len(life_line[i]):
                print(k+1,life_line[i][k])
                k=k+1
            num=int(input("enter the ans: "))
            c=c+1
            if user==solution2[i]:
            return(True,"you are right")
        else:
            return(False,"wrong answer")
    
    else:
        print("you already use life line 5050")
        num1=int(input("enter the answer: "))
        if num1==solution2[i]:
            return("your answer is right")
        else:
            return("you answer is wrong")

def option(i):
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j=j+1
    user=int(input("enter the answer: "))
    if user==solution1[i]:
        print("you are right")
    if user==5050:
        return(life_line(i))
    else:
        return False

def main_KBC():
    i=0
    while i<len(question):
        print("Q.",i+1,question[i])
        print(option(i))
        i=i+1
main_KBC()
        









        
