import csv

def read_colleagues(filepath):
    """
    Read colleague names from a CSV file.

    :param: filepath (str): The path to the CSV file.

    :return: list: A list of colleague names.
    """
    colleagues = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    colleagues.append(row[0].strip())  # Assuming the names are in the first column
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    return colleagues

def write_to_file(filename, data):
    """
    Write data to a file.

    :param: filename (str): The name of the file to write to.
    :data (list): The data to write to the file.
    """
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(f"{item}\n")
        print(f"Data written to '{filename}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

