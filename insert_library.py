# insert_library.py

import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from .env
load_dotenv()

# Get Supabase credentials
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

sb: Client = create_client(url, key)

def add_members(name, email):
    payload = {"name": name, "email": email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data

def add_books(title, author, category, stock):
    payload = {
        "title": title,
        "author": author,
        "category": category,
        "stock": int(stock)
    }
    resp = sb.table("books").insert(payload).execute()
    return resp.data

if __name__ == "__main__":
    # Insert member
    name = input("Enter name of person: ").strip()
    email = input("Enter email: ").strip()

    try:
        created = add_members(name, email)
        print("Inserted member:", created)
    except Exception as e:
        print("Failed to insert member:", e)

    # Insert book
    title = input("Enter the book title: ").strip()
    author = input("Enter the book author: ").strip()
    category = input("Enter the book category: ").strip()
    stock = input("Enter the book stock: ").strip()

    try:
        created_book = add_books(title, author, category, stock)
        print("Inserted book:", created_book)
    except Exception as e:
        print("Failed to insert book:", e)
