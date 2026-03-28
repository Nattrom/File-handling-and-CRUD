import os

FILE_NAME = "database.txt"


# -------------------------------
# FUNCTION: Add Daily Blocker
# -------------------------------
def add_blocker():
    blocker = input("\nEnter your Daily Blocker: ")

    # Save in append mode (does not overwrite existing data)
    with open(FILE_NAME, "a") as file:
        file.write(blocker + "\n")

    print("✅ Blocker saved successfully.\n")


# -------------------------------
# FUNCTION: Fetch All Blockers
# -------------------------------
def fetch_blockers():
    # Check if file exists
    if not os.path.exists(FILE_NAME):
        print("⚠️ No database found. Please add a blocker first.\n")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

        if not lines:
            print("📭 No blockers recorded yet.\n")
        else:
            print("\n📋 Team Daily Blockers:")
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")
            print()


# -------------------------------
# FUNCTION: Overwrite Warning
# -------------------------------
def overwrite_file():
    confirm = input("⚠️ This will overwrite all data. Continue? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            file.write("")  # Clears the file
        print("🧹 File has been cleared.\n")
    else:
        print("❌ Operation cancelled.\n")


# -------------------------------
# MAIN MENU
# -------------------------------
def menu():
    while True:
        print("===== TEAM DAILY STATUS SYSTEM =====")
        print("1. Add Daily Blocker")
        print("2. Fetch All Blockers")
        print("3. Overwrite File (Clear Data)")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_blocker()
        elif option == "2":
            fetch_blockers()
        elif option == "3":
            overwrite_file()
        elif option == "4":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid option. Try again.\n")


# Run program
if __name__ == "__main__":
    menu()


# =====================================================
# 📝 ENGLISH PRACTICE (COMMENT BLOCK)
# =====================================================

"""
Protocol Selection (3-C Rule):

1. I will reach out to the team via Slack because the issue is an immediate blocker and requires quick attention.
2. I would use Email if the problem needs a detailed explanation and documentation for future reference.
3. I would report the issue in Jira if it is a recurring problem that needs to be tracked and assigned to a developer.


Vocabulary Integration Paragraph:

This script demonstrates Persistence by storing user input in a text file that remains available even after the program is closed. 
The Fetch functionality allows the system to retrieve and display all stored blockers efficiently. 
To prevent accidental data loss, the program includes a warning before performing an Overwrite operation. 
If any issue occurs, the user can Reach out to the team using appropriate communication channels.
"""