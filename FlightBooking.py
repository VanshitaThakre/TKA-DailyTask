
class Flight:
    def __init__(self, code, source, destination, fare, seats):
        self.code = code
        self.source = source
        self.destination = destination
        self.fare = fare
        self.seats = seats


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def discount(self):
        return 0


class Student(Passenger):
    def discount(self):
        return 10


class Booking:
    def __init__(self, flight, passenger, tickets):
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

    def show_booking(self):
        total = self.flight.fare * self.tickets
        discount = total * self.passenger.discount() / 100

        print("\nBooking Confirmed!")
        print("Passenger:", self.passenger.name)
        print("Flight:", self.flight.code)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Tickets:", self.tickets)
        print("Total Fare:", total)
        print("Discount:", discount)
        print("Final Fare:", total - discount)


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Pune", "Delhi", 4000, 20),
            Flight("MB202", "Mumbai", "Bengaluru", 5000, 25),
            Flight("PN303", "Pune", "Hyderabad", 3500, 15)
        ]
        self.booking = None

    def run(self):
        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                for f in self.flights:
                    print(f.code, f.source, "to", f.destination,
                          "Fare:", f.fare, "Seats:", f.seats)

            elif choice == "2":
                code = input("Enter flight code: ")

                flight = None
                for f in self.flights:
                    if f.code == code:
                        flight = f
                        break

                if flight is None:
                    print("Invalid flight code!")
                    continue

                name = input("Enter passenger name: ")
                if not name.strip():
                    print("Name cannot be empty!")
                    continue

                try:
                    age = int(input("Enter age: "))
                    tickets = int(input("Enter tickets: "))
                except ValueError:
                    print("Enter valid numbers!")
                    continue

                if age <= 0 or tickets <= 0:
                    print("Age and tickets must be greater than zero!")
                    continue

                if tickets > flight.seats:
                    print("Not enough seats!")
                    continue

                kind = input("Regular or Student: ").lower()

                if kind == "student":
                    passenger = Student(name, age)
                elif kind == "regular":
                    passenger = Passenger(name, age)
                else:
                    print("Invalid passenger type!")
                    continue

                flight.seats -= tickets
                self.booking = Booking(flight, passenger, tickets)
                self.booking.show_booking()

            elif choice == "3":
                if self.booking:
                    self.booking.show_booking()
                else:
                    print("No booking found!")

            elif choice == "4":
                print("Thank you for using Flight Booking!")
                break

            else:
                print("Invalid choice!")


system = FlightBookingSystem()
system.run()
