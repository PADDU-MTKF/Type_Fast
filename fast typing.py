
# MADE BY PRADYUMNA


import time as t
import random as r
import os,sys
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import threading



len_pno=pno=cursor=mydb=None


def helpme():

    help_line='''
This program will help you improve your typing speed

1) Each dificulty contains multiple levels
2) Each Level has different Chalenges
3) You can move to next Level only if you clear previous one
4) After selecting Level there will be character displaied at the
    bottom and your task is to type the same in your keyboard
5) The character will change at a perticular interval of time
    according to your dificulty
6) NOTE that interchanging capital and small letters will effect
    your score
7) All Levels of all dificulty are similar,only time changes
8) As another character appeares continue typing it
9) After the last character of that Level,You will get your result'''
    messagebox.showinfo('HELP',help_line)



def select_option(f=1):

    def home_page():
        def level_page(difi,cust=None):


            def lev(time):

                def Back():
                    lev.grid_forget()
                    info_lev.place_forget()
                    l1.place_forget()
                    l2.place_forget()
                    l3.place_forget()
                    l4.place_forget()
                    l5.place_forget()
                    l6.place_forget()
                    l7.place_forget()
                    back.place_forget()
                    home_page()

                def task(l):
                    global pno,mydb,cursor

                    def start(ln):
                        def result(you,pc,flag=0):
                            def see():
                                def next__():
                                    result_title.grid_forget()
                                    rbox.place_forget()
                                    bck_btn.place_forget()
                                    result(you,pc,1)

                                ok_btn.place_forget()
                                side_bar.place_forget()
                                result_com.place_forget()
                                scr.place_forget()
                                see.place_forget()


                                rbox=Listbox(main,height=11,width=19,bg='LightSteelBlue2',font='Areal 10 bold')
                                bck_btn=Button(main,text=' BACK',bg='purple',fg='white',command=next__,font='Verdana 13 bold italic')

                                c="     PC            YOU"
                                rbox.insert(END,c)
                                c='   '+'-'*26
                                rbox.insert(END,c)
                                for i in range(len(pc)):
                                    c='     '+str(pc[i])+'                 '+str(you[i])
                                    rbox.insert(END,c)


                                rbox.place(x=8,y=93)
                                bck_btn.place(x=210,y=110)





                            def nxt(difi,time):
                                result_title.grid_forget()
                                ok_btn.place_forget()
                                side_bar.place_forget()
                                result_com.place_forget()
                                scr.place_forget()
                                see.place_forget()
                                level_page(difi,time)

                            game_entry.place_forget()
                            game_title.grid_forget()

                            result_title=Label(main,text='****************    RESULT   ',bg='light blue',fg='black',font='Verdana 15 bold italic')
                            ok_btn=Button(main,text='OK',bg='purple',fg='white',font='Verdana 13 bold italic',command=lambda:nxt(difi,time))
                            side_bar=Label(main,text='Y\nO\nU\nR\n \nS\nC\nO\nR\nE',fg='red',font='Verdana 15 bold italic')
                            see=Button(main,text='SEE WHAT YOU\nTYPED',bg='pink',fg='black',font='Verdana 7 bold italic',command=see)


                            s=str(len(pc))
                            if you==pc:
                                txt='PASS\n😀'
                                col='green'
                                score=s+'/'+s

                                if flag==0:
                                    DB={'2':'easy','1':'medium','0.5':'hard','0.3':'advanced'}
                                    try:
                                        cursor.execute('select '+DB[str(time)]+' from profile where pro_no='+str(pno))
                                        for i in cursor:
                                            fin=int(i[0])

                                        if ln>fin:
                                            cursor.execute('update profile set '+DB[str(time)]+'='+str(fin+1)+' where pro_no='+str(pno))
                                            mydb.commit()
                                            #print('updated')
                                        else:
                                            pass
                                    except:
                                        pass

                            else:
                                txt='FAIL\n😔'
                                col='red'
                                count=index=0
                                for i in pc:
                                    if i==you[index]:
                                        count+=1
                                    index+=1
                                score=str(count)+'/'+s

                            #print('pro no :',pno,'Level ',ln,'time=',time)



                            result_com=Label(main,text=txt,fg=col,bg='snow',font='Verdana 15 bold italic')
                            scr=Label(main,text=score,fg='black',bg='cyan3',font='Verdana 16 bold italic')


                            result_title.grid(row=0,column=1,pady=23,padx=40)
                            ok_btn.place(x=293,y=135)
                            side_bar.place(x=30,y=60)
                            result_com.place(x=210,y=255)
                            scr.place(x=190,y=93)
                            see.place(x=100,y=136)


                            #print(you,pc)
                            #print(len(pc))


                        game_title=Label(main,text='*****************    START   ',bg='light blue',fg='black',font='Verdana 15 bold italic')
                        game_title.grid(row=0,column=1,pady=23,padx=40)
                        game_entry=Entry(main,width=13,fg='blue',font='Verdana 17 italic')
                        game_entry.focus()
                        game_entry.place(x=127,y=93)

                        pc=[]
                        you=[]
                        ran=[]
                        if ln==1: #level 1
                            def do():
                                t.sleep(2)
                                for i in range(65,91):
                                    ch=chr(i)
                                    pc.append(ch)
                                    game_char=Label(main,text=ch,bg='snow',fg='red',font='Areal 40 bold')
                                    game_char.place(x=220,y=250)
                                    t.sleep(time)
                                    u=game_entry.get()
                                    you.append(u)
                                    game_entry.delete(0,END)
                                    game_char.place_forget()
                                result(you,pc)
                            try:
                                th=threading.Thread(target=do)
                                th.daemon=True
                                th.start()
                            except:
                                pass

                        elif ln==2: #level 2
                            def do():
                                t.sleep(2)
                                for i in range(90,64,-1):
                                    ch=chr(i)
                                    pc.append(ch)
                                    game_char=Label(main,text=ch,bg='snow',fg='red',font='Areal 40 bold')
                                    game_char.place(x=220,y=250)
                                    t.sleep(time)
                                    u=game_entry.get()
                                    you.append(u)
                                    game_entry.delete(0,END)
                                    game_char.place_forget()
                                result(you,pc)
                            try:
                                th=threading.Thread(target=do)
                                th.daemon=True
                                th.start()
                            except:
                                pass

                        elif ln==3: #level 3
                            for i in range(65,91):
                                    ch=chr(i)
                                    ran.append(ch)
                            def do():
                                t.sleep(2)
                                for i in range(26):
                                    ch=r.choice(ran)
                                    pc.append(ch)
                                    game_char=Label(main,text=ch,bg='snow',fg='red',font='Areal 40 bold')
                                    game_char.place(x=220,y=250)
                                    t.sleep(time)
                                    u=game_entry.get()
                                    you.append(u)
                                    game_entry.delete(0,END)
                                    game_char.place_forget()
                                    ran.remove(ch)
                                result(you,pc)
                            try:
                                th=threading.Thread(target=do)
                                th.daemon=True
                                th.start()
                            except:
                                pass

                        elif ln==4: #level 4
                            for i in range(42,58):
                                    ch=chr(i)
                                    ran.append(ch)
                            ran.append(chr(39))
                            ran.append(chr(59))
                            ran.append(chr(61))
                            ran.append(chr(91))
                            ran.append(chr(92))
                            ran.append(chr(93))
                            ran.append(chr(96))
                            def do():
                                t.sleep(2)
                                for i in range(len(ran)):
                                    ch=r.choice(ran)
                                    pc.append(ch)
                                    game_char=Label(main,text=ch,bg='snow',fg='red',font='Areal 40 bold')
                                    game_char.place(x=220,y=250)
                                    t.sleep(time)
                                    u=game_entry.get()
                                    you.append(u)
                                    game_entry.delete(0,END)
                                    game_char.place_forget()
                                    ran.remove(ch)
                                result(you,pc)
                            try:
                                th=threading.Thread(target=do)
                                th.daemon=True
                                th.start()
                            except:
                                pass
                        elif ln==5: #level 5
                            for i in range(33,65):
                                ch=chr(i)
                                ran.append(ch)
                            for i in range(91,97):
                                ch=chr(i)
                                ran.append(ch)
                            for i in range(123,127):
                                ch=chr(i)
                                ran.append(ch)

                            def do():
                                t.sleep(2)
                                for i in range(42):
                                    ch=r.choice(ran)
                                    pc.append(ch)
                                    game_char=Label(main,text=ch,bg='snow',fg='red',font='Areal 40 bold')
                                    game_char.place(x=220,y=250)
                                    t.sleep(time)
                                    u=game_entry.get()
                                    you.append(u)
                                    game_entry.delete(0,END)
                                    game_char.place_forget()
                                    ran.remove(ch)
                                result(you,pc)
                            try:
                                th=threading.Thread(target=do)
                                th.daemon=True
                                th.start()
                            except:
                                pass


                        elif ln==6: #level 6
                            for i in range(33,97):
                                ch=chr(i)
                                ran.append(ch)

                            for i in range(123,127):
                                ch=chr(i)
                                ran.append(ch)

                            def do():
                                t.sleep(2)
                                for i in range(68):
                                    ch=r.choice(ran)
                                    pc.append(ch)
                                    game_char=Label(main,text=ch,bg='snow',fg='red',font='Areal 40 bold')
                                    game_char.place(x=220,y=250)
                                    t.sleep(time)
                                    u=game_entry.get()
                                    you.append(u)
                                    game_entry.delete(0,END)
                                    game_char.place_forget()
                                    ran.remove(ch)
                                result(you,pc)
                            try:
                                th=threading.Thread(target=do)
                                th.daemon=True
                                th.start()
                            except:
                                pass

                        elif ln==7: #level 7
                            for i in range(33,127):
                                ch=chr(i)
                                ran.append(ch)

                            def do():
                                t.sleep(2)
                                for i in range(94):
                                    ch=r.choice(ran)
                                    pc.append(ch)
                                    game_char=Label(main,text=ch,bg='snow',fg='red',font='Areal 40 bold')
                                    game_char.place(x=220,y=250)
                                    t.sleep(time)
                                    u=game_entry.get()
                                    you.append(u)
                                    game_entry.delete(0,END)
                                    game_char.place_forget()
                                    ran.remove(ch)
                                result(you,pc)
                            try:
                                th=threading.Thread(target=do)
                                th.daemon=True
                                th.start()
                            except:
                                pass




                    DB={'2':'easy','1':'medium','0.5':'hard','0.3':'advanced'}
                    flag=1
                    try:
                        cursor.execute('select '+DB[str(time)]+' from profile where pro_no='+str(pno))
                        for i in cursor:
                            fin=int(i[0])

                        if l==fin+1 or l<=fin:
                            flag=0
                        else:
                            pass
                    except:
                        flag=0

                    if flag==0:
                        lev.grid_forget()
                        info_lev.place_forget()
                        l1.place_forget()
                        l2.place_forget()
                        l3.place_forget()
                        l4.place_forget()
                        l5.place_forget()
                        l6.place_forget()
                        l7.place_forget()
                        back.place_forget()
                        start(l)

                lev=Label(main,text='***********  SELECT LEVEL   ',bg='light blue',fg='black',font='Verdana 15 bold italic')
                info_lev=Label(main,text='G\nI\nV\nE\n \nY\nO\nU\nR\n \nB\nE\nS\nT',fg='red',font='Verdana 12 bold italic')

                l1=Button(main,text='LEVEL 1',bg='light green',fg='blue',font='Verdana 10 bold italic',command=lambda:task(1))


                nocolour=['light gray','white']
                scolour=['light green','blue']

                global pno,mydb,cursor
                DB={'2':'easy','1':'medium','0.5':'hard','0.3':'advanced'}
                try:
                    cursor.execute('select '+DB[str(time)]+' from profile where pro_no='+str(pno))
                    for i in cursor:
                        fin=int(i[0])
                    while True:
                        if 2<=fin or 2==fin+1:
                            l2=Button(main,text='LEVEL 2',bg=scolour[0],fg=scolour[1],font='Verdana 10 bold italic',command=lambda:task(2))
                            if 2==fin+1:
                                l3=Button(main,text='LEVEL 3',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(3))
                                l4=Button(main,text='LEVEL 4',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(4))
                                l5=Button(main,text='LEVEL 5',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(5))
                                l6=Button(main,text='LEVEL 6',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(6))
                                l7=Button(main,text='LEVEL 7',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(7))
                                break
                        else:
                            l2=Button(main,text='LEVEL 2',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(2))
                            l3=Button(main,text='LEVEL 3',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(3))
                            l4=Button(main,text='LEVEL 4',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(4))
                            l5=Button(main,text='LEVEL 5',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(5))
                            l6=Button(main,text='LEVEL 6',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(6))
                            l7=Button(main,text='LEVEL 7',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(7))
                            break

                        if 3<=fin or 3==fin+1:
                            l3=Button(main,text='LEVEL 3',bg=scolour[0],fg=scolour[1],font='Verdana 10 bold italic',command=lambda:task(3))
                            if 3==fin+1:
                                l4=Button(main,text='LEVEL 4',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(4))
                                l5=Button(main,text='LEVEL 5',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(5))
                                l6=Button(main,text='LEVEL 6',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(6))
                                l7=Button(main,text='LEVEL 7',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(7))
                                break
                        if 4<=fin or 4==fin+1:
                            l4=Button(main,text='LEVEL 4',bg=scolour[0],fg=scolour[1],font='Verdana 10 bold italic',command=lambda:task(4))
                            if 4==fin+1:
                                l5=Button(main,text='LEVEL 5',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(5))
                                l6=Button(main,text='LEVEL 6',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(6))
                                l7=Button(main,text='LEVEL 7',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(7))
                                break
                        if 5<=fin or 5==fin+1:
                            l5=Button(main,text='LEVEL 5',bg=scolour[0],fg=scolour[1],font='Verdana 10 bold italic',command=lambda:task(5))
                            if 5==fin+1:
                                l6=Button(main,text='LEVEL 6',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(6))
                                l7=Button(main,text='LEVEL 7',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(7))
                                break
                        if 6<=fin or 6==fin+1:
                            l6=Button(main,text='LEVEL 6',bg=scolour[0],fg=scolour[1],font='Verdana 10 bold italic',command=lambda:task(6))
                            if 6==fin+1:
                                l7=Button(main,text='LEVEL 7',bg=nocolour[0],fg=nocolour[1],font='Verdana 10 bold italic',command=lambda:task(7))
                                break
                        if 7<=fin or 7==fin+1:
                            l7=Button(main,text='LEVEL 7',bg=scolour[0],fg=scolour[1],font='Verdana 10 bold italic',command=lambda:task(7))
                            break

                except:
                    l2=Button(main,text='LEVEL 2',bg=scolour[0],fg=scolour[1],font='Verdana 10 bold italic',command=lambda:task(2))
                    l3=Button(main,text='LEVEL 3',bg='light green',fg='blue',font='Verdana 10 bold italic',command=lambda:task(3))
                    l4=Button(main,text='LEVEL 4',bg='light green',fg='blue',font='Verdana 10 bold italic',command=lambda:task(4))
                    l5=Button(main,text='LEVEL 5',bg='light green',fg='blue',font='Verdana 10 bold italic',command=lambda:task(5))
                    l6=Button(main,text='LEVEL 6',bg='light green',fg='blue',font='Verdana 10 bold italic',command=lambda:task(6))
                    l7=Button(main,text='LEVEL 7',bg='light green',fg='blue',font='Verdana 10 bold italic',command=lambda:task(7))




                back=Button(main,text='BACK',font='Verdana 10 bold italic',command=Back)

                lev.grid(row=0,column=1,pady=23,padx=40)
                info_lev.place(x=30,y=60)
                l1.place(x=90,y=107)
                l2.place(x=194,y=107)
                l3.place(x=306,y=107)
                l4.place(x=90,y=150)
                l5.place(x=306,y=150)
                l6.place(x=90,y=195)
                l7.place(x=306,y=195)
                back.place(x=215,y=285)

            difi=str(difi)
            tim={'1':2,'2':1,'3':0.5,'4':0.3}    #time dict for dificulty
            if difi=='5':
                def check(Event):
                    sle=tbox.get()
                    try:
                        sle=float(sle)
                        if sle<=0:
                            tbox.delete(0,END)
                            warning.place(x=30,y=60)
                        else:
                            cus.grid_forget()
                            tbox.place_forget()
                            tinfo.place_forget()
                            warning.place_forget()

                            tim['5']=sle
                            time=tim[difi]
                            lev(time)


                    except:
                        tbox.delete(0,END)
                        warning.place(x=30,y=60)

                if cust==None:
                    cus=Label(main,text='*************  CUSTOMIZE   ',bg='light blue',fg='black',font='Verdana 15 bold italic')
                    tbox=Entry(main,width=13,fg='blue',font='Verdana 17 italic')
                    tinfo=Label(text='Give the time you\nwant to have as\ninterval between each\ncharacter(in seconds)',bg='snow',fg='red')
                    tbox.bind('<Return>',check)
                    tbox.focus()
                    warning=Label(main,text='I\nN\nV\nA\nL\nI\nD\n \nT\nI\nM\nE',fg='red',font='Verdana 12 bold italic')


                    cus.grid(row=0,column=1,pady=23,padx=40)
                    tbox.place(x=127,y=93)
                    tinfo.place(x=174,y=255)

                else:
                    tim['5']=cust
                    time=tim[difi]
                    lev(time)


            else:
                time=tim[difi]
                lev(time)


        def forget(difi):
            lev_title.grid_forget()
            easy.place_forget()
            medium.place_forget()
            hard.place_forget()
            advanced.place_forget()
            custom.place_forget()
            helpbt.place_forget()
            sel_opp.place_forget()
            if difi==6:
                select_option()
            else:
                level_page(difi)

        lev_title=Label(main,text='********  SELECT DIFICULTY  ',bg='light blue',fg='black',font='Verdana 15 bold italic')
        easy=Button(main,text='      EASY      ',bg='light green',fg='blue',command=lambda:forget(1))
        medium=Button(main,text='   MEDIUM   ',bg='light blue',fg='green',command=lambda:forget(2))
        hard=Button(main,text='      HARD     ',bg='red',fg='white',command=lambda:forget(3))
        advanced=Button(main,text=' ADVANCED',bg='purple',fg='white',command=lambda:forget(4))
        custom=Button(main,text='   CUSTOM   ',bg='gold',fg='blue',command=lambda:forget(5))
        helpbt=Button(main,text='      HELP      ',bg='pink',fg='black',command=helpme)
        sel_opp=Button(main,text='OPTION',font='Verdana 10 bold italic',command=lambda:forget(6))

        lev_title.grid(row=0,column=1,pady=23,padx=40)
        easy.place(x=10,y=75)
        medium.place(x=10,y=116)
        hard.place(x=10,y=160)
        advanced.place(x=10,y=206)
        custom.place(x=10,y=247)
        helpbt.place(x=10,y=287)
        sel_opp.place(x=215,y=285)

    def create_profile():
        def add(Event):
            global cursor,mydb,pno,len_pno
            name=entry.get()
            len_pno=int(len_pno)+1
            cursor.execute('insert into profile(pro_no,pro_name) values(\''+str(len_pno)+'\',\''+name+'\')')
            mydb.commit()
            pno=len_pno
            pro_title.grid_forget()
            info.place_forget()
            entry.place_forget()
            home_page()

        pro_title=Label(main,text='*********  CREATE PROFILE  ',bg='light blue',fg='black',font='Verdana 15 bold italic')
        info=Label(main,text='G\nI\nV\nE\n \nY\nO\nU\nR\n \nN\nA\nM\nE',fg='red',font='Verdana 12 bold italic')
        entry=Entry(main,width=13,fg='blue',font='Verdana 17 italic')
        entry.bind('<Return>',add)
        entry.focus()

        pro_title.grid(row=0,column=1,pady=23,padx=40)
        info.place(x=30,y=60)
        entry.place(x=127,y=93)


    def select_profile():
        global cursor,mydb,pno

        def next():
            global pno
            try:
                pno=listbox.curselection()
                pno=index[pno[0]]
                sel_pro_title.grid_forget()
                listbox.place_forget()
                next_btn.place_forget()
                home_page()
            except:
                pass
        sel_pro_title=Label(main,text='*********  SELECT PROFILE  ',bg='light blue',fg='black',font='Verdana 15 bold italic')
        listbox=Listbox(main,height=11,width=19,bg='LightSteelBlue2',font='Verdana 8 bold italic')
        next_btn=Button(main,text=' NEXT',bg='purple',fg='white',command=next,font='Verdana 13 bold italic')

        cursor.execute('select * from profile')
        index=[]
        for i in cursor:
            index.append(i[0])
            listbox.insert(END,i[1])
            listbox.yview(END)


        sel_pro_title.grid(row=0,column=1,pady=23,padx=40)
        listbox.place(x=8,y=93)
        next_btn.place(x=210,y=110)



    def _next():
        opt_title.grid_forget()
        select_pro.place_forget()
        create_pro.place_forget()
        create_profile()

    def __next():
        opt_title.grid_forget()
        select_pro.place_forget()
        create_pro.place_forget()
        select_profile()

    if f!=0:
        opt_title=Label(main,text='**********  SELECT OPTION  ',bg='light blue',fg='black',font='Verdana 15 bold italic')
        select_pro=Button(main,text=' SELECT\nPROFILE',bg='purple',fg='white',command=__next,font='Verdana 14 bold italic')
        create_pro=Button(main,text=' CREATE\nPROFILE',bg='light green',fg='blue',command=_next,font='Verdana 14 bold italic')

        opt_title.grid(row=0,column=1,pady=23,padx=40)
        select_pro.place(x=8,y=100)
        create_pro.place(x=8,y=188)
    else:
        create_profile()


# SQL ***********************************************************
def connect(Event=None):
    pwd=pass_entry.get()
    try:
        global cursor,mydb,pno,len_pno
        mydb=mysql.connect(host='localhost',user='root',passwd=pwd) # connecting with the MySQL
        cursor=mydb.cursor()
    except:
        main.destroy()
        return


    try:
        cursor.execute('use typing_profile')

    except:
        cursor.execute('create database typing_profile')
        cursor.execute('use typing_profile')
        cursor.execute('create table profile(pro_no varchar(50) primary key not null,pro_name varchar(50) not null,easy varchar(10) default \'0\' not null,medium varchar(10) default \'0\' not null,hard varchar(10) default \'0\' not null,advanced varchar(10) default \'0\' not null)')

    pro=[]
    cursor.execute('select * from profile')
    for i in cursor:
        pro.append(i)

    pasw_title.grid_forget()
    pass_info.place_forget()
    pass_entry.place_forget()
    ok.place_forget()
    note.place_forget()

    len_pno=len(pro)

    if pro ==[]:
        select_option(0)
    else:
        select_option()

#def test():




# GUI *********************************************************

main=Tk()   #creating main window
main.geometry('390x320+500+50')    #set size of window
main.resizable(height=False,width=False)
main.iconbitmap('Resources\icon.ico')
main.title('FAST TYPING')
img=PhotoImage(file=r'Resources\bg.png')
Label(main,image=img).place(relwidth=2,relheight=1)
#...........................................................


pasw_title=Label(main,text='*****************    GIVE   ',bg='light blue',fg='black',font='Verdana 15 bold italic')
pass_info=Label(main,text='S\nQ\nL\n \nP\nA\nS\nS\nW\nO\nR\nD',fg='red',font='Verdana 12 bold italic')
pass_entry=Entry(main,show='*',width=13,fg='blue',font='Verdana 17 italic')
pass_entry.bind('<Return>',connect)
pass_entry.focus()
ok=Button(main,text=' NEXT',bg='purple',fg='white',command=connect,font='Verdana 13 bold italic')
note=Label(main,text='WRONG PASSWORD\nWILL CLOSE\nTHE PROGRAM',fg='red',bg='snow',font='Verdana 7 bold italic')

pasw_title.grid(row=0,column=1,pady=23,padx=40)
pass_info.place(x=30,y=60)
pass_entry.place(x=127,y=93)
ok.place(x=293,y=135)
note.place(x=180,y=270)

'''
th=threading.Thread(target=test)
th.daemon=True
th.start()'''

main.mainloop()
sys.exit()


#**************************************************************
'''print('\nTHANK YOU\n\nDONT FORGET TO GIVE FEEDBACK :) \nAND RATTING :D ')
z=input('\nPRESS ENTER')'''
