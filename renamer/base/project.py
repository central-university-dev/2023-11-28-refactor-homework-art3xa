from pathlib import Path

from renamer.base.exceptions import DoesNotExistError, NotAFileError
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

    def get_file(self, path: str) -> File:
        """Get Python file from project."""
        file = self.get_resource(path)
        if not isinstance(file, File):
            raise NotAFileError(path)
        return file

    def get_python_files(self) -> list[File]:
        """Get Python files in project."""
        return [File(str(path)) for path in self.pathlib.glob("**/*.py")]
