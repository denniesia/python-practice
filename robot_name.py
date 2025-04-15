import random, string

class Robot:
    used_names = set()

    def __init__(self):
        self.name = self.name_generator()

    def name_generator(self):
        while True:
            letters = random.choices(string.ascii_uppercase, k=2)
            numbers = random.choices(string.digits, k=3)
            name = ''.join(letters) + ''.join(numbers)

            if name not in self.used_names:
                self.used_names.add(name)
                return name

    def reset_name(self):
        self.name = self.name_generator()

    def get_name(self):
        return self.name



