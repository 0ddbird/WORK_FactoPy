import inspect
import importlib
import importlib.util

from package_1 import main as function_1
from package_2 import main as function_2


def compose_module(choice):
    with open("test.py", 'w') as f:
        if choice == "1":
            function = function_1
        else:
            function = function_2

        content = inspect.getsource(function)
        f.write(content)


def get_py_module():
    spec = importlib.util.spec_from_file_location("test", "./test.py")
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)
    return test_module


def main():
    choice = input("Type 1 or 2\n")
    compose_module(choice)
    module = get_py_module()
    module.main()


if __name__ == '__main__':
    main()
