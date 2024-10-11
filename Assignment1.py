allMovies = [

    # dictionary1
    {
    "movieId": "1",
    "name": "Mission Impossible 14 - The AARP Threat",
    "pineappleMetric": "88",
    "releaseYear": 2018,
    "rating": "PG-13",
    "runtime": 136,
    "director": "Robert Silva",
    "writer": ["Mary Silva", "Mario Silva"],
    "productionCompany": {
            "prodCompanyName": "Rinse Wash Repeat",
            "prodCompanyLocation": "USA"
    },
    "budget": 127000000,
    "boxOffice": [32000000, 15000000]
},

    # dictionary2
    {
    "movieId": "2",
    "name": "Die Hard - Resurrection",
    "pineappleMetric": "58",
    "releaseYear": 2019,
    "rating": "R",
    "runtime": 117,
    "director": "Joan Smith",
    "writer": ["Terry Smith", "Francine Smith"],
    "productionCompany": {
            "prodCompanyName": "Yippee-Ki-Yay",
            "prodCompanyLocation": "Australia"
    },
    "budget": 63000000,
    "boxOffice": [19000000, 7000000, 5300000]
},

    # dictionary3
 {
    "movieId": "3",
    "name": "Fifty Shades Greener",
    "pineappleMetric": "35",
    "releaseYear": 2018,
    "rating": "PG",
    "runtime": 98,
    "director": "Cookie Muster",
    "writer": ["Elmo Jones", "Sue Bird"],
    "productionCompany": {
            "prodCompanyName": "Sesame Muppets",
            "prodCompanyLocation": "UK"
    },
    "budget": 17000000,
    "boxOffice": [58000000, 43000000, 27000000, 13000000]
}
    ]

allReviews = [

    # dictionary4
    {
    "reviewId": "1",
    "reviewAuthor": "Timmy Twopence",
    "reviewDate": "2019-07-23",
    "reviewText": "It is an unexpected pleasure to have John McClane back as a zombie pursuing the nefarious masterminds behind a plan to dominate the world by transforming most of the population into undead slaves",
    "movieID": "2"
},

    # dictionary5
    {
    "reviewId": "2",
    "reviewAuthor": "Sylvia Sterling",
    "reviewDate": "2018-06-12",
    "reviewText": "In this exciting movie, Ethan Hunt battles his worst enemy ever: a nefarious organization that advocates the retirement of actors when they are too old to play leads in action movies",
    "movieID": "1"
},

    # dictionary6

    {
    "reviewId": "3",
    "reviewAuthor": "Francis Pounder",
    "reviewDate": "2018-12-04",
    "reviewText": "Kermit the Frog against a nefarious industrialist trying to pollute the world is a fun premise but the use of powerpoint slides during the movie is very distracting",
    "movieID": "3"
}
]


# a. Print the name of all movies released in 2018.
print("All Movies Released in 2018:")
for movie in allMovies:
    if movie['releaseYear'] == 2018:
        print(movie['name'])


# b. Print the name of all movies with a Pineapple Metric lower than 50.
print()
print("Movies with a Pineapple Metric lower than 50:")
for movie in allMovies:
    if int(movie['pineappleMetric']) < 50:
        print(movie['name'])

# c. Print the name of all movies whose production company is located in the “UK”.
print()
print("Movies with a Production Company in the UK:")
for movie in allMovies:
    if movie['productionCompany']['prodCompanyLocation'] == "UK":
        print(movie['name'])
# d. Print the name and opening week box office (ONLY these “columns”) from all movies.
print()
print("Movies and Opening Week Box Office:")
for movie in allMovies:
       print(f"{movie['name']}: ${movie['boxOffice'][0]}.00")
# e. Print the name of all movies produced by “Rinse Wash Repeat”
print()
print("Movies with a Production Company in the UK:")
for movie in allMovies:
    if movie['productionCompany']['prodCompanyName'] == "Rinse Wash Repeat":
        print(movie['name'])
        print()
# f. Print the details of all reviews for a movie name input by the user.
print()
print("List of All Movies:")
for movie in allMovies:
    print(f"{movie['movieId']}: {movie['name']}")
movie_input = input("Enter the Movie ID from the list above: ")

movie_name = None
for movie in allMovies:
       if movie['movieId'] == movie_input:
            movie_name = movie['name']
            break

if movie_name:
    print(f"Reviews for {movie_name} (Movie ID: {movie_input})...")
    found = False

for review in allReviews:
    if review['movieID'] == movie_input:
        print(f"Author: {review['reviewAuthor']}")
        print(f"Date: {review['reviewDate']}")
        print(f"Review: {review['reviewText']}\n")
        found = True

if not found:
        print(f"No reviews found for Movie ID: {movie_input}.")

