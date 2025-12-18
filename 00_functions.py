# Functions
def greet():
    print('Hello World!')
    print( "Open Door!" )

greet()  # calling the function


def sum( num1, num2 ): # parameters
    print(num1+num2)

sum(num1 = 100, num2 = 200) # passing arguments by keyword
sum(100,200) # passing arguments by position



def catch(obj = '⚽'):
    print( f'Catched! {obj}')
#     return f'Catched! {obj}'

bag = catch('💻')
print(bag)
