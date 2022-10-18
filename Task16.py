# Declare a dictionary with any key-value pair of items/elements

# Print the dictionary in console

# Update the dictionary with two different key-value pair items

# Print the dictionary in console again

persons = {
    "body": "Skinny",
    "height": 5.9,
    "color": "Black"
}
print("dictionary", persons)

body = persons.get("body")
print(body)

Update = persons.update({"eye": "Brown", "hair": "long braids", "sex": "male"})
print("Update:", persons)