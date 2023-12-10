from pathlib import Path

from renamer.base.project import Project
from renamer.mover import Mover

FIXTURES_PATH = Path("tests/fixtures/move/class")


def test_move_class():
    project = Project(FIXTURES_PATH / "move/proj")
    from_file = project.get_resource("source.py")
    to_file = project.get_resource("source2.py")
    move = Mover(project, from_file, to_file)
    got = move.move_class("AClass")
    assert got == [Path(FIXTURES_PATH / "move/expected.py").read_text(),
                   Path(FIXTURES_PATH / "move/expected2.py").read_text(),
                   Path(FIXTURES_PATH / "move/expected3.py").read_text()]
