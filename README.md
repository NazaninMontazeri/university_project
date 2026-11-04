
# 🎓 University Management System

A comprehensive desktop application for managing university operations, built with Python and Tkinter using the MVC (Model-View-Controller) architectural pattern.

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#️-architecture)
- [Technologies Used](#️-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Modules](#-modules)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Support](#-support)

---

## ✨ Features

### Core Functionalities

- 👥 **Student Management:** Register and manage student records.
- 👨‍🏫 **Professor Management:** Manage professors, their salaries, and assigned courses.
- 📚 **Course Management:** Create and manage university courses, including names, units, and codes.
- 📝 **Enrollment Management:** Process and track student course selections with data validation.
- 💯 **Score Management:** Manage student scores, validate submissions, and track pass/fail results.

### User Interface

- 🎨 Modern and clean Graphical User Interface built with Tkinter.
- 📊 Data tables with vertical scrollbar support.
- ✨ Consistent button layouts and user-friendly navigation.
- 🔄 Select and populate functionality across all views.

### Data Management

- ✅ Input validation for all fields.
- 💾 File-based data persistence using Python's `pickle` module.
- 📝 Business Logic layer to prevent duplicate entries and invalid data.

---

## 🏗️ Architecture

This project follows the **MVC (Model-View-Controller)** architectural pattern, combined with separate Business Logic and Data Access layers.

```text
┌─────────────────────┐
│        View         │
│     UI Layer        │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│     Controller      │
│  Request Handling   │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│    Business Logic   │
│ Rules & Validation  │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│     Data Access     │
│   Data Operations   │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│      Database       │
│   File Storage      │
│      (Pickle)       │
└─────────────────────┘
```

### Architecture Layers

- **View:** Provides the graphical interface and handles user interactions.
- **Controller:** Connects the views to the application logic.
- **Business Logic:** Handles application rules, data processing, and validation.
- **Data Access:** Performs CRUD operations and manages data storage.
- **Database:** Stores application data using file-based storage.

---

## 🛠️ Technologies Used

- **Programming Language:** Python 3.x
- **GUI Framework:** Tkinter
- **Data Storage:** Pickle (File-based storage)
- **Architecture:** MVC Pattern
- **Testing:** Python's built-in `unittest` module

---

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- Git

### Setup Steps

**1. Clone the repository:**

```bash
git clone https://github.com/yourusername/university_project.git
```

**2. Navigate to the project directory:**

```bash
cd university_project
```

**3. Run the application:**

```bash
python main.py
```

No external Python packages are required if Python and Tkinter are already installed.

---

## 🚀 Usage

### Start the Application

Run the following command:

```bash
python main.py
```

The application opens with the main panel. Use the available buttons to navigate between different management modules.

### Main Modules

Each module can be accessed independently from the main panel:

- `student_view.py` - Student Management
- `professor_view.py` - Professor Management
- `lesson_view.py` - Course Management
- `select_lesson_view.py` - Enrollment Management
- `score_view.py` - Score Management

### Main Operations

- **Select:** Click on a row in the table to select a record and view its details.
- **Save:** Add a new record.
- **Reset:** Clear the form and refresh the table.
- **Submit:** Process an action, such as submitting a student score.

---

## 📁 Project Structure

```text
university_project/
│
├── main.py                   # Main application entry point
├── README.md                 # Project documentation
│
├── model/                    # Data models
│   ├── person.py
│   ├── student.py
│   ├── professor.py
│   ├── lesson.py
│   ├── score.py
│   └── select_lesson.py
│
├── business_logic/           # Business Logic Layer
│   ├── student_bl.py
│   └── professor_bl.py
│
├── view/                     # User Interface
│   ├── student_view.py
│   ├── professor_view.py
│   ├── lesson_view.py
│   ├── select_lesson_view.py
│   └── score_view.py
│
├── controller/               # Controller Layer
│   ├── student_controller.py
│   ├── professor_controller.py
│   ├── lesson_controller.py
│   ├── select_lesson_controller.py
│   └── score_controller.py
│
├── data_access/              # Data Access Layer
│   └── data/
│       ├── student_da.py
│       ├── professor_da.py
│       ├── lesson_da.py
│       ├── score_da.py
│       └── select_lesson_da.py
│
├── tools/                    # Utilities
│   ├── validators/
│   └── validation.py
│
└── test/                     # Unit Tests
    ├── person_test.py
    ├── student_test.py
    ├── professor_test.py
    ├── lesson_test.py
    ├── score_test.py
    └── select_lesson_test.py
```

---

## 📚 Modules

### Entities

- **Person:** Base entity for personal information.
- **Student:** Stores student details and course enrollment information.
- **Professor:** Stores professor details, salary, and assigned courses.
- **Lesson:** Represents university courses with unit counts and codes.
- **Score:** Stores student scores and pass/fail evaluation.
- **SelectLesson:** Represents the relationship between a student, a professor, and a course.

### UI Components

- **Views:** Custom Tkinter windows with Treeview tables and form layouts.
- **Data Access (DA):** Handles CRUD operations and `.dat` file storage.

---

## 👥 Contributing

Contributions and suggestions for improving this project are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes:

```bash
git commit -m "Add some AmazingFeature"
```

4. Push your branch:

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request.

### Code Style

- Follow the PEP 8 style guide.
- Add comments for complex logic.
- Write unit tests for new features.
- Maintain consistency with the MVC architecture.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

## 🙏 Acknowledgments

Special thanks to everyone who contributed to this project.

---

## 📞 Support

For support or questions, please open an issue in the GitHub repository.

---

**Built with ❤️ by Nazanin Montazeri**