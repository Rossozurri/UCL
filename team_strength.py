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
    
    
    if t_1==teams[0]:
        a=STRENGTH[1]
    if t_1==teams[1]:
        a=STRENGTH[2]
    if t_1==teams[2]:
        a=STRENGTH[3]
    if t_1==teams[3]:
        a=STRENGTH[3]
    if t_1==teams[4]:
        a=STRENGTH[4]
    if t_1==teams[5]:
        a=STRENGTH[5]
    if t_1==teams[6]:
        a=STRENGTH[6]
    if t_1==teams[7]:
        a=STRENGTH[7]
    if t_1==teams[8]:
        a=STRENGTH[8]
    if t_1==teams[9]:
        a=STRENGTH[9]
    if t_1==teams[10]:
        a=STRENGTH[10]
    if t_1==teams[11]:
        a=STRENGTH[11]
    if t_1==teams[12]:
        a=STRENGTH[12]
    if t_1==teams[13]:
        a=STRENGTH[13]
    if t_1==teams[14]:
        a=STRENGTH[14]
    if t_1==teams[15]:
        a=STRENGTH[15]
    if t_1==teams[16]:
        a=STRENGTH[16]
    if t_1==teams[17]:
        a=STRENGTH[17]
    if t_1==teams[18]:
        a=STRENGTH[18]
    if t_1==teams[19]:
        a=STRENGTH[19]
    if t_1==teams[20]:
        a=STRENGTH[20]
    if t_1==teams[21]:
        a=STRENGTH[21]
    if t_1==teams[22]:
        a=STRENGTH[22]
    if t_1==teams[23]:
        a=STRENGTH[23]
    if t_1==teams[24]:
        a=STRENGTH[24]
    if t_1==teams[25]:
        a=STRENGTH[25]
    if t_1==teams[26]:
        a=STRENGTH[26]
    if t_1==teams[27]:
        a=STRENGTH[27]
    if t_1==teams[28]:
        a=STRENGTH[28]
    if t_1==teams[29]:
        a=STRENGTH[29]
    if t_1==teams[30]:
        a=STRENGTH[30]
    if t_1==teams[31]:
        a=STRENGTH[31]

    if t_2==teams[0]:
        b=STRENGTH[1]
    if t_2==teams[1]:
        b=STRENGTH[2]
    if t_2==teams[2]:
        b=STRENGTH[3]
    if t_2==teams[3]:
        b=STRENGTH[3]
    if t_2==teams[4]:
        b=STRENGTH[4]
    if t_2==teams[5]:
        b=STRENGTH[5]
    if t_2==teams[6]:
        b=STRENGTH[6]
    if t_2==teams[7]:
        b=STRENGTH[7]
    if t_2==teams[8]:
        b=STRENGTH[8]
    if t_2==teams[9]:
        b=STRENGTH[9]
    if t_2==teams[10]:
        b=STRENGTH[10]
    if t_2==teams[11]:
        b=STRENGTH[11]
    if t_2==teams[12]:
        b=STRENGTH[12]
    if t_2==teams[13]:
        b=STRENGTH[13]
    if t_2==teams[14]:
        b=STRENGTH[14]
    if t_2==teams[15]:
        b=STRENGTH[15]
    if t_2==teams[16]:
        b=STRENGTH[16]
    if t_2==teams[17]:
        b=STRENGTH[17]
    if t_2==teams[18]:
        b=STRENGTH[18]
    if t_2==teams[19]:
        b=STRENGTH[19]
    if t_2==teams[20]:
        b=STRENGTH[20]
    if t_2==teams[21]:
        b=STRENGTH[21]
    if t_2==teams[22]:
        b=STRENGTH[22]
    if t_2==teams[23]:
        b=STRENGTH[23]
    if t_2==teams[24]:
        b=STRENGTH[24]
    if t_2==teams[25]:
        b=STRENGTH[25]
    if t_2==teams[26]:
        b=STRENGTH[26]
    if t_2==teams[27]:
        b=STRENGTH[27]
    if t_2==teams[28]:
        b=STRENGTH[28]
    if t_2==teams[29]:
        b=STRENGTH[29]
    if t_2==teams[30]:
        b=STRENGTH[30]
    if t_2==teams[31]:
        b=STRENGTH[31]

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
    
    if t_1==teams[0]:
        a=STRENGTH[1]
    if t_1==teams[1]:
        a=STRENGTH[2]
    if t_1==teams[2]:
        a=STRENGTH[3]
    if t_1==teams[3]:
        a=STRENGTH[3]
    if t_1==teams[4]:
        a=STRENGTH[4]
    if t_1==teams[5]:
        a=STRENGTH[5]
    if t_1==teams[6]:
        a=STRENGTH[6]
    if t_1==teams[7]:
        a=STRENGTH[7]
    if t_1==teams[8]:
        a=STRENGTH[8]
    if t_1==teams[9]:
        a=STRENGTH[9]
    if t_1==teams[10]:
        a=STRENGTH[10]
    if t_1==teams[11]:
        a=STRENGTH[11]
    if t_1==teams[12]:
        a=STRENGTH[12]
    if t_1==teams[13]:
        a=STRENGTH[13]
    if t_1==teams[14]:
        a=STRENGTH[14]
    if t_1==teams[15]:
        a=STRENGTH[15]
    if t_1==teams[16]:
        a=STRENGTH[16]
    if t_1==teams[17]:
        a=STRENGTH[17]
    if t_1==teams[18]:
        a=STRENGTH[18]
    if t_1==teams[19]:
        a=STRENGTH[19]
    if t_1==teams[20]:
        a=STRENGTH[20]
    if t_1==teams[21]:
        a=STRENGTH[21]
    if t_1==teams[22]:
        a=STRENGTH[22]
    if t_1==teams[23]:
        a=STRENGTH[23]
    if t_1==teams[24]:
        a=STRENGTH[24]
    if t_1==teams[25]:
        a=STRENGTH[25]
    if t_1==teams[26]:
        a=STRENGTH[26]
    if t_1==teams[27]:
        a=STRENGTH[27]
    if t_1==teams[28]:
        a=STRENGTH[28]
    if t_1==teams[29]:
        a=STRENGTH[29]
    if t_1==teams[30]:
        a=STRENGTH[30]
    if t_1==teams[31]:
        a=STRENGTH[31]

    if t_2==teams[0]:
        b=STRENGTH[1]
    if t_2==teams[1]:
        b=STRENGTH[2]
    if t_2==teams[2]:
        b=STRENGTH[3]
    if t_2==teams[3]:
        b=STRENGTH[3]
    if t_2==teams[4]:
        b=STRENGTH[4]
    if t_2==teams[5]:
        b=STRENGTH[5]
    if t_2==teams[6]:
        b=STRENGTH[6]
    if t_2==teams[7]:
        b=STRENGTH[7]
    if t_2==teams[8]:
        b=STRENGTH[8]
    if t_2==teams[9]:
        b=STRENGTH[9]
    if t_2==teams[10]:
        b=STRENGTH[10]
    if t_2==teams[11]:
        b=STRENGTH[11]
    if t_2==teams[12]:
        b=STRENGTH[12]
    if t_2==teams[13]:
        b=STRENGTH[13]
    if t_2==teams[14]:
        b=STRENGTH[14]
    if t_2==teams[15]:
        b=STRENGTH[15]
    if t_2==teams[16]:
        b=STRENGTH[16]
    if t_2==teams[17]:
        b=STRENGTH[17]
    if t_2==teams[18]:
        b=STRENGTH[18]
    if t_2==teams[19]:
        b=STRENGTH[19]
    if t_2==teams[20]:
        b=STRENGTH[20]
    if t_2==teams[21]:
        b=STRENGTH[21]
    if t_2==teams[22]:
        b=STRENGTH[22]
    if t_2==teams[23]:
        b=STRENGTH[23]
    if t_2==teams[24]:
        b=STRENGTH[24]
    if t_2==teams[25]:
        b=STRENGTH[25]
    if t_2==teams[26]:
        b=STRENGTH[26]
    if t_2==teams[27]:
        b=STRENGTH[27]
    if t_2==teams[28]:
        b=STRENGTH[28]
    if t_2==teams[29]:
        b=STRENGTH[29]
    if t_2==teams[30]:
        b=STRENGTH[30]
    if t_2==teams[31]:
        b=STRENGTH[31]

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
