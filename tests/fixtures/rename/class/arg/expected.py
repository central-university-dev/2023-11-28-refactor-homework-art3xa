class AClass:
    def __init__(self, new_name: str) -> None:
        self.new_name = new_name

    def func(self, arg2: str):
        print(f"{self.new_name}, arg{arg2}")


class BClass(AClass):
    def __init__(self, new_name: str) -> None:
        super().__init__(new_name)


class CClass(BClass, AClass):
    ...


class DClass:
    @staticmethod
    def some_method():
        print("some_method")


class EClass(DClass, CClass):
    def check(self):
        self.func("arg2")
        self.some_method()
