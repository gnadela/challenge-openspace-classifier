import random
from .table import Table

class Openspace:
    """
    Represents an open space with multiple tables.
    """

    def __init__(self, number_of_tables: int = 6):
        """
        Initializes an Openspace object with the specified number of tables.

        :param: number_of_tables (int): The number of tables in the open space.
        """
        self.tables = [Table() for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def organize(self, names: list[str]):
        """
        Organizes colleagues randomly at the tables in the open space.

        :param: names (List[str]): The list of colleagues' names to be organized.
        """
        random.shuffle(names)
        index = 0
        for table in self.tables:
            while table.has_free_spot() and index < len(names):
                table.assign_seat(names[index])
                index += 1

    def display(self):
        """
        Displays the configuration of the open space, including tables and occupants.
        """
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}:")
            for seat in table.seats:
                print(seat)
            print()

    def store(self, filename: str):
        """
        Stores the configuration of the open space in a file.

        :param: filename (str): The name of the file to store the configuration.
        """
        with open(filename, 'w') as file:
            for i, table in enumerate(self.tables, start=1):
                file.write(f"Table {i}:\n")
                for seat in table.seats:
                    file.write(str(seat) + '\n')
                file.write('\n')





