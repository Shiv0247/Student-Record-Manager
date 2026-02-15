# Simple GitHub Project: Student Record Manager (Python)

## Project Idea

Create a basic Python program to store and view student names and marks. This is easy, useful, and perfect for a first GitHub project.

## What This Project Shows

* Basic Python skills
* Input/output handling
* Lists and simple logic

## Features

* Add a student name
* Add marks
* View all student records

## Code (main.py)

```python
students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        students.append((name, marks))
        print("Student added!")

    elif choice == "2":
        print("\nStudent Records:")
        for s in students:
            print("Name:", s[0], "| Marks:", s[1])

    elif choice == "3":
        break

    else:
        print("Invalid choice")

