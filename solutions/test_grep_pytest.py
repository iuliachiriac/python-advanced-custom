import pytest

from ex_8_1_files import grep


# Fixture using `tmp_path_factory`
# https://docs.pytest.org/en/stable/how-to/tmp_path.html#the-tmp-path-factory-fixture
@pytest.fixture(scope="session")
def filename(tmp_path_factory):  # fixture requires another fixture
    filename = "test_file.txt"
    file_path = tmp_path_factory.mktemp("data") / filename
    with file_path.open("w") as f:
        f.write("hello world\n")
        f.write("hi there\n")
        f.write("dear world, hello!\n")
        f.write("hello\n")
        f.write("bye\n")
        f.write("hellohello\n")
    return str(file_path)


def test_multiple_lines_match(filename):
    result = grep("hello", filename)
    assert isinstance(result, list)
    assert len(result) == 4
    assert result == [
        "hello world\n",
        "dear world, hello!\n",
        "hello\n",
        "hellohello\n",
    ]


@pytest.mark.parametrize("search_text", ["*", "   "])
def test_no_lines_match(filename, search_text):
    result = grep(search_text, filename)
    assert result == []


def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        grep("hello", "nonexistent.txt")
