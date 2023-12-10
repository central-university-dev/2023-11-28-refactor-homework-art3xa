from pathlib import Path

from renamer.base.project import Project
from renamer.renamer import Renamer

FIXTURES_PATH = Path("tests/fixtures/rename/func")


def test_rename_func_name():
    project = Project(FIXTURES_PATH / "name/proj")
    file = project.get_resource("source.py")
    rename = Renamer(project, file)
    got = rename.rename_function("func", "new_func")
    assert got == [Path(FIXTURES_PATH / "name/expected.py").read_text()]


def test_rename_func_name_with_import():
    project = Project(FIXTURES_PATH / "name_with_import/proj")
    file = project.get_resource("source.py")
    rename = Renamer(project, file)
    got = rename.rename_function("func", "new_func")
    assert got == [
        Path(FIXTURES_PATH / "name_with_import/expected.py").read_text(),
        Path(FIXTURES_PATH / "name_with_import/expected2.py").read_text(),
    ]


def test_rename_func_name_with_import_alias():
    project = Project(FIXTURES_PATH / "name_with_import_alias/proj")
    file = project.get_resource("source.py")
    rename = Renamer(project, file)
    got = rename.rename_function("func", "new_func")
    assert got == [
        Path(FIXTURES_PATH / "name_with_import_alias/expected.py").read_text(),
        Path(FIXTURES_PATH / "name_with_import_alias/expected2.py").read_text(),
    ]


def test_rename_func_name_with_import_alias_back():
    project = Project(FIXTURES_PATH / "name_with_import_alias/proj")
    file = project.get_resource("source2.py")
    rename = Renamer(project, file)
    got = rename.rename_function("func", "new_func")
    assert got == [
        Path(FIXTURES_PATH / "name_with_import_alias/expected.py").read_text(),
        Path(FIXTURES_PATH / "name_with_import_alias/expected2.py").read_text(),
    ]


def test_rename_func_name_with_import_alias_module():
    project = Project(FIXTURES_PATH / "name_with_import_alias_module/proj")
    file = project.get_resource("source_module/source_module_file.py")
    rename = Renamer(project, file)
    got = rename.rename_function("some_func", "new_func")
    assert got == [
        Path(FIXTURES_PATH / "name_with_import_alias_module/expected.py").read_text(),
        Path(FIXTURES_PATH / "name_with_import_alias_module/expected2.py").read_text(),
        Path(FIXTURES_PATH / "name_with_import_alias_module/expected_module/expected_module_file.py").read_text(),
        Path(FIXTURES_PATH / "name_with_import_alias_module/expected_module/expected_module_file2.py").read_text(),
        Path(FIXTURES_PATH / "name_with_import_alias_module/expected_module/__init__.py").read_text(),
    ]
