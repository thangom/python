class Movie:
    global langlst
    global lang
    print("\nWelcome to Stark cinemas!")
    langlst=["Tamil","English","Hindi","Kannada","Telugu","Malayalam"]
    lang=int(input("\nMovie languages\n1.Tamil\n2.English\n3.Hindi\n4.Kannada\n5.Telugu\n6.Malayalam\n\nPlease choose the Lanuage: "))


    def tam_movie(self):
        global movie_input,movielst
        movielst=["Love today","Coffee with kadhal","Niththam oru vaanam","Sardar","Prince","Ponniyin selvan:part1"]
        print("\n1.Love today\n2.Coffee with kadhal\n3.Niththam oru vaanam\n4.Sardar\n5.Prince\n6.Ponniyin selvan:part1")
        movie_input=int(input("\nChoose your movie: "))
        if movie_input==1:
            print("\nYour Movie is",movielst[0])
        elif movie_input==2:
            print("\nYour Movie is",movielst[1])
        elif movie_input==3:
            print("\nYour Movie is",movielst[2])
        elif movie_input==4:
            print("\nYour Movie is",movielst[3])
        elif movie_input==5:
            print("\nYour Movie is",movielst[4])
        elif movie_input==6:
            print("\nYour Movie is",movielst[5])
        else:
            print("\nYou entered wrong number")
    def eng_movie(self):
        global movielst2,movie_input
        movielst2=["Black panther:Wakanda forever","Black adam","The fabelmans","The invitation","Halloween ends","Ticket to paradise"]
        print("\n1.Black panther:Wakanda forever\n2.Black adam\n3.The fabelmans\n4.The invitation\n5.Halloween ends\n6.Ticket to paradise")
        movie_input=int(input("\nChoose your movie: "))
        if movie_input==1:
            print("\nYour Movie is",movielst2[0])
        elif movie_input==2:
            print("\nYour Movie is",movielst2[1])
        elif movie_input==3:
            print("\nYour Movie is",movielst2[2])
        elif movie_input==4:
            print("\nYour Movie is",movielst2[3])
        elif movie_input==5:
            print("\nYour Movie is",movielst2[4])
        elif movie_input==6:
            print("\nYour Movie is",movielst2[5])
        else:
            print("\nYou entered wrong number")
    def hin_movie(self):
        global movielst3,movie_input
        movielst3=["Good bye","Thank god","Doctor g","Phone bhoot","Rocket gang","Double xl"]
        print("\n1.Good bye\n2.Thank god\n3.Doctor g\n4.Phone bhoot\n5.Rocket gang\n6.Double xl")
        movie_input=int(input("\nChoose your movie: "))
        if movie_input==1:
            print("\nYour Movie is",movielst3[0])
        elif movie_input==2:
            print("\nYour Movie is",movielst3[1])
        elif movie_input==3:
            print("\nYour Movie is",movielst3[2])
        elif movie_input==4:
            print("\nYour Movie is",movielst3[3])
        elif movie_input==5:
            print("\nYour Movie is",movielst3[4])
        elif movie_input==6:
            print("\nYour Movie is",movielst3[5])
        else:
            print("\nYou entered wrong number")
    def kan_movie(self):
        global movielst4,movie_input
        movielst4=["Kaanthara","Banaras","Vikrant rona","Love 360","Wedding gift","Window seat"]
        print("\n1.Kaanthara\n2.Banaras\n3.Vikrant rona\n4.Love 360\n5.Wedding gift\n6.Window seat")
        movie_input=int(input("\nChoose your movie: "))
        if movie_input==1:
            print("\nYour Movie is",movielst4[0])
        elif movie_input==2:
            print("\nYour Movie is",movielst4[1])
        elif movie_input==3:
            print("\nYour Movie is",movielst4[2])
        elif movie_input==4:
            print("\nYour Movie is",movielst4[3])
        elif movie_input==5:
            print("\nYour Movie is",movielst4[4])
        elif movie_input==6:
            print("\nYour Movie is",movielst4[5])
        else:
            print("\nYou entered wrong number")
    def tel_movie(self):
        global movielst5,movie_input
        movielst5=["Yashoda","Aadhaaram","Thaggedele","Aakasam","Mister mummy","The ghost"]
        print("\n1.Yashoda\n2.Aadhaaram\n3.Thaggedele\n4.Aakasam\n5.Mister mummy\n6.The ghost")
        movie_input=int(input("\nChoose your movie: "))
        if movie_input==1:
            print("\nYour Movie is",movielst5[0])
        elif movie_input==2:
            print("\nYour Movie is",movielst5[1])
        elif movie_input==3:
            print("\nYour Movie is",movielst5[2])
        elif movie_input==4:
            print("\nYour Movie is",movielst5[3])
        elif movie_input==5:
            print("\nYour Movie is",movielst5[4])
        elif movie_input==6:
            print("\nYour Movie is",movielst5[5])
        else:
            print("\nYou entered wrong number")
    def mal_movie(self):
        global movielst6,movie_input
        movielst6=["Jeya jeya jeya jeya hey","Saturday night","Panthrand","Kumari","Padavettu","Monster"]
        print("\n1.Jeya jeya jeya jeya hey\n2.Saturday night\n3.Panthrand\n4.Kumari\n5.Padavettu\n6.Monster")
        movie_input=int(input("\nChoose your movie: "))
        if movie_input==1:
            print("\nYour Movie is",movielst6[0])
        elif movie_input==2:
            print("\nYour Movie is",movielst6[1])
        elif movie_input==3:
            print("\nYour Movie is",movielst6[2])
        elif movie_input==4:
            print("\nYour Movie is",movielst6[3])
        elif movie_input==5:
            print("\nYour Movie is",movielst6[4])
        elif movie_input==6:
            print("\nYour Movie is",movielst6[5])
        else:
            print("\nYou entered wrong number")

class Time:
    def show_time():
        global showtime,user_time
        showtime = ["10:00 Am" ,"02:00 Pm", "06:00 Pm", "10:00 Pm"] 
        i=1
        for i,value in enumerate (showtime):
            print(i+1,":",value,"\n")
        user_time =  int(input("Enter your Time slot: "))

class Seat:
    def user_seats(): 
        n,m=10,10
        print("\nSeats View\n")
        for i in range(0, n + 1):
            if i == 0:
                for j in range(0, m + 1):
                    print(j, end=" ")
            else:
                print(i, end=" ")
                for k in range(m):
                    print("S", end=" ")
            print()
        global l,user_seat
        l=[]
        user_seat=int(input("\nEnter your ticket/s count: "))
        for i in range(1,user_seat+1):
            r,c=map(int,input("\nEnter your seat row,column:").split())
            print("\nYour seat",i,"is: ",r,"row and",c,"column confirmed")
            l.append((r,c))
        print("\nYour Ticket/s Price: ",user_seat*100)
