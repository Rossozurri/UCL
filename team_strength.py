import random
import pymysql

conn=pymysql.connect(user="root",password="inter",host="localhost",database="ucl")
cursor=conn.cursor()

q='select name from teams'
cursor.execute(q)
x=cursor.fetchall()
teams=[]
for i in x:
    for j in i:
        teams.append(j)

q='select strength from teams'
cursor.execute(q)
x=cursor.fetchall()
STRENGTH=[]
for i in x:
    for j in i:
        STRENGTH.append(j)


def team_strength(t_1,t_2):
    
    for i in range(32):
        if t_1==teams[i]:
            a=STRENGTH[i]

    for j in range(32):
        if t_2==teams[j]:
            b=STRENGTH[j]

    z=random.randrange(0,8)
    y=[t_1,t_2]
    if z==0:
        print(t_1,":0","    ",t_2,":0")
        return 0,0
    else:
        x=random.choices(y,weights=[a,b],k=z)
        print(t_1,":",x.count(t_1),"    ",t_2,":",x.count(t_2))
        return x.count(t_1), x.count(t_2)

def pen(t_1,t_2):

    for i in range(32):
        if t_1==teams[i]:
            a=STRENGTH[i]
    
    for j in range(32):
        if t_2==teams[j]:
            b=STRENGTH[j]

    team_1=[]
    team_2=[]
    
    for l in range(5):
        x=random.choices([True,False],weights=[a,b],k=2)
        team_1.append(x[0])
        team_2.append(x[1])

    
    score_1=0
    score_2=0

    for m in range(5):
        if team_1[m]:
            score_1+=1
        if team_2[m]:
            score_2+=1

    if score_1>score_2:
        print(f"{t_1}:- ",end='')

        for i in team_1:
            if i:
                if team_1.index(i)!=len(team_1):
                    print("*",end='  ')
                if team_1.index(i)==len(team_1):
                    print("*")
            else:
                if team_1.index(i)!=len(team_1):
                    print(".",end='  ')
                if team_1.index(i)==len(team_1):
                    print(".")
        print()
        
        print(f"{t_2}:- ",end='')
        
        for i in team_2:
            if i:
                if team_2.index(i)!=len(team_2):
                    print("*",end='  ')
                if team_2.index(i)==len(team_2):
                    print("*")
            else:
                if team_2.index(i)!=len(team_2):
                    print(".",end='  ')
                if team_2.index(i)==len(team_2):
                    print(".")
        print() 
        print("------------------------------------------------------")
        
        return t_1
    
    elif score_1==score_2:
        x=random.choices([True,False],weights=[a,b],k=2)
        team_1.append(x[0])
        team_2.append(x[1])
        while x[0]==x[1]:
            x=random.choices([True,False],weights=[a,b],k=2)
            team_1.append(x[0])
            team_2.append(x[1])
            
        if x[0]:
            print(f"{t_1}:- ",end='')
    
            for i in team_1:
                if i:
                    if team_1.index(i)!=len(team_1):
                        print("*",end='  ')
                    if team_1.index(i)==len(team_1):
                        print("*")
                else:
                    if team_1.index(i)!=len(team_1):
                        print(".",end='  ')
                    if team_1.index(i)==len(team_1):
                        print(".")
            print()
            
            print(f"{t_2}:- ",end='')
            
            for i in team_2:
                if i:
                    if team_2.index(i)!=len(team_2):
                        print("*",end='  ')
                    if team_2.index(i)==len(team_2):
                        print("*")
                else:
                    if team_2.index(i)!=len(team_2):
                        print(".",end='  ')
                    if team_2.index(i)==len(team_2):
                        print(".")
            print()
            print("------------------------------------------------------")
            
            return t_1
        
        if x[1]:
            print(f"{t_1}:- ",end='')
    
            for i in team_1:
                if i:
                    if team_1.index(i)!=len(team_1):
                        print("*",end='  ')
                    if team_1.index(i)==len(team_1):
                        print("*")
                else:
                    if team_1.index(i)!=len(team_1):
                        print(".",end='  ')
                    if team_1.index(i)==len(team_1):
                        print(".")
            print()
            
            print(f"{t_2}:- ",end='')
            
            for i in team_2:
                if i:
                    if team_2.index(i)!=len(team_2):
                        print("*",end='  ')
                    if team_2.index(i)==len(team_2):
                        print("*")
                else:
                    if team_2.index(i)!=len(team_2):
                        print(".",end='  ')
                    if team_2.index(i)==len(team_2):
                        print(".")
            print()
            print("------------------------------------------------------")
            return t_2
        
    else:
        print(f"{t_1}:- ",end='')
    
        for i in team_1:
            if i:
                if team_1.index(i)!=len(team_1):
                    print("*",end='  ')
                if team_1.index(i)==len(team_1):
                    print("*")
            else:
                if team_1.index(i)!=len(team_1):
                    print(".",end='  ')
                if team_1.index(i)==len(team_1):
                    print(".")
        print()
        print(f"{t_2}:- ",end='')
        
        for i in team_2:
            if i:
                if team_2.index(i)!=len(team_2):
                    print("*",end='  ')
                if team_2.index(i)==len(team_2):
                    print("*")
            else:
                if team_2.index(i)!=len(team_2):
                    print(".",end='  ')
                if team_2.index(i)==len(team_2):
                    print(".")
        print()
        print("------------------------------------------------------")
        
        return t_2


conn.close()
    
if __name__ == "__main__":
    team_strength()
if __name__ == "__main__":
    pen()
