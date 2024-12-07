import random
import string


def random_password(length=10):
    character = string.ascii_lowercase+string.digits + \
        string.ascii_uppercase+string.punctuation
    for x in range(length):
        password = ''.join(random.choice(character) for _ in range(12))
        print(password)
        with open('new.txt', 'a',) as file:
            file.write(password+'\n')


random_password()
