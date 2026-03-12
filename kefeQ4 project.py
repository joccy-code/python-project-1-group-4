# # 4)	 Movie Ticket Booking Simulation
# -	Simulate a movie theater booking system that:
# •	Shows a list of available movie titles, showtimes, and seat prices.
# •	Asks the user to choose a movie and number of tickets.
# •	Confirms total price and asks if they want to book another movie.
# •	Ends when they say "no" and displays total bookings and cost.
#	write a program for Movie Ticket Booking Simulation
# •	Shows a list of available movie titles,
# •	Calculates the total price based on the selected movie and number of tickets,
# •	Provides a confirmation message with the total price.
movie_titles =     showtimes = {
        "Avator": "2:00 PM, 5:00 PM, 8:00 PM",
        "Zootopia": "1:00 PM, 4:00 PM, 7:00 PM",
        "Blockbusters & supperheroes": "3:00 PM, 6:00 PM, 9:00 PM",
        "king of king": "2:30 PM, 5:30 PM, 8:30 PM",
        "Dreams": "1:30 PM, 4:30 PM, 7:30 PM",
        "David": "2:15 PM, 5:15 PM, 8:15 PM",
        "Sarahs' oil": "3:15 PM, 6:15 PM, 9:15 PM",
        "Dogman": "2:45 PM, 5:45 PM, 8:45 PM",
        "Pets on a train": "1:45 PM, 4:45 PM, 7:45 PM",
        "Shelter": "2:00 PM, 5:00 PM, 8:00 PM",
        "Scream 7": "3:00 PM, 6:00 PM, 9:00 PM",
        "The last of us": "1:30 PM, 4:30 PM, 7:30 PM",
        "One Battle After Another": "2:15 PM, 5:15 PM, 8:15 PM",
    }
seat_prices = {
        "Avator": 12,
        "Zootopia": 8,
        "Blockbusters & supperheroes": 12,
        "king of king": 10,
        "Dreams": 8,
        "David": 12,
        "Sarahs' oil": 12,
        "Dogman": 6,
        "Pets on a train": 8,
        "Shelter": 10,
        "Scream 7": 7,
        "The last of us": 10,
        "One Battle After Another": 8,
    }
total_price = 0
tax_amount = total_price * 0.08
subtotal_price = total_price
while True:
    print("Available movies_titles:")
    print("showtimes, and seat prices:")
    for movie in movie_titles:
        print(f"- {movie} (${seat_prices[movie]}) - Showtimes: {showtimes[movie]} ")
    movie = input("Enter the movie title (or type 'done' to finish): ")
    if movie.lower() == "done":
        break
    if movie in movie_titles:
        quantity = int(input(f"Enter the number of tickets for {movie}: "))
        total_price += seat_prices[movie] * quantity
    else:
        print("Movie not found in the list. Please try again.")
print(f"The total price for your movie tickets is: ${total_price:.2f}.")
movie = input("do you want to book another movie (or type 'done' to finish): ")
print(" your booking has been confirmed. Enjoy your movie!")
print(f"The total price for your movie tickets is: ${total_price:.2f}.")
print(f"The subtotal price for your movie tickets is: ${subtotal_price:.2f}.")
print(f"The tax amount for your movie tickets is: ${tax_amount:.2f}.")