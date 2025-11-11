#initial grocery list
grocery_list = ["milk","bread","eggs"]

#Function to add an item to the list
def add_item(item):
    grocery_list.append(item)


# Function to remove the last item from the list
def remove_last_item():
    if grocery_list:
        grocery_list.pop()

# Lambda function to display all items
display_items = lambda: [print(f"Item: {item}") for item in grocery_list]
      
# Recursive function to count total number of characters
def count_characters(items):
    if not items:  # base case
        return 0
    return len(items[0]) + count_characters(items[1:]) 

# --- Test the functions step by step ---
print("Initial Grocery List:")
display_items()

# Add an item
add_item("butter")
add_item("cheese")

print("\nUpdated Grocery List:")
display_items()

# Remove last item
remove_last_item()

print("\nAfter Removing Last Item:")
display_items()

# Bonus: Total character count
total_chars = count_characters(grocery_list)
print(f"\nTotal number of characters in all items: {total_chars}")