'''4. Movie Ticket Booking
 
Create a Cinema class with:
 
*Attributes: movies (dict → movie: seats available)
 
*Methods:
 
* book(movie, seats) → reduces seat count
 
* cancel(movie, seats) → adds back seats
 
* show_movies() → shows available seats
 
Sample Input:
 
python
 
cinema = Cinema({"Avatar": 10, "Batman": 5})
 
print(cinema.book("Avatar", 2))
 
print(cinema.cancel("Avatar", 1))
 
cinema.show_movies()
 

 
Sample Output:
 

 
Booked 2 tickets for Avatar
 
Cancelled 1 ticket for Avatar
 
Movies: {'Avatar': 9, 'Batman': 5}
 

 '''


class Cinema:
    def __init__(self, movies):
        self.movies = movies

    def book(self, movie, seats):
        if movie in self.movies and self.movies[movie] >= seats:
            self.movies[movie] -= seats
            return "Booked", seats, "tickets for", movie
        else:
            return "Not enough seats or movie not found"

    def cancel(self, movie, seats):
        if movie in self.movies:
            self.movies[movie] += seats
            return "Cancelled", seats, "ticket for", movie
        else:
            return "Movie not found"

    def show_movies(self):
        print("Movies:", self.movies)
cinema = Cinema({"Avatar": 10, "Batman": 5})

print(cinema.book("Avatar", 2))
print(cinema.cancel("Avatar", 1))
cinema.show_movies()
