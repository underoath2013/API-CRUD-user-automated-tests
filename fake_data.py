from faker import Faker
from random import randint, choice
import string

faker = Faker('en_US')


class FakeData:
    @staticmethod
    def list_generator(data):
        random_index = randint(0, len(data)-1)
        random_data = data[random_index]
        return random_data

    @staticmethod
    def name():
        name = faker.name()
        return name

    @staticmethod
    def age():  # from 0 to 100
        age = randint(0, 100)
        return age

    @staticmethod
    def big_string():
        length = 101
        big_string = ''.join(choice(string.ascii_letters + string.digits) for _ in range(length))
        return big_string

    @staticmethod
    def random_int():
        random_int = randint(0, 100)
        return random_int

    @staticmethod
    def random_string():
        random_string = faker.text(max_nb_chars=10)
        return random_string
