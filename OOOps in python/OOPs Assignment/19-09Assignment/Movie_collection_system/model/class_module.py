'''============================================================
ASSIGNMENT 7 – MOVIE COLLECTION SYSTEM
======================================

Create a Movie class inside:

models/movie.py

ATTRIBUTES:

* movie_id
* movie_name
* genre
* rating
* ticket_price

TASKS:

1. Take details of 5 movies from the user.
2. Create Movie objects.
3. Store all objects in a list.
4. Display all movies.
5. Display movies having rating greater than 8.
6. Display all Action movies.
7. Find the highest-rated movie.
8. Search a movie using Movie Id.
9. Calculate average movie rating.
10. Display movies whose ticket price is greater than 300.

SAMPLE DATA:

101 Dangal Drama 8.4 250
102 Jawan Action 7.5 300
103 3Idiots Drama 8.4 200
104 Bahubali Action 8.1 350
105 Pathaan Action 7.0 320

EXPECTED OUTPUT:

Movies with rating greater than 8:

Dangal 8.4
3Idiots 8.4
Bahubali 8.1

Action Movies:

Jawan
Bahubali
Pathaan

Highest Rated Movie:

Dangal 8.4

Movies with ticket price greater than 300:

Bahubali 350
Pathaan 320

Average Movie Rating:

7.88

Search Movie Id: 104

Movie Found:

104 Bahubali Action 8.1 350
'''
movies=[]
class movie:
    def __init__(self):
        self.movie_id=int(input("Enter Movie ID:"))
        self.movie_name=input("Enter Movie Name:")
        self.genre=input("Enter Show type:").lower()
        self.rating=float(input("Enter Movie Rating:"))
        self.ticket_price=int(input("Enter Movie Ticket Price:"))
        movies.append(self)

    def display(self):
        print("\nMovie Details")
        for i in movies:
            print(i.movie_id,i.movie_name,i.genre,i.rating,i.ticket_price)

    def rating_(self):
        print("\nMovie With rating greater the 8:")
        for i in movies:
            if i.rating>8:
                print(i.movie_id,i.movie_name,i.genre,i.rating,i.ticket_price)

    def action(self):
        print("\nAction Movies:")
        for i in movies:
            if i.genre>"action":
                print(i.movie_id,i.movie_name,i.genre,i.rating,i.ticket_price)

    def high_rating(self):
        print("\nHighest Rating movie:")
        high=0
        for i in movies:
            if i.rating>high:
                high=i.rating
        for i in movies:
            if i.rating==high:
                print(i.movie_id,i.movie_name,i.genre,i.rating,i.ticket_price)

    def found_movie(self):
        self.id=int(input("\nEnter Movie ID:"))
        for i in movies:
            if i.movie_id==self.id:
                print(i.movie_id,i.movie_name,i.genre,i.rating,i.ticket_price)
                break
        else:
            print("Movie Not Found")

    def average(self):
        total=0
        print("\nAverage Movie Rating")
        for i in movies:
            total=total + i.rating
        print(total/len(movies))

    def greater(self):
        print("\nMovie With ticket price greater than 300:")
        for i in movies:
            if i.ticket_price>300:
                print(i.movie_id,i.movie_name,i.genre,i.rating,i.ticket_price)
    