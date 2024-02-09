class Seat:
    """
    Class representing a seat in a table.
    """

    def __init__(self):
        """
        Initializes a seat.
        """
        self.free = True
        self.occupant = None

    def set_occupant(self, name: str):
        """
        Sets an occupant to the seat.

        param: name (str): name of the occupant

        return: None
        """
        self.occupant = name
        self.free = False

    def remove_occupant(self) -> str:
        """
        Removes the occupant from the seat.

        return: (str) Name of the occupant removed.
        """
        occupant_name = self.occupant
        self.occupant = None
        self.free = True
        return occupant_name

    def __str__(self):
        """
        Returns a string representation of the Seat.
        """
        status = "Free" if self.free else f"Occupied by {self.occupant}"
        return f"Seat: {status}"

class Table:
    """
    Class representing a table in the openspace.
    """

    def __init__(self, capacity: int = 4):
        """
        Initializes a table with a given capacity.

        :param: capacity (int): Capacity of the table (number of seats).

        :return: None
        """
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self) -> bool:
        """
        Checks if the table has a free spot.

        :return: (bool) True if there is a free spot, False otherwise.
        """
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name: str):
        """
        Assigns a seat to a person.

        :param: name (str): name of the person

        :return: None
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break

    def left_capacity(self) -> int:
        """
        Calculates the number of free seats left on the table.

        :return: (int) number of free seats
        """
        return sum(1 for seat in self.seats if seat.free)

    def display(self):
        """
        Displays the configuration of the table.
        """
        for seat in self.seats:
            print(seat)

    def __str__(self):
        """
        Returns a string representation of the Table.
        """
        return f"Table with {self.capacity} seats ({self.left_capacity()} available)"
