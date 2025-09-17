import os
from supabase import create_client, Client 
from dotenv import load_dotenv  

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# --- 1. List Available Books ---
def list_available_books():
    try:
        response = sb.table("books").select("*").gte("stock", 1).execute()
        return response.data
    except Exception as e:
        print("Error listing available books:", e)
        return []

# --- 2. Search Books ---
def search_books(query):
    try:
        response = sb.table("books").select("*").or_(
            f"title.ilike.%{query}%,author.ilike.%{query}%,category.ilike.%{query}%"
        ).execute()
        return response.data
    except Exception as e:
        print("Error searching books:", e)
        return []

# --- MAIN MENU ---
def main():
    while True:
        print("\n--- Library Menu ---")
        print("1. List available books")
        print("2. Search books by title/author/category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            books = list_available_books()
            if books:
                print("\nAvailable Books:")
                for book in books:
                    print(f"{book['title']} | {book['author']} | {book['category']} | Stock: {book['stock']}")
            else:
                print("No available books found.")

        elif choice == "2":
            query = input("Enter title, author, or category to search: ").strip()
            results = search_books(query)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"{book['title']} | {book['author']} | {book['category']} | Stock: {book['stock']}")
            else:
                print("No matching books found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter 1 to 4.")

if __name__ == "__main__":
    main()
