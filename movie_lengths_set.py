def exact_length_flight(flight_length, movie_lengths):
    movie_lengths_seen = set()
    for movie in movie_lengths:
        match = flight_length - movie
        if match in movie_lengths_seen:
            return True
        movie_lengths_seen.add(movie)


print("test")
