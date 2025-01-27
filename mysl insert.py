import pymysql
import random
conn=pymysql.connect(user="root",password="inter",host="localhost",database="ucl")
cursor=conn.cursor()
team=["Bayern","Copenhagen","Galatasaray","Man United","Arsenal","PSV","Lens","Sevilla","Real Madrid","Napoli",
      "Braga","Union Berlin","Real Sociedad","Inter","Benfica","RB Salzburg","Atlético Madrid","Lazio","Feyenoord",
      "Celtic","Dortmund","PSG","Milan","Newcastle","Man City","RB Leipzig","Young Boys","Crvena zvezda","Barcelona",
      "Porto","Shakhtar","Antwerp"]
stregnth=[random.uniform(87,92),random.uniform(56,61),random.uniform(65,70),random.uniform(73,78),
          random.uniform(83,88),random.uniform(65,70),random.uniform(62,67),random.uniform(73,78),
          random.uniform(92,97),random.uniform(76,81),random.uniform(54,59),random.uniform(56,61),
          random.uniform(79,84),random.uniform(91,96),random.uniform(71,76),random.uniform(70,75),
          random.uniform(84,89),random.uniform(74,79),random.uniform(41,46),random.uniform(58,63),
          random.uniform(80,85),random.uniform(84,89),random.uniform(85,90),random.uniform(75,80),
          random.uniform(89,94),random.uniform(73,78),random.uniform(61,67),random.uniform(35,40),
          random.uniform(80,85),random.uniform(71,76),random.uniform(56,61),random.uniform(44,49)]
for i in range(32):
    l=[team[i],stregnth[i]]
    query="insert into teams values(%s,%s)"
    cursor.execute(query,l)
    conn.commit()
conn.close()
