from pathlib import Path

from renamer.project import Project
from renamer.rename import Rename

FIXTURES_PATH = Path("tests/fixtures/rename/func")


def test_rename_func_arg():
    project = Project(FIXTURES_PATH / "arg/proj")
    file = project.get_resource("source.py")
    rename = Rename(project, file)
    got = rename.rename_variable("arg1", "new_name")
    assert got == [Path(FIXTURES_PATH / "arg/expected.py").read_text()]


def test_rename_func_arg_with_import():
    project = Project(FIXTURES_PATH / "arg_with_import/proj")
    file = project.get_resource("source.py")
    rename = Rename(project, file)
    got = rename.rename_variable("arg1", "new_name")
    assert got == [
        Path(FIXTURES_PATH / "arg_with_import/expected.py").read_text(),
        Path(FIXTURES_PATH / "arg_with_import/expected2.py").read_text(),
    ]
