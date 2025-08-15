# main.py
import sqlite3
from db_config import create_database

def register_complaint():
    name = input("\nEnter your name: ")
    email = input("Enter your email: ")
    complaint = input("Describe your complaint: ")

    conn = sqlite3.connect('rock.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO complaints (name, email, complaint)
        VALUES (?, ?, ?)
    ''', (name, email, complaint))

    complaint_id = cursor.lastrowid
    print(f"\n✅ Complaint registered successfully!")
    print(f"Your Complaint ID: {complaint_id}")

    conn.commit()
    conn.close()

def track_complaint():
    complaint_id = input("\nEnter Complaint ID: ")

    conn = sqlite3.connect('rock.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id, name, email, complaint, status
        FROM complaints
        WHERE id = ?
    ''', (complaint_id,))

    complaint = cursor.fetchone()
    conn.close()

    if complaint:
        print("\n--- Complaint Details ---")
        print(f"ID: {complaint[0]}")
        print(f"Name: {complaint[1]}")
        print(f"Email: {complaint[2]}")
        print(f"Complaint: {complaint[3]}")
        print(f"Status: {complaint[4]}")
    else:
        print("\n❌ Complaint not found.")

def main_menu():
    print("\n===== ROCK - Register Online Crime in Kochi =====")
    print("1. Register a Complaint")
    print("2. Track Complaint")
    print("3. Exit")

    choice = input("\nSelect an option (1/2/3): ")

    if choice == '1':
        register_complaint()
    elif choice == '2':
        track_complaint()
    elif choice == '3':
        print("\nThank you for using ROCK Portal!")
        exit()
    else:
        print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    create_database()  # Ensure database exists
    while True:
        main_menu()
