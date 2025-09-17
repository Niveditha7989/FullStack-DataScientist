import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def update_product(name, price, stock):
    payload = {"price": int(price), "stock": int(stock)}
    resp = sb.table("products").update(payload).eq("name", name).execute()
    return resp.data

if __name__ == "__main__":
    name = input("Enter the product name to update: ").strip()
    price = input("Enter new price: ").strip()
    stock = input("Enter new stock: ").strip()

    updated = update_product(name, price, stock)
    print("Updated:", updated)