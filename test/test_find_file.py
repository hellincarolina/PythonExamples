import pytest
from find_file import get_executable_file


def test_not_a_directory_path():
    with pytest.raises(NotADirectoryError):
        assert get_executable_file("C:\\Users\\test\\test1.txt")


def test_not_existing_directory():
    with pytest.raises(FileNotFoundError):
        assert get_executable_file("C:\\invalid_path")


def test_get_file():
    assert get_executable_file("C:\\Users\\test") == "C:\\Users\\test\\test.bat"


def test_get_file_from_empty_directory():
    assert get_executable_file("C:\\Users\\test\\emptyDirectory") is None
