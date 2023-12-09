from renamer.base.resource import Resource


class File(Resource):
    def read(self) -> str:
        """Read file as string."""
        return self.pathlib.read_text(encoding="utf-8")

    def read_bytes(self) -> bytes:
        """Read file as bytes."""
        return self.pathlib.read_bytes()

    def is_python_file(self) -> bool:
        """Check if file is a Python file."""
        return self.pathlib.suffix == ".py"
