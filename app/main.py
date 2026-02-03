from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    CinemaBar()
    for customer_data in customers:
        current_customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(current_customer.food, current_customer)

    hall_num = CinemaHall(hall_number)
    cleaning_stuff = Cleaner(cleaner)

    customer_instances = [Customer(c["name"], c["food"]) for c in customers]

    hall_num.movie_session(movie, customer_instances, cleaning_stuff)
