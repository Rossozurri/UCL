import random
from team_strength import team_strength,pen

def qtr_fnl(QLFD):
    random.shuffle(QLFD)
    matches=[]
    agg=[]
    qlfd_3=[]
    match_1=[]
    for i in range(2):
        match_1.append(QLFD[i])
    match_2 = []
    for i in range(2,4):
        match_2.append(QLFD[i])
    match_3 = []
    for i in range(4,6):
        match_3.append(QLFD[i])
    match_4 = []
    for i in range(6,8):
        match_4.append(QLFD[i])

    matches.append(match_1)
    matches.append(match_2)
    matches.append(match_3)
    matches.append(match_4)

    for i in matches:
        print(i)
    print()

    print("First Leg Results:- ")
    print()
    for i in matches:
        p,q=team_strength(i[1],i[0])
        agg.append([q,p])
    print()
    print(agg)
    print()
    print("Second Leg Results:- ")
    print()
    for i in matches:
        p,q=team_strength(i[0],i[1])
        agg[matches.index(i)][1]+=q
        agg[matches.index(i)][0]+=p
    print()
    print(agg)
    print()

    for x in range(4):
        if agg[x][0]>agg[x][1]:
            qlfd_3.append(matches[x][0])
        elif agg[x][0]==agg[x][1]:
            qlfd_3.append(pen(matches[x][0],matches[x][1]))
        else:
            qlfd_3.append(matches[x][1])

    return qlfd_3  


if __name__=="__main__":
    qtr_fnl()
