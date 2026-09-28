Start
  |
  v
Display Main Menu
  |
  v
User Selects an Option
  |
  +--> Add Student ------> Store Record
  |
  +--> Display Students -> Show Records
  |
  +--> Search Student ---> Find by Roll Number
  |
  +--> Update Student ---> Modify Existing Record
  |
  +--> Delete Student ---> Remove Record
  |
  +--> Exit -------------> End Program
  |
  v
Return to Main Menu
```

---

## 1. Technologies and Tools Used

| Technology / Tool | Purpose |
|---|---|
| Python | Main programming language |
| Python Lists | Store student records |
| Python Dictionaries | Represent individual student records |
| Functions | Divide the program into logical operations |
| Loops | Maintain the menu and process records |
| Conditional Statements | Handle menu choices and validation |
| Git/GitHub | Recommended for version control and repository submission |

---

## 2. Project Structure

The current project contains:

```text
Student-Management-System/
│
├── SEM1_PROJECT.py
└── README.md
```

### Main Source File

`SEM1_PROJECT.py` contains the complete application and includes the following logical modules/functions:

```text
add_student()
display_students()
search_student()
update_student()
delete_student()
```

The main menu controls the overall workflow.

---

## 3. Installation and Setup

### Prerequisites

Install Python 3.x on your computer.

Verify the installation using:

```bash
python --version
```

or:

```bash
python3 --version
```

### Clone the Repository

If the project is uploaded to GitHub:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Student-Management-System
```

### Run the Program

Execute:

```bash
python SEM1_PROJECT.py
```

On some systems, use:

```bash
python3 SEM1_PROJECT.py
```

---

## 4. How to Use the System

After starting the program, the following menu is displayed:

```text
==============================
     STUDENT MANAGEMENT
==============================
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==============================
```

Enter the number corresponding to the required operation.

### Example

To add a student:

```text
Enter your choice: 1

--- Add Student ---
Enter roll number: 101
Enter student name: Rahul
Enter age: 18
Enter course: B.Tech
Enter marks: 85
```

The system then confirms:

```text
Student added successfully!
```

---

## 5. Data Representation

Each student is represented using a Python dictionary:

```python
{
    "roll_no": "101",
    "name": "Rahul",
    "age": 18,
    "course": "B.Tech",
    "marks": 85.0
}
```

All student dictionaries are stored in the `students` list.

This provides a simple in-memory structure for performing CRUD operations.

---

## 6. Non-Functional Requirements

### 6.1 Usability

The system uses a simple menu-driven interface so that users can select operations easily.

### 6.2 Performance

For the current in-memory implementation, operations are lightweight and suitable for a small number of student records.

### 6.3 Reliability

The system checks whether a requested student exists before performing search, update, or delete operations.

### 6.4 Maintainability

The program separates major operations into individual functions, making the code easier to understand and modify.

### 6.5 Error Handling

The system handles situations such as:

- Searching for a non-existent student
- Updating a non-existent student
- Deleting a non-existent student
- Selecting an invalid menu option
- Empty student list

> Numeric inputs such as age and marks currently rely on valid user input and could be strengthened with additional exception handling.

---

## 7. Technical Design

### Architecture

The current application follows a simple procedural, menu-driven architecture:

```text
User
  |
  v
Command-Line Menu
  |
  v
Function Selection
  |
  +--> Add
  +--> Display
  +--> Search
  +--> Update
  +--> Delete
  |
  v
In-Memory Student List
```

### Storage

No external database is currently used. Student records are stored temporarily in a Python list and are lost when the program terminates.

---

## 8. Testing Instructions

The application can be manually tested using the following cases:

| Test Case | Expected Result |
|---|---|
| Add a valid student | Student is added successfully |
| Display students after adding | Student information is displayed |
| Search using an existing roll number | Matching student is displayed |
| Search using an unknown roll number | `Student not found.` is displayed |
| Update an existing student | Selected information is updated |
| Delete an existing student | Student is removed |
| Delete an unknown student | `Student not found.` is displayed |
| Select an invalid menu option | Invalid-choice message is displayed |
| Display when no students exist | `No students found.` is displayed |

---

## 9. Limitations

The current version has the following limitations:

1. Data is stored only in memory.
2. Student records are lost when the program exits.
3. There is no graphical user interface.
4. There is no database integration.
5. Automated unit tests are not included.
6. The current implementation is contained in one Python source file rather than a 5–10 file modular project structure.
7. Input validation can be expanded to handle invalid numeric input more robustly.

---

## 10. Future Enhancements

The project can be extended by:

- Adding SQLite or another database for permanent storage.
- Adding login and user authentication.
- Creating a graphical user interface.
- Adding stronger input validation and exception handling.
- Adding sorting and filtering by marks, course, or age.
- Generating student performance reports.
- Adding automated unit tests.
- Splitting the application into multiple modules/classes.
- Adding logging and monitoring.
- Deploying the system as a web application.

---

## 11. Git and GitHub

Version control should be used to track project development.

Typical commands:

```bash
git init
git add .
git commit -m "Initial Student Management System"
git branch -M main
git remote add origin <YOUR-GITHUB-REPOSITORY-URL>
git push -u origin main
```

Replace `<YOUR-GITHUB-REPOSITORY-URL>` with the actual GitHub repository URL.

---

## 12. Project Report Artefacts

According to the provided project guidelines, the complete project submission should also document:

- Problem Statement
- Objectives
- Functional Requirements
- Non-functional Requirements
- System Architecture Diagram
- Workflow Diagram
- Use Case Diagram
- Class/Component Diagram, where applicable
- Sequence Diagram
- Database/Storage Design, where applicable
- Design Decisions and Rationale
- Implementation Details
- Screenshots/Results
- Testing Approach
- Challenges Faced
- Learnings and Key Takeaways
- Future Enhancements
- References

---

## 13. References

- VITyarthi – Build Your Own Project: General Project Instructions & Submission Guidelines.
- Python 3 documentation and standard language features used in the implementation.

---

## 14. Author

**Project:** Student Management System  
**Language:** Python  
**Project Type:** Command-Line Application
