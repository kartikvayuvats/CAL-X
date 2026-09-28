# 🥗 Calorie Tracker

A simple **Python-based Calorie Tracker** that helps users record their meals, monitor daily calorie intake, track nutrition, and manage their daily calorie goals.

This project was developed as part of the **Vityarthi Python Project**.

---

## 📌 Project Overview

The Calorie Tracker is a command-line application designed to make basic calorie and nutrition tracking simple and organized.

Users can:

- Add food and meal information
- View today's meals
- Calculate total daily calorie intake
- View protein, carbohydrates, and fat consumption
- Set a daily calorie goal
- Edit existing meals
- Delete meals
- Store data permanently using JSON files
- Maintain an activity log

---

## 🎯 Objectives

The main objectives of this project are:

1. To create a simple calorie tracking system using Python.
2. To practice modular programming.
3. To store and retrieve data using JSON files.
4. To implement input validation and error handling.
5. To calculate daily calories and nutritional values.
6. To provide users with an easy-to-use command-line interface.

---

## ✨ Features

### 1. Add Food

Users can add a food item along with:

- Food name
- Calories
- Protein
- Carbohydrates
- Fat

The information is stored for future use.

### 2. View Today's Meals

Displays all currently stored meals with their nutritional information.

Example:

```text
--- TODAY'S MEALS ---

Meal 1
----------------------
Food     : Chicken
Calories : 500 kcal
Protein  : 45 g
Carbs    : 0 g
Fat      : 10 g
```

### 3. Daily Calorie Summary

Calculates:

- Total calories consumed
- Daily calorie goal
- Remaining calories

Example:

```text
--- DAILY CALORIE SUMMARY ---

Calories consumed : 1025 kcal
Daily goal        : 2500 kcal
Calories remaining : 1475 kcal
```

### 4. Nutrition Summary

Calculates total:

- Calories
- Protein
- Carbohydrates
- Fat

### 5. Set Calorie Goal

Users can set or update their daily calorie target.

Example:

```text
Enter your daily calorie goal: 2500

✓ Daily calorie goal updated successfully!
```

### 6. Delete Meal

Users can select a meal from the list and permanently remove it.

### 7. Edit Meal

Users can modify the nutritional information of an existing meal.

### 8. Data Persistence

Meal and calorie-goal information is stored using JSON files, allowing data to remain available after the program is closed.

### 9. Input Validation

The project validates user input and prevents invalid values such as negative nutritional values.

### 10. Activity Logging

Important user actions are recorded in `activity.log`.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| JSON | Data storage |
| File Handling | Reading and writing project data |
| Exception Handling | Handling invalid input |
| Modular Programming | Separating project functionality |

---

## 📂 Project Structure

```text
Calorie Tracker/
│
├── main.py
├── food.py
├── calorie_tracker.py
├── nutrition.py
├── storage.py
├── validator.py
├── logger.py
├── activity.log
│
└── data/
    ├── meals.json
    └── settings.json
```

---

## 🧩 Modules

### `main.py`

Controls the main application loop and displays the user menu.

### `food.py`

Handles adding food and storing nutritional information.

### `calorie_tracker.py`

Handles viewing meals and calorie-related operations.

### `nutrition.py`

Calculates daily calorie and nutrition summaries.

### `storage.py`

Handles reading and writing meal and settings data using JSON files.

### `validator.py`

Validates user input such as food names and numerical values.

### `logger.py`

Records important application activities in `activity.log`.

---

## 🔄 Application Flow

```text
             START
               │
               ▼
       Display Main Menu
               │
       ┌───────┼────────┐
       │       │        │
       ▼       ▼        ▼
    Add Food  View     Summary
              Meals      │
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           Calories   Nutrition   Goal
              │          │          │
              └──────────┼──────────┘
                         │
                    Edit / Delete
                         │
                         ▼
                        EXIT
```

---

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your system.

Check the installation:

```bash
python --version
```

### 2. Open the project folder

Open the project in VS Code or a terminal.

### 3. Run the program

```bash
python main.py
```

### 4. Use the menu

```text
========================================
           CALORIE TRACKER
========================================

1. Add Food
2. View Today's Meals
3. View Daily Calorie Summary
4. View Nutrition Summary
5. Set Calorie Goal
6. Delete Meal
7. Edit Meal
8. Exit
```

---

## 🧪 Example Usage

### Adding a meal

```text
Enter your choice: 1

--- ADD FOOD ---

Enter food name: Chicken
Enter calories: 500
Enter protein (g): 45
Enter carbohydrates (g): 0
Enter fat (g): 10

✓ Food added and saved successfully!
```

### Viewing calorie summary

```text
Enter your choice: 3

--- DAILY CALORIE SUMMARY ---

Calories consumed : 1025 kcal
Daily goal        : 2500 kcal
Calories remaining : 1475 kcal
```

### Viewing nutrition

```text
Enter your choice: 4

--- NUTRITION SUMMARY ---

Calories : 1025 kcal
Protein  : 51 g
Carbs    : 65 g
Fat      : 11 g
```

---

## ✅ Validation & Error Handling

The application handles common invalid inputs, including:

- Empty food names
- Invalid numerical input
- Negative calorie values
- Negative nutritional values
- Invalid menu choices
- Invalid meal numbers

The project uses exception handling to prevent the application from terminating unexpectedly because of invalid numerical input.

---

## 💾 Data Storage

The application uses JSON files for lightweight local data storage.

### `meals.json`

Stores information about meals and their nutritional values.

### `settings.json`

Stores application settings such as the daily calorie goal.

This approach keeps the project simple while demonstrating practical file handling.

---

## 📊 Activity Logging

The project maintains an `activity.log` file to record important actions such as:

```text
Food added
Meals viewed
Nutrition summary viewed
Daily calorie summary viewed
Program exited
```

This provides a simple record of application activity.

---

## 🚀 Future Scope

The current project is a command-line application. It can be extended in the future with:

- Graphical User Interface (GUI)
- Web-based interface
- Mobile application
- User accounts
- Database integration
- Food database/API
- Calorie recommendations
- Weight tracking
- Exercise tracking
- Progress charts
- Weekly and monthly reports
- Personalized nutrition recommendations

---

## 🌟 Advantages

- Simple and easy to use
- Lightweight
- Modular code structure
- Persistent data storage
- Input validation
- Nutrition tracking
- Calorie-goal monitoring
- Easy to extend

---

## ⚠️ Limitations

- Currently operates through a command-line interface.
- Food nutritional values must be entered manually.
- Data is stored locally in JSON files.
- It does not currently provide personalized medical or dietary recommendations.
- No user authentication is implemented.

---

## 🎓 Learning Outcomes

Through this project, the following Python concepts were practiced:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- Modules and imports
- File handling
- JSON
- Exception handling
- Input validation
- Modular programming

---

## 👨‍💻 Project

**Project:** Calorie Tracker  
**Program:** Vityarthi Python Project  
**Language:** Python  
**Type:** Command-Line Application

---

## 📜 License

This project is created for educational purposes as part of the Vityarthi project.