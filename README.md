# Open Space Classifier


## Overview

The Open Space Classifier is a Python program designed to randomly assign people to spots in an open space environment. It helps efficiently distribute people across available tables while ensuring a fair and random allocation.

## Features

- Random assignment of people to seats
- Support for loading colleagues' names from an Excel file
- Handling of cases where there are more people than available seats

## Getting Started
### Prerequisites
- Python 3.x installed on your system
- Required Python packages installed:
    - `csv` module (included in Python standard library)
    - `random` module (included in Python standard library)

### Installation

Clone the repository to your local machine:
```bash
git clone https://github.com/gnadela/challenge-openspace-classifier
```

Navigate to the project directory:
```bash
cd challenge-openspace-classifier
```

### Usage

Run the main script `main.py` to launch the organizer:

```bash
python main.py
```

The current version of the program loads the list of names from the provided `new_colleagues.csv` file. It displays the output on the terminal and stores it in a text file called `openspace_config.txt`.

