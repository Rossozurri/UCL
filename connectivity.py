import pymysql
import time

conn=pymysql.connect(user="root",password="inter",host="localhost",database="ucl")
cursor=conn.cursor()

def LIST_MAIN():
    q='select name from teams'
    cursor.execute(q)
    x=cursor.fetchall()
    MAIN=[]
    for i in x:
        for j in i:
            MAIN.append(j)
    return MAIN
        


def LIST_STRENGTH():
    q='select strength from teams'
    cursor.execute(q)
    x=cursor.fetchall()
    STRENGTH=[]
    for i in x:
        for j in i:
            STRENGTH.append(j)
    return STRENGTH

conn.close()

