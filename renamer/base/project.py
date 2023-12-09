from pathlib import Path

from renamer.base.exceptions import DoesNotExistError
from renamer.base.file import File
from renamer.base.folder import Folder


class Project(Folder):
    def get_resource(self, path: str) -> File | Folder:
        """Get resource from project."""
        path = Path(self.pathlib / path)
        if not path.exists():
            raise DoesNotExistError(path)
        if path.is_file():
            return File(path)
        return Folder(path)

    def get_python_files(self) -> list[File]:
        """Get Python files in project."""
        return [File(str(path)) for path in self.pathlib.glob("**/*.py")]
