class AClass:
    def __init__(self, arg1: str) -> None:
        self.arg1 = arg1

    def func(self, arg2: str):
        print(f"{self.arg1}, arg{arg2}")


class BClass(AClass):
    def __init__(self, arg1: str) -> None:
        super().__init__(arg1)


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
