# Refactoring tool

1. Инструмент должен использовать библиотеку libcst или ast для работы с синтаксическим деревом исходного кода.
2. Инструмент должен позволять переименовывать/переносить функции/классы в исходном коде.
3. Инструмент должен автоматически обновлять все упоминания (в том числе импорты) переименованной/перенесенной функции/класса в исходном коде.
4. Покрытие тестами должно составлять более 95%


# How to use renamer

```python
from renamer.base.project import Project
from renamer.renamer import Renamer

project = Project("proj")
file = project.get_resource("source.py")
rename = Renamer(project, file)
got = rename.rename_function("func", "new_func")
with open("new_proj/source.py", "w") as f:
    f.write(got[0])
```

```python
# proj/source.py
def func(arg1, arg2):
    print(f"{arg1}, arg{arg2}")


def main():
    func("arg1", "arg2")

```

```python
# new_proj/source.py
def new_func(arg1, arg2):
    print(f"{arg1}, arg{arg2}")


def main():
    new_func("arg1", "arg2")

```

# How to use mover

```python
from renamer.base.project import Project
from renamer.mover import Mover

project = Project("proj")
from_file = project.get_resource("source.py")
to_file = project.get_resource("source2.py")
move = Mover(project, from_file, to_file)
got = move.move_class("AClass")
with open("new_proj/source.py", "w") as f:
    f.write(got[0])
with open("new_proj/source2.py", "w") as f:
    f.write(got[1])
with open("new_proj/source3.py", "w") as f:
    f.write(got[2])
```

```python
# proj/source.py
class AClass:
    def __init__(self):
        ...

    def a_method(self):
        ...


AClass()

```

```python
# proj/source2.py
import source

source.AClass()

```

```python
# proj/source3.py
import source

source.AClass()

```

```python
# new_proj/source.py
import source2


source2.AClass()
```

```python
# new_proj/source2.py
class AClass:
    def __init__(self):
        ...

    def a_method(self):
        ...
import source

AClass()

```

```python
# new_proj/source3.py
import source2

source2.AClass()

```