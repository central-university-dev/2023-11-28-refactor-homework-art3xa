from pathlib import Path

import pytest

from renamer.resource import Resource


@pytest.fixture()
def resource():
    return Resource("test_path")


def test_path(resource):
    assert resource.path == "test_path"


def test_name(resource):
    assert resource.name == "test_path"


def test_pathlib(resource):
    assert resource.pathlib == Path("test_path")


def test_is_file(resource):
    assert resource.is_file is False


def test_is_folder(resource):
    assert resource.is_folder is False


def test_hash(resource):
    assert hash(resource) == hash("test_path")


def test_eq(resource):
    assert (resource == Resource("test_path")) is True


def test_repr(resource):
    assert repr(resource) == "Resource(path=test_path)"
