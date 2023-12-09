from pathlib import Path

from renamer.base.exceptions import NotAFolderError
from renamer.base.file import File
from renamer.base.resource import Resource


class Folder(Resource):
    def __new__(cls, path: str) -> "Folder":
        """Create new folder."""
        if not Path(path).is_dir():
            raise NotAFolderError(path)
        return super().__new__(cls)

    def get_files(self) -> list[File]:
        """Get files in folder."""
        return [file for file in self.get_children() if file.is_file]

    def get_folders(self) -> list["Folder"]:
        """Get folders in folder."""
        return [folder for folder in self.get_children() if folder.is_folder]

    def get_children(self) -> list[Resource]:
        """Get children of folder."""
        children = []
        for path in self.pathlib.iterdir():
            if path.is_file():
                children.append(File(path))
            elif path.is_dir():
                children.append(Folder(path))
        return children
