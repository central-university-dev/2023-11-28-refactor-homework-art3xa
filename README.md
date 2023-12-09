# Refactoring tool

1. Инструмент должен использовать библиотеку libcst или ast для работы с синтаксическим деревом исходного кода.
2. Инструмент должен позволять переименовывать/переносить функции/классы в исходном коде.
3. Инструмент должен автоматически обновлять все упоминания (в том числе импорты) переименованной/перенесенной функции/класса в исходном коде.
4. Покрытие тестами должно составлять более 95%


# How to use

```python
from renamer.base.project import Project
from renamer.rename import Rename

project = Project("proj")
file = project.get_resource("source.py")
rename = Rename(project, file)
got = rename.rename_function("func", "new_func")
with open("got.py", "w") as f:
    f.write(got)
```

```python
# proj/source.py
def func(arg1, arg2):
    print(f"{arg1}, arg{arg2}")


def main():
    func("arg1", "arg2")

```

```python
# got.py
def new_func(arg1, arg2):
    print(f"{arg1}, arg{arg2}")


def main():
    new_func("arg1", "arg2")

```