# Task -> DIctionary

user_data = {
    "name":"Ali",
    "age": 17,
    "phone_num":"1344123835",
    "email":"ali123@gmail.com",
    "square": lambda num1: num1 * num1 ,
    "Fruit": ["Apple", "Orange", "Banana"]
}

print("User Data: ")
print("User name: ", user_data["name"])
print("User age: ", user_data["age"])
print("User email: ", user_data["email"])
print("User phone number: ", user_data["phone_num"])
print("User Fruit list: ", user_data["Fruit"])
print("Square of 5: ", user_data["square"](5))