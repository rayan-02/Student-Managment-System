# Student Management System

A simple Python-based Student Management System that uses Object-Oriented Programming (OOP) and JSON file handling to manage student records.

## Features

- Add a student
- View all students
- Search for a student by roll number
- Update student information
- Delete a student
- Save data to a JSON file
- Load saved data automatically

## Requirements

- Python 3.x

## Project Structure

```
Student-Management-System/
├── main.py
├── students.json
└── README.md
```

## How to Run

```bash
python main.py
```

## Data Storage

Student records are stored in `students.json`. Data is automatically loaded when the program starts and saved after any changes.

## Student Information

Each student record contains:

- Name
- Roll Number
- Age
- GPA

## Note

Change the following line in `add_student()`:

```python
name = input("Enter Student Name: ").capitalize
```

to:

```python
name = input("Enter Student Name: ").capitalize()
```

This ensures the student's name is properly capitalized.

## License

This project is for learning and educational purposes.