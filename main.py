from utils.file_utils import read_colleagues
from utils.openspace import Openspace 

input_file = "new_colleagues.csv"
output_file = "openspace_config.txt"

def main():
    # Load colleagues from the Excel file
    filename = input_file
    colleagues = read_colleagues(filename)

    # Create an openspace with 6 tables
    openspace = Openspace()

    # Organize colleagues in the openspace
    openspace.organize(colleagues)

    # Display the openspace
    openspace.display()

    # Store the openspace configuration
    openspace.store(output_file)

if __name__ == "__main__":
    main()
