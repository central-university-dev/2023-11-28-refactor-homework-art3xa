from source_module.source_module_file import new_func as alias_function


def func(arg1, arg2):
    print(f"{arg1}, arg{arg2}")


def main():
    func("arg1", "arg2")
    alias_function("arg1", "arg2")
