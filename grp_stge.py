import random
from team_strength import team_strength

def group_stage(MAIN):
        random.shuffle(MAIN)
        MAIN_group=[]
        group_1 = []
        for i in range(4):
                group_1.append(MAIN[i])
        group_2 = []
        for i in range(4,8):
                group_2.append(MAIN[i])
        group_3 = []
        for i in range(8,12):
                group_3.append(MAIN[i])
        group_4 = []
        for i in range(12,16):
                group_4.append(MAIN[i])
        group_5 = []
        for i in range(16,20):
                group_5.append(MAIN[i])
        group_6 = []
        for i in range(20,24):
                group_6.append(MAIN[i])
        group_7 = []
        for i in range(24,28):
                group_7.append(MAIN[i])
        group_8 = []
        for i in range(28,32):
                group_8.append(MAIN[i])

        print("The Groups Are:- ")
        print()
        print("Group A:- ",group_1)
        print("Group B:- ",group_2)
        print("Group C:- ",group_3)
        print("Group D:- ",group_4)
        print("Group E:- ",group_5)
        print("Group F:- ",group_6)
        print("Group G:- ",group_7)
        print("Group H:- ",group_8)
        print()

        MAIN_group.append(group_1)
        MAIN_group.append(group_2)
        MAIN_group.append(group_3)
        MAIN_group.append(group_4)
        MAIN_group.append(group_5)
        MAIN_group.append(group_6)
        MAIN_group.append(group_7)
        MAIN_group.append(group_8)

        ro16=[]
        
        for i in MAIN_group:
                grp_t_1=[]
                grp_t_2=[]
                grp_t_3=[]
                grp_t_4=[]
                t_1_point=0
                t_2_point=0
                t_3_point=0
                t_4_point=0
                gd_1=0
                gd_2=0
                gd_3=0
                gd_4=0
                for x in range(2):
                        for j in range(4):
                                for k in range(j+1,4):
                                        p,q=team_strength(i[j],i[k])
                                        if p>q:
                                            if j==0:
                                                t_1_point+=3
                                                gd_1+=p-q
                                            if j==1:
                                                t_2_point+=3
                                                gd_2+=p-q
                                            if j==2:
                                                t_3_point+=3
                                                gd_3+=p-q
                                            if j==3:
                                                t_4_point+=3
                                                gd_4+=p-q

                                            if k==0:
                                                gd_1+=q-p
                                            if k==1:
                                                gd_2+=q-p
                                            if k==2:
                                                gd_3+=q-p
                                            if k==3:
                                                gd_4+=q-p
                                                
                                        elif p<q:
                                            if k==0:
                                                t_1_point+=3
                                                gd_1+=q-p
                                            if k==1:
                                                t_2_point+=3
                                                gd_2+=q-p
                                            if k==2:
                                                t_3_point+=3
                                                gd_3=q-p
                                            if k==3:
                                                t_4_point+=3
                                                gd_4=q-p

                                            if j==0:
                                                gd_1+=p-q
                                            if j==1:
                                                gd_2+=p-q
                                            if j==2:
                                                gd_3+=p-q
                                            if j==3:
                                                gd_4+=p-q
                                            
                                        else:
                                                if j==0:
                                                    t_1_point+=1
                                                if j==1:
                                                    t_2_point+=1
                                                if j==2:
                                                    t_3_point+=1
                                                if j==3:
                                                    t_4_point+=1
                                                if k==0:
                                                    t_1_point+=1
                                                if k==1:
                                                    t_2_point+=1
                                                if k==2:
                                                    t_3_point+=1
                                                if k==3:
                                                    t_4_point+=1

                print('\n')
                mx=[]
                tp=[t_1_point,t_2_point,t_3_point,t_4_point]
                g=[gd_1,gd_2,gd_3,gd_4]
                tp.sort(reverse=True)
                for k in range(4):
                        dumy=[]
                        dumy.extend(tp)
                        dumy.remove(tp[k])
                        if tp[k] in dumy:
                                for u in range(k+1,4):
                                        if tp[k]==tp[u]:
                                                if tp[k]==t_1_point:
                                                        if tp[u]==t_2_point:
                                                                if gd_1>=gd_2:
                                                                        mx.append(i[0])
                                                                        print(f'{i[0]:^16} points:={t_1_point:^6} gol diff:={gd_1:^6}')
                                                                        mx.append(i[1])
                                                                        print(f'{i[1]:^16} points:={t_2_point:^6} gol diff:={gd_2:^6}')
                                                                else:
                                                                        mx.append(i[1])
                                                                        print(f'{i[1]:^16} points:={t_2_point:^6} gol diff:={gd_2:^6}')
                                                                        mx.append(i[0])
                                                                        print(f'{i[0]:^16} points:={t_1_point:^6} gol diff:={gd_1:^6}')
                                                        if tp[u]==t_3_point:
                                                                if gd_1>=gd_3:
                                                                        mx.append(i[0])
                                                                        print(f'{i[0]:^16} points:={t_1_point:^6} gol diff:={gd_1:^6}')
                                                                        mx.append(i[2])
                                                                        print(f'{i[2]:^16} points:={t_3_point:^6} gol diff:={gd_3:^6}')
                                                                else:
                                                                        mx.append(i[2])
                                                                        print(f'{i[2]:^16} points:={t_3_point:^6} gol diff:={gd_3:^6}')
                                                                        mx.append(i[0])
                                                                        print(f'{i[0]:^16} points:={t_1_point:^6} gol diff:={gd_1:^6}')
                                                        if tp[u]==t_4_point:
                                                                if gd_1>=gd_4:
                                                                        mx.append(i[0])
                                                                        print(f'{i[0]:^16} points:={t_1_point:^6} gol diff:={gd_1:^6}')
                                                                        mx.append(i[3])
                                                                        print(f'{i[3]:^16} points:={t_4_point:^6} gol diff:={gd_4:^6}')
                                                                else:
                                                                        mx.append(i[3])
                                                                        print(f'{i[3]:^16} points:={t_4_point:^6} gol diff:={gd_4:^6}')
                                                                        mx.append(i[0])
                                                                        print(f'{i[0]:^16} points:={t_1_point:^6} gol diff:={gd_1:^6}')
                                                if tp[k]==t_2_point:
                                                        if tp[u]==t_3_point:
                                                                if gd_2>=gd_3:
                                                                        mx.append(i[1])
                                                                        print(f'{i[1]:^16} points:={t_2_point:^6} gol diff:={gd_2:^6}')
                                                                        mx.append(i[2])
                                                                        print(f'{i[2]:^16} points:={t_3_point:^6} gol diff:={gd_3:^6}')
                                                                else:
                                                                        mx.append(i[2])
                                                                        print(f'{i[2]:^16} points:={t_3_point:^6} gol diff:={gd_3:^6}')
                                                                        mx.append(i[1])
                                                                        print(f'{i[1]:^16} points:={t_2_point:^6} gol diff:={gd_2:^6}')
                                                        if tp[u]==t_4_point:
                                                                if gd_2>=gd_4:
                                                                        mx.append(i[1])
                                                                        print(f'{i[1]:^16} points:={t_2_point:^6} gol diff:={gd_2:^6}')
                                                                        mx.append(i[3])
                                                                        print(f'{i[3]:^16} points:={t_4_point:^6} gol diff:={gd_4:^6}')
                                                                else:
                                                                        mx.append(i[3])
                                                                        print(f'{i[3]:^16} points:={t_4_point:^6} gol diff:={gd_4:^6}')
                                                                        mx.append(i[1])
                                                                        print(f'{i[1]:^16} points:={t_2_point:^6} gol diff:={gd_2:^6}')
                                                                        
                                                if tp[k]==t_3_point:
                                                        if tp[u]==t_4_point:
                                                                if gd_3>=gd_4:
                                                                        mx.append(i[2])
                                                                        print(f'{i[2]:^16} points:={t_3_point:^6} gol diff:={gd_3:^6}')
                                                                        mx.append(i[3])
                                                                        print(f'{i[3]:^16} points:={t_4_point:^6} gol diff:={gd_4:^6}')
                                                                else:
                                                                        mx.append(i[3])
                                                                        print(f'{i[3]:^16} points:={t_4_point:^6} gol diff:={gd_4:^6}')
                                                                        mx.append(i[2])
                                                                        print(f'{i[2]:^16} points:={t_3_point:^6} gol diff:={gd_3:^6}')
                                                
                        if tp[k] not in dumy:
                                if tp[k]==t_1_point:
                                        mx.append(i[0])
                                        print(f'{i[0]:^16} points:={t_1_point:^6} gol diff:={gd_1:^6}')
                                if tp[k]==t_2_point:
                                        mx.append(i[1])
                                        print(f'{i[1]:^16} points:={t_2_point:^6} gol diff:={gd_2:^6}')
                                if tp[k]==t_3_point:
                                        mx.append(i[2])
                                        print(f'{i[2]:^16} points:={t_3_point:^6} gol diff:={gd_3:^6}')
                                if tp[k]==t_4_point:
                                        mx.append(i[3])
                                        print(f'{i[3]:^16} points:={t_4_point:^6} gol diff:={gd_4:^6}')

                print("\n")
                ro16.append(mx[0])
                ro16.append(mx[1])
        return ro16
                

if __name__ == "__main__":
        group_stage()
