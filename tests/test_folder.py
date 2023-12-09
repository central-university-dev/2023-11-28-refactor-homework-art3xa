import pytest

from renamer.errors import NotAFolderError
from renamer.file import File
from renamer.folder import Folder


@pytest.fixture(scope="function")
def tmp_folder(tmp_path):
    file_path = tmp_path / "temp.txt"
    file_path.write_text("Hello, World!")
    (tmp_path / "subfolder").mkdir()
    return Folder(str(tmp_path))


def test_is_file(tmp_folder):
    assert tmp_folder.is_file is False


def test_is_folder(tmp_folder):
    assert tmp_folder.is_folder is True


def test_get_files(tmp_folder):
    files = tmp_folder.get_files()
    assert len(files) == 1
    assert isinstance(files[0], File)
    assert files[0].read() == "Hello, World!"


def test_get_folders(tmp_folder):
    folders = tmp_folder.get_folders()
    assert len(folders) == 1
    assert isinstance(folders[0], Folder)


def test_folder_create_from_file(tmp_path):
    file_path = tmp_path / "temp.txt"
    file_path.write_text("Hello, World!")
    with pytest.raises(NotAFolderError):
        Folder(str(file_path))
