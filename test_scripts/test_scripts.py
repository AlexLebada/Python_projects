import re

def print_people(*people):
    for person in people:
        print("This person is", person)


if 1==0:
    value = 5

    if value == 5:
        print("yes")
    elif value == 3:
        print("n")
    else:
        print("non")

run = True
current = 1

while run and 1==0:
    if current == 50:
        run = False
    else:
        current += 1


string = "'I AM NOT YELLING' she said"

new = re.sub('[A-Z]', '[a-z]',string)
print(new)
