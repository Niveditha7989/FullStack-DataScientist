import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from .env
load_dotenv()

# Get Supabase credentials
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

sb: Client = create_client(url, key)

from datetime import datetime


def borrow_book(member_id, book_id):
    try:
        # Step 1: Check current stock
        stock_resp = sb.table("books").select("stock").eq("book_id", book_id).single().execute()
        book = stock_resp.data

        if not book:
            print("Book not found.")
            return

        if book["stock"] < 1:
            print(" Book not available (out of stock).")
            return

        # Step 2: Decrease stock by 1
        new_stock = book["stock"] - 1
        stock_update = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()

        if not stock_update.data:
            print("Failed to update stock.")
            return

        # Step 3: Insert into borrow_records
        borrow_data = {
            "member_id": member_id,
            "book_id": book_id,
            "borrow_date": datetime.now().isoformat(),
            "return_date": None
        }

        borrow_resp = sb.table("borrow_records").insert(borrow_data).execute()

        if borrow_resp.data:
            print(f" Borrowed successfully. Book ID {book_id} | Member ID {member_id}")
        else:
            # Rollback stock if borrow insert fails
            sb.table("books").update({"stock": book["stock"]}).eq("book_id", book_id).execute()
            print(" Failed to record borrow. Rolled back stock.")

    except Exception as e:
        print(" Error during borrow operation:", e)

def main():
    print("\n=== Borrow Book ===")
    try:
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID to borrow: "))
        borrow_book(member_id, book_id)
    except ValueError:
        print("Invalid input. IDs must be integers.")

if __name__ == "__main__":
    main()
