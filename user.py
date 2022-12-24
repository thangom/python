import theatre

class User_details:
    def user_info():
        global username,age,gender,mobile_number
        print("\nEnter your details to confirm your ticket/s")
        username=input("\nName: ")
        age=int(input("\nAge: "))
        gender=input("\nGender: ")
        mobile_number=int(input("\nMobile Number: "))

    def confirmed_tkts():
        print("\nYour Ticket/s are confirmed!\n\nYour Booking Details")
        print("\n1.Language of Movie: ",theatre.langlst[theatre.lang-1])
        if theatre.langlst[theatre.lang-1]=='Tamil':
            print("\n2.Title of Movie: ",theatre.movielst[theatre.movie_input-1])
        elif theatre.langlst[theatre.lang-1]=='English':
            print("\n2.Title of Movie: ",theatre.movielst2[theatre.movie_input-1])
        elif theatre.langlst[theatre.lang-1]=='Hindi':
            print("\n2.Title of Movie: ",theatre.movielst3[theatre.movie_input-1])
        elif theatre.langlst[theatre.lang-1]=='Kannada':
            print("\n2.Title of Movie: ",theatre.movielst4[theatre.movie_input-1])
        elif theatre.langlst[theatre.lang-1]=='Telugu':
            print("\n2.Title of Movie: ",theatre.movielst5[theatre.movie_input-1])
        elif theatre.langlst[theatre.lang-1]=='Malayalam':
            print("\n2.Title of Movie: ",theatre.movielst6[theatre.movie_input-1])
    
        print("\n3.Show time: ",theatre.showtime[theatre.user_time-1])
        print("\n4.Number of Tickets: ",theatre.user_seat)
        print("\n5.Ticket/s Price: 100 * ",theatre.user_seat,"=",100*theatre.user_seat)
        print("\n6.User Info:\n\nUsername: ",username,"\n\nAge: ",age,"\n\nGender: ",gender,"\n\nMobile Number: ",mobile_number)
        print("\n<----Thank You!---->")