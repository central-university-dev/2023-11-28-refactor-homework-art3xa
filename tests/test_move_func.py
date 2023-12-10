from pathlib import Path

from renamer.base.project import Project
from renamer.mover import Mover

FIXTURES_PATH = Path("tests/fixtures/move/func")


def test_remove_func():
    project = Project(FIXTURES_PATH / "remove/proj")
    from_file = project.get_resource("source.py")
    to_file = project.get_resource("source2.py")
    move = Mover(project, from_file, to_file)
    removed_module, function_def = move._remove_function("func")
    assert removed_module.code == Path(FIXTURES_PATH / "remove/expected.py").read_text()


def test_add_func():
    project = Project(FIXTURES_PATH / "add/proj")
    from_file = project.get_resource("source.py")
    to_file = project.get_resource("source2.py")
    move = Mover(project, from_file, to_file)
    removed_module, function_def = move._remove_function("func")
    added_module = move._add_function("func", function_def)
    assert removed_module.code == Path(FIXTURES_PATH / "add/expected.py").read_text()
    assert added_module.code == Path(FIXTURES_PATH / "add/expected2.py").read_text()


def test_move_func():
    project = Project(FIXTURES_PATH / "move/proj")
    from_file = project.get_resource("source.py")
    to_file = project.get_resource("source2.py")
    move = Mover(project, from_file, to_file)
    got = move.move_function("func")
    assert got == [Path(FIXTURES_PATH / "move/expected.py").read_text(),
                   Path(FIXTURES_PATH / "move/expected2.py").read_text(),
                   Path(FIXTURES_PATH / "move/expected3.py").read_text()]


def test_move2_func():
    project = Project(FIXTURES_PATH / "move2/proj")
    from_file = project.get_resource("source.py")
    to_file = project.get_resource("source2.py")
    move = Mover(project, from_file, to_file)
    got = move.move_function("func")
    assert got == [Path(FIXTURES_PATH / "move2/expected.py").read_text(),
                   Path(FIXTURES_PATH / "move2/expected2.py").read_text(),
                   Path(FIXTURES_PATH / "move2/expected3.py").read_text()]