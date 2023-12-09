import pytest

from renamer.base.exceptions import DoesNotExistError
from renamer.base.file import File
from renamer.base.folder import Folder
from renamer.base.project import Project


@pytest.fixture(scope="function")
def tmp_project_folder(tmp_path):
    (tmp_path / "subfolder").mkdir()
    file_path = tmp_path / "text.txt"
    file_path.write_text("Hello, World!")
    return Project(str(tmp_path))


def test_project_creation(tmp_project_folder):
    assert isinstance(tmp_project_folder, Project)


def test_project_is_folder(tmp_project_folder):
    assert tmp_project_folder.is_folder is True


def test_project_is_file(tmp_project_folder):
    assert tmp_project_folder.is_file is False


def test_project_get_files(tmp_project_folder, tmp_path):
    files = tmp_project_folder.get_files()
    assert len(files) == 1
    assert files[0].path == tmp_path / "text.txt"


def test_project_get_folders(tmp_project_folder):
    folders = tmp_project_folder.get_folders()
    assert len(folders) == 1


def test_project_get_python_files(tmp_project_folder):
    python_files = tmp_project_folder.get_python_files()
    assert len(python_files) == 0


def test_project_get_resource_file(tmp_project_folder):
    resource = tmp_project_folder.get_resource("text.txt")
    assert isinstance(resource, File)
    assert resource.read() == "Hello, World!"


def test_project_get_resource_folder(tmp_project_folder):
    resource = tmp_project_folder.get_resource("subfolder")
    assert isinstance(resource, Folder)


def test_project_get_resource_not_found(tmp_project_folder):
    with pytest.raises(DoesNotExistError):
        tmp_project_folder.get_resource("not_found")
