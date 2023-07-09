import inspect
import textwrap
import types
from importlib.util import spec_from_file_location, module_from_spec

from package_1 import function_1
from package_2 import function_2


def compose_module(choice):
    if choice == "1":
        def main():
            function_1()
            function_2()

    else:
        def main():
            function_2()
            function_1()

    new_function = types.FunctionType(main.__code__, globals())
    content = inspect.getsource(new_function)
    content = textwrap.dedent(content)

    function_1_content = inspect.getsource(function_1)
    function_1_content = textwrap.dedent(function_1_content)

    function_2_content = inspect.getsource(function_2)
    function_2_content = textwrap.dedent(function_2_content)
    with open("test.py", 'w') as f:
        f.write(function_1_content + "\n\n")
        f.write(function_2_content + "\n\n")
        f.write(content + "\n\n")


def get_py_module():
    spec = spec_from_file_location("test", "./test.py")
    test_module = module_from_spec(spec)
    spec.loader.exec_module(test_module)
    return test_module


def main():
    choice = input("Type 1 or 2\n")
    compose_module(choice)
    module = get_py_module()
    module.main()


if __name__ == '__main__':
    main()
