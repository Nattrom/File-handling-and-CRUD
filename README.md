# 🧠 Team Daily Status System

## Description
This Python program allows users to store and manage daily blockers using a text file (`database.txt`).  
It demonstrates data persistence, meaning the information remains saved even after the program is closed.

## Features
- Add a blocker (append mode `a`)
- Fetch all blockers (read mode `r`)
- Overwrite file with confirmation (write mode `w`)
- File existence validation

## Project Structure
week3_project/
- database.txt
- persistence_log.py
- README.md

## How to Run
1. Open terminal  
2. Navigate to the folder:
   cd week3_project  
3. Run the program:
   python persistence_log.py  

## Key Concepts
- Persistence: data is saved permanently  
- Fetch: retrieve stored data  
- Overwrite: replace file content with warning  
- File handling using `with open()`

## Author
Systems Engineering Student
