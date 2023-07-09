import inspect
import importlib
import importlib.util

from package_1 import function as function_1
from package_2 import function as function_2


def create_py_file(choice):
    with open("test.py", 'w') as f:
        if choice == "1":
            function = function_1
        else:
            function = function_2

        content = inspect.getsource(function)
        f.write(content)


def run_py_file():
    spec = importlib.util.spec_from_file_location("test", "./test.py")
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)
    return test_module


def main():
    choice = input("Type 1 or 2\n")
    create_py_file(choice)
    test_module = run_py_file()
    test_module.function()


if __name__ == '__main__':
    main()
