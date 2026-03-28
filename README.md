# 🧠 Team Daily Status System (Persistence Project)

## 📌 Description
This project is a Python-based system that allows users to manage daily blockers using file persistence.  
The system stores data in a text file (`database.txt`), ensuring that information remains available even after the program is closed.

---

## 🎯 Objective
To demonstrate the use of:
- File handling in Python (`r`, `w`, `a` modes)
- Data persistence
- CRUD-like operations
- Error handling
- Professional communication practices in English

---

## ⚙️ Features

### 1. Add Daily Blocker
- Prompts the user to enter a blocker.
- Saves the information using **append mode (`a`)**.

### 2. Fetch All Blockers
- Reads and displays all saved blockers.
- Uses a loop to show each entry clearly.

### 3. Overwrite File (Clear Data)
- Warns the user before deleting all data.
- Uses **write mode (`w`)** to reset the file.

### 4. Error Handling
- Checks if the file exists before reading.
- Displays user-friendly messages if no data is found.

---

## 🗂️ Project Structure
