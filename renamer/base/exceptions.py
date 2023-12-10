from pathlib import Path


class DoesNotExistError(Exception):
    """Raised when a file or directory does not exist."""

    def __init__(self, path: Path) -> None:
        """Initialize error."""
        super().__init__(f"Path {path} does not exist")


class NotAFolderError(Exception):
    """Raised when a path is not a folder."""

    def __init__(self, path: str) -> None:
        """Initialize error."""
        super().__init__(f"Path {path} is not a folder")


class NotAFileError(Exception):
    """Raised when a path is not a file."""

    def __init__(self, path: str) -> None:
        """Initialize error."""
        super().__init__(f"Path {path} is not a file")
