from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the items
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    is_in_stock: bool

# Sample data to demonstrate functionality
fake_items_db = {
    1: {"name": "Item One", "description": "This is the first item.", "price": 10.99, "is_in_stock": True},
    2: {"name": "Item Two", "description": "This is the second item.", "price": 20.49, "is_in_stock": False},
    3: {"name": "Item Three", "description": "This is the third item.", "price": 15.75, "is_in_stock": True},
}

# Define a POST endpoint to create an item
@app.post("/postitems/")
def create_item(item: Item):
    # You can create a new ID dynamically or use a database in a real app
    item_id = max(fake_items_db.keys()) + 1  # Simple way to get next ID
    item_dict = item.dict()  # Convert Pydantic model to a dictionary
    fake_items_db[item_id] = item_dict  # Store the item in the fake database
    print(f"Item created: ID {item_id}, Name: {item.name}")
    return {"item_id": item_id, "item": item_dict}

@app.get("/getitems/{item_id}")
def read_item(item_id: int, q: str = None):
    item = fake_items_db.get(item_id)
    if item is None:
        print(f"Item not found: ID {item_id}")  # Print a message if the item is not found
        raise HTTPException(status_code=404, detail="Item not found")  # Use HTTPException for errors
    
    response = {"item_id": item_id, "item": item}

# Print a message that the item was found
    print(f"Item retrieved: ID {item_id}, Name: {item['name']}")

    # Include the query parameter in the response if provided
    if q:
        response["query"] = q

    return response