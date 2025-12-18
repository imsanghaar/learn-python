# Dictionaires methods

# Dictionary
user = {
    "name": "Sanghaar",
    "age": 17, # type: ignore
    "email": "imamsanghaar@gmail.com"
}


# Dictionary methods:
# 1. .items -> returns a list of (keys, value) tuples
# print("user items: ",user.items()) # This will print the whole items inside the dictionary [ dict_items([('name', 'Sanghaar'), ('age', 17), ('email', 'imamsanghaar@gmail.com')])]
# 2. .keys() ->  returns a list of containing dictionary's key
# print("user keys: ", user.keys()) #  -> This will print the keys like("names", "age", "email")
# 3.  .values() -> returns a list of values of keys
# print("user values: ", user.values())  #  -> This will print the values of the keys
# 4.  .update({}) -> updates the dictionary with supplied key-pair
# user.update({"Marks": 90})
# print(user)
# 4.  .get("") -> returns the value of the specified keys(and the value is returned like "sanghaar")
print(user.get("name")) # -> returns none if the given arguemnt is not in the dict:
# print(user["name"])     # -> returns error id the given argument is not in the dictionary




