movie_list = []
movie_dict = {}
user_input = None

def addMovie(name,director,year):
    movie_dict = {'Name': name, 'Director': director, 'Year': year}
    movie_list.append(movie_dict)

def listMovies():
    for movie in movie_list:
        print(movie)

def findMovie(movieName):
    for movie in movie_list:
        if movie['Name'] == movieName:
            print(movie)


print("""Enter one of the following options.
            1. Adding a movie to your collection
            2. Listing all the movies in your collection
            3. Finding a movie in your collection 
            q. Qutting the program\n""")
user_input = input("Please enter one of the above options: ").lower()

while user_input != 'q':
        if user_input == '1':
            movie_name = input("Please enter the movie name you want to add: ").lower()
            movie_director = input("Please enter the movie director name: ").lower()
            movie_year = input("Please enter the year when the movie was released: ").lower()
            addMovie(movie_name, movie_director, movie_year)
            print("""\nEnter one of the following options.
            1. Adding a movie to your collection
            2. Listing all the movies in your collection
            3. Finding a movie in your collection 
            q. Qutting the program\n""")
            user_input = input("Please enter one of the above options: ").lower()
            continue
        elif user_input == '2':
            listMovies()
            print("""\nEnter one of the following options.
            1. Adding a movie to your collection
            2. Listing all the movies in your collection
            3. Finding a movie in your collection 
            q. Qutting the program\n""")
            user_input = input("Please enter one of the above options: ").lower()
            continue
        elif user_input == '3':
            find_movie = input("Please enter the movie name you want to find: ").lower()
            findMovie(find_movie)
            print("""\nEnter one of the following options.
            1. Adding a movie to your collection
            2. Listing all the movies in your collection
            3. Finding a movie in your collection 
            q. Qutting the program\n""")
            user_input = input("Please enter one of the above options: ").lower()
            continue
        else:
           print("""\nEnter one of the following options.
            1. Adding a movie to your collection
            2. Listing all the movies in your collection
            3. Finding a movie in your collection 
            q. Qutting the program\n""")
           user_input = input("Please enter one of the above options: ").lower()

        

        


