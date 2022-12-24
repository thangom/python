import theatre,user

if theatre.lang==1:
    theatre.Movie.tam_movie(theatre.lang)
    theatre.Time.show_time()
    theatre.Seat.user_seats()
    user.User_details.user_info()
    user.User_details.confirmed_tkts()

elif theatre.lang==2:
    theatre.Movie.eng_movie(theatre.lang)
    theatre.Time.show_time()
    theatre.Seat.user_seats()
    user.User_details.user_info()
    user.User_details.confirmed_tkts()

elif theatre.lang==3:
    theatre.Movie.hin_movie(theatre.lang)
    theatre.Time.show_time()
    theatre.Seat.user_seats()
    user.User_details.user_info()
    user.User_details.confirmed_tkts()
    
elif theatre.lang==4:
    theatre.Movie.kan_movie(theatre.lang)
    theatre.Time.show_time()
    theatre.Seat.user_seats()
    user.User_details.user_info()
    user.User_details.confirmed_tkts()
    
elif theatre.lang==5:
    theatre.Movie.tel_movie(theatre.lang)
    theatre.Time.show_time()
    theatre.Seat.user_seats()
    user.User_details.user_info()
    user.User_details.confirmed_tkts()
    
elif theatre.lang==6:
    theatre.Movie.mal_movie(theatre.lang)
    theatre.Time.show_time()
    theatre.Seat.user_seats()
    user.User_details.user_info()
    user.User_details.confirmed_tkts()

else:
    print("\nYou Entered Wrong Number to select language!!!")
    
