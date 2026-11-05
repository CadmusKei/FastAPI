def greet(username, account_age, fav_colour):
    print(f"{username}'s account is {account_age} years old. Their fav colour is: {fav_colour}")
    

user = {
    "username": "Cadmus",
    "account_age": 15,
    "fav_colour": "Green"
}

greet(**user)

# This wont run since its missing the paramters user has
# print(**user)