from utils.file_utils import read_colleagues
from utils.openspace import Openspace 

def main():
    # Load colleagues from the Excel file
    filename = "new_colleagues.csv"
    colleagues = read_colleagues(filename)

    # Create an openspace with 6 tables
    openspace = Openspace(6)

    # Organize colleagues in the openspace
    openspace.organize(colleagues)

    # Display the openspace
    openspace.display()

    # Store the openspace configuration
    openspace.store("openspace_config.txt")

if __name__ == "__main__":
    main()
