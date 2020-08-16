# Create list of fruits.
# 1. Iterate it in 3 different way


fruits = ['cherry', 'strawberry', 'apple', 'banana', 'kiwi', 'jackfruit']

print('Iteration Option One')
for fruit in fruits:
    print(fruit)

print('\nIteration Option Two')
x = 0
while x < len(fruits):
    print(fruits[x])
    x += 1

print('\nIteration Option Three')
itr = iter(fruits)
item = next(itr)

while True:
    try:
        print(next(itr))

    except StopIteration:
        break


# 2. Find if there is an "apple" in the list

def does_contain_apple(list):
    for element in list:
        if element == 'apple':
            return True
    return False


result = does_contain_apple(fruits)
print('Does return apple :', result)


# 3. Find index of the "apple"
def index_of_apple(list):
    try:
        print('Index of apple is: ', list.index('apple'))
    except ValueError:
        print('Apple not contained in list')


index_of_apple(fruits)

# 4. Find how many times "apple" is in the list
fruits_two_apples = ['cherry', 'strawberry', 'apple', 'banana', 'kiwi', 'jackfruit', 'apple']
fruits_no_apples = ['cherry', 'strawberry', 'banana', 'kiwi', 'jackfruit']


def count_apple(list):
    count = 0
    for element in list:
        if element == 'apple':
            count += 1
    return count


print('This list has ', count_apple(fruits_two_apples), ' apples')
print('This list has ', count_apple(fruits_no_apples), ' apples')
