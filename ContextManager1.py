from copy import deepcopy

class TransactionalSaver:
    def __init__(self, object):
        self.object = object
        self.copy_object = None

    def __enter__(self):
        self.copy_object = deepcopy(self.object)
        return self.object


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.object.__dict__.update(self.copy_object.__dict__)
            print(f'There was an error: ({exc_val}), so the object was not changed')
            return True
        else:
            print('The object was successfully changed')


class Person:
    def __init__(self, name: str, age: int, friends: list):
        self.name = name
        self.age = age
        self.friends = friends

    def __str__(self):
        return f'name: {self.name}, age: {self.age}, friends: {self.friends}'


a = Person('a', 42, ['b', 'c'])
print(a)


with TransactionalSaver(a) as object:
    object.age = 20
    object.friends.append('d')
    object.name.append(123)

print(a)