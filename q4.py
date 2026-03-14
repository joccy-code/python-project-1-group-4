total_price = 0
total_ticket = 0
count = 0

movie_list = [
    {"title": "TEENS", "showtimes": "1:30hr", "seat_price": 200},
    {"title": "TIME", "showtimes": "1:40hr", "seat_price": 300},
    {"title": "PANTHER", "showtimes": "1:45hr", "seat_price": 400},
    {"title": "THE ROCK", "showtimes": "1:35hr", "seat_price": 500},
    {"title": "FIRE", "showtimes": "1:50hr", "seat_price": 600},
]

print("\nHere are available movies with their details\n")

for movie in movie_list:
    print(movie["title"], movie["showtimes"], movie["seat_price"])

while True:

    user_movie = input("\nChoose a movie: ").upper()
    no_ticket = int(input("Enter number of tickets: "))

    movie_found = False

    for movie in movie_list:

        if user_movie == movie["title"]:

            price = no_ticket * movie["seat_price"]
            total_price += price
            total_ticket += no_ticket
            count += 1

            print(f"Booking confirmed. Cost: {price}")

            movie_found = True
            break

    if not movie_found:
        print("Please enter a correct movie name.")

    user_answer = input("\nDo you want to book another movie? (yes/no): ").lower()

    if user_answer == "no":
        print("\n----- Booking Summary -----")
        print(f"Total price: {total_price}")
        print(f"Total tickets booked: {total_ticket}")
        print(f"Total number of bookings: {count}")
        break
