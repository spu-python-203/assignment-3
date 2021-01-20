import random
import string


def create_password():
    """
    Create a random password.
    """
    line = []
    for i in range(random.randint(1, 10)):
        line.append(random.choice(string.digits))

    for i in range(random.randint(5, 10)):
        character = random.choice(string.printable)
        if character in ' \t\n\r\x0b\x0c\\':
            continue
        line.append(character)

    random.shuffle(line)

    return ''.join(line)


def create_passwords_file(filename, length):
    """
    Create a file and add passwords in each line.
    """
    with open(filename, 'w+') as handle:
        n = 0
        while n <= length:
            handle.write(create_password() + '\n')
            n += 1


if __name__ == "__main__":
    """
    Main entry point of the program. Creates a passwords 
    file in current working directory.
    """
    create_passwords_file('passwords.txt', 50)
    print('File generated with 50 new passwords.')
