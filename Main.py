from grp_stge import group_stage
from team_strength import team_strength,pen
from round_of_16 import rnd_of_16
from quater_finals import qtr_fnl
from semi_final import sm_fnl
import random
import pymysql

##MAIN=["Bayern","Copenhagen","Galatasaray","Man United","Arsenal","PSV","Lens","Sevilla","Real Madrid","Napoli","Braga","Union Berlin",
##       "Real Sociedad","Inter","Benfica","RB Salzburg","Atlético Madrid","Lazio","Feyenoord","Celtic","Dortmund","PSG","Milan","Newcastle",
##       "Man City","RB Leipzig","Young Boys","Crvena zvezda","Barcelona","Porto","Shakhtar","Antwerp"]

conn=pymysql.connect(user="root",password="inter",host="localhost",database="ucl")
cursor=conn.cursor()

q='select name from teams'
cursor.execute(q)
x=cursor.fetchall()
MAIN=[]
for i in x:
    for j in i:
        MAIN.append(j)

conn.close()

ch='Y'
stage=0


while ch.upper()=="Y":
    if stage==0:
        print()
        print("Group stage:- \n")
        qlfd=group_stage(MAIN)
        print()
    elif stage==1:
        print()
        print("Round of 16:- \n")
        qlfd=rnd_of_16(qlfd)
        print()
    elif stage==2:
        print()
        print("Quater finals:- \n")
        qlfd=qtr_fnl(qlfd)
        print()
    elif stage==3:
        print()
        print("Semi finals:- \n")
        qlfd=sm_fnl(qlfd)
        print()
    elif stage==4:
        print()
        print("Final:- \n")
        random.shuffle(qlfd)
        p,q=team_strength(qlfd[0],qlfd[1])
        if p>q:
            print(f"The Champions are :- {qlfd[0]}")
        elif q>p:
            print(f"The Champions are :- {qlfd[1]}")
        else:
            print("the champions are :-",pen(qlfd[0],qlfd[1]))
        print()
    elif stage==5:
        ch=input("Do you want to replay the simulation(Y/N):-")
        if ch.upper()=='Y':
            stage=-1
    stage+=1
