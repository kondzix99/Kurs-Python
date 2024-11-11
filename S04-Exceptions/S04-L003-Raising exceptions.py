import datetime as dt
from math import expm1


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("<{}>:<{}>".format(trip.symbol, e))
            except Exception as e:
                list_of_errors.append("<{}>:<{}>".format(trip.symbol, e))

        if len(list_of_errors) > 0:
            raise Exception("The list of trips has errors: <{}>".format(list_of_errors))
        else:
            print("the offer will be published...")


trips = [
    Trip('IT-VNC', '', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 30))
]

try:
    print("Beginning of checking trips")
    Trip.publish_offer(trips)
except Exception as e:
    print("ERROR APPEND DURING PUBLISHING_OFFER FUNCTION: {}".format(e))
    print('THE OFFER CANNOT BE PUBLISHED')