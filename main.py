import os


print(os.environ.get("env1", "No variable"))


def sum(x, y):
    return x


assert 3 == sum(1, 2)
