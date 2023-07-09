import inspect
import importlib
import importlib.util


def first_function():
    print("First function called!")


def second_function():
    print("Second function called!")


def create_py_file():
    choice = input("Type 1 or 2 ")

    with open("test.py", 'w') as f:
        if choice == "1":
            function = first_function
        else:
            function = second_function

        content = inspect.getsource(function)
        f.write(content)

    with open("test.py", 'r') as f:
        print(f.read())


def run_py_file():
    spec = importlib.util.spec_from_file_location("test", "./test.py")
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)


def main():
    create_py_file()
    run_py_file()


if __name__ == '__main__':
    main()
