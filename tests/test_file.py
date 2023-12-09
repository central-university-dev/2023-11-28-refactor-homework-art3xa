import pytest

from renamer.file import File


@pytest.fixture(scope="function", params=["temp.txt", "temp"])
def tmp_file(tmp_path, request):
    content = "Hello, World!"
    file_path = tmp_path / request.param
    file_path.write_text(content)
    return File(str(file_path))


def test_is_file(tmp_file):
    assert tmp_file.is_file is True


def test_is_folder(tmp_file):
    assert tmp_file.is_folder is False


def test_read(tmp_file):
    assert tmp_file.read() == "Hello, World!"


def test_read_bytes(tmp_file):
    assert tmp_file.read_bytes() == b"Hello, World!"


def test_is_python_file_false(tmp_file):
    assert tmp_file.is_python_file() is False


def test_is_python_file_true(tmp_path):
    file_path = tmp_path / "temp.py"
    file_path.write_text("print('Hello, World!')")
    tmp_file = File(str(file_path))
    assert tmp_file.is_python_file() is True
