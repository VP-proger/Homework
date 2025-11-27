class ErrorLogger:
    def __init__(self, object):
        self.object = object

    def __enter__(self):
        return self.object

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'{exc_type.__name__}: "{exc_val}" {exc_tb}')
        return True

with ErrorLogger(1970) as obj:
    1 / 0