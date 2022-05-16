import pytest
from find_file import get_executable_file


def test_not_a_directory_path():
    with pytest.raises(NotADirectoryError):
        assert get_executable_file("..\\test_data\\test.bat")


def test_not_existing_directory():
    with pytest.raises(FileNotFoundError):
        assert get_executable_file("..\\test_data\\t1")


def test_get_file():
    assert get_executable_file("..\\test_data\\") == "..\\test_data\\test.bat"


def test_get_file_from_empty_directory():
    assert get_executable_file("..\\test_data\\emptydirectory") is None
