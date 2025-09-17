import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from .env
load_dotenv()

# Get Supabase credentials
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

sb: Client = create_client(url, key)


def delete_member(member_id):
    try:
        # Check if member has any borrow records
        borrow_resp = sb.table("borrow_records").select("*").eq("member_id", member_id).execute()
        if borrow_resp.data:
            print(f" Cannot delete member {member_id}: They have borrowed books.")
            return

        # Proceed to delete
        del_resp = sb.table("members").delete().eq("member_id", member_id).execute()
        if del_resp.data:
            print(f" Member {member_id} deleted successfully.")
        else:
            print(" Member not found.")
    except Exception as e:
        print("Error deleting member:", e)


def delete_book(book_id):
    try:
        # Check if book has been borrowed (and not returned)
        borrow_resp = sb.table("borrow_records").select("*").eq("book_id", book_id).is_("return_date", None).execute()
        if borrow_resp.data:
            print(f"Cannot delete book {book_id}: It is currently borrowed.")
            return

        # Proceed to delete
        del_resp = sb.table("books").delete().eq("book_id", book_id).execute()
        if del_resp.data:
            print(f" Book {book_id} deleted successfully.")
        else:
            print(" Book not found.")
    except Exception as e:
        print("Error deleting book:", e)


def main():
    print("\n=== Delete Operations ===")
    print("1. Delete Member (only if no borrowed books)")
    print("2. Delete Book (only if not currently borrowed)")

    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        try:
            member_id = int(input("Enter Member ID to delete: "))
            delete_member(member_id)
        except ValueError:
            print(" Invalid member ID.")
    elif choice == "2":
        try:
            book_id = int(input("Enter Book ID to delete: "))
            delete_book(book_id)
        except ValueError:
            print(" Invalid book ID.")
    else:
        print(" Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
