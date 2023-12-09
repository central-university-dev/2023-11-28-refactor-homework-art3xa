from pathlib import Path


class Resource:
    def __init__(self, path: str) -> None:
        self._path = path

    @property
    def path(self) -> str:
        """Get path of resource."""
        return self._path

    @property
    def name(self) -> str:
        """Get name of resource."""
        return Path(self._path).name

    @property
    def pathlib(self) -> Path:
        """Get pathlib.Path of resource."""
        return Path(self._path)

    @property
    def is_file(self) -> bool:
        """Check if resource is a file."""
        return Path(self._path).is_file()

    @property
    def is_folder(self) -> bool:
        """Check if resource is a folder."""
        return Path(self._path).is_dir()

    def __hash__(self) -> int:
        """Hash resource."""
        return hash(self._path)

    def __eq__(self, other: "Resource") -> bool:
        """Compare resource."""
        return self._path == other._path and self.__class__ == other.__class__

    def __repr__(self) -> str:
        """Represent resource."""
        return f"{self.__class__.__name__}(path={self._path})"
