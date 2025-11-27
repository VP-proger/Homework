class AttributesMocker:
    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.attributes = {}
        self.temporary_attributes = kwargs

    def __enter__(self):
        for key, value in self.obj.__dict__.items():
            self.attributes[key] = value

        self.obj.__dict__.update(self.temporary_attributes)

        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj.__dict__.update(self.attributes)


class MyClass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.__dict__.items()}'

a = MyClass(1, 2, 3)
print(a)

with AttributesMocker(a, x=10, y=20, z=30) as mocker:
    mocker.i = 100
    print(mocker)

print(a)