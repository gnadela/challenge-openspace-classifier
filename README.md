## Challenge: Open space organizer


# Description
This is my very first python project as part of the AI and Data Science bootcamp with BeCode

The classroom setup at BeCode is an openspace with 6 table of 4 seats. 

This project aims to create a program that could be run everyday to (randomly) assign everybody a seat at a table.


# Installation
The program is organized as follows:

project_root/
├── main.py
└── utils/
    ├── __init__.py
    ├── file_utils.py
    ├── openspace.py
    └── table.py


# Usage
The program allows you to get a list of colleagues from an excel file and place them randomly on the different tables of the open space.

Note: The default setup of the open space is 6 tables of 4 seats → 24 seats.

The program can take a filepath as an argument to load the list of colleagues.
The program distributes randomly the people on the existing tables and says how much seats are left.
The program can deal with the possibility of having to much people in the room.
