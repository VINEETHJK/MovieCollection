movie_list = []
movie_dict = {}
user_input = None
MENU_PROMPT = "\n Enter 'a' to add a movie, 'l' to list to your movies, 'f' to find a movie and 'q' to quit the program: "


def addMovie():
    name = input("Enter the movie name you want to add: ").lower()
    director = input("Enter the movie director name: ").lower()
    year = input("Enter the year when the movie was released: ").lower()
    movie_dict = {'Name': name, 'Director': director, 'Year': year}
    movie_list.append(movie_dict)

def listMovies():
    for movie in movie_list:
        print_movie_details(movie)

def findMovie():
    search_title = input("Enter the movie title you want to find: ")
    for movie in movie_list:
        if movie['Name'] == search_title:
            print_movie_details(movie)

def print_movie_details(movie):
        print(f"Name: {movie['Name']}")
        print(f"Director: {movie['Director']}")
        print(f"Year: {movie['Year']}\n")
        

def menu():
    user_input = input(MENU_PROMPT).lower()
    while user_input != 'q':
        if user_input == 'a':
            addMovie()
        elif user_input == 'l':
            listMovies()
        elif user_input == 'f':
            findMovie()
        else:
            print('Unknown command.Please try again.')

        user_input = input(MENU_PROMPT).lower()
        
menu()

