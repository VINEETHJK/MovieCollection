def addMovie(name,director,year):
    pass

def listMovies():
    pass

def findMovie(movieName):
    pass


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
            break
        elif user_input == '2':
            listMovies()
            break
        elif user_input == '3':
            find_movie = input("Please enter the movie name you want to find: ").lower()
            findMovie(find_movie)
            break
        else:
            print("""Please enter '1' for adding a movie, 
            '2' for listing all the movies,
            '3' for finding a movie, 
            or 'q' for quitting the program.""")
            user_input = input("Please enter one of the above options: ").lower()

        

        


