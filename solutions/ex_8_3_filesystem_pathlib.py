from pathlib import Path

# Write a Python program that creates a directory outdir at the current location
# and a directory innerdir inside outdir. Create an empty file inside innerdir.
# Use os.walk() to print the directory tree for outdir. Remove the directories
# and the file.
innerdir_path = Path() / "outdir" / "innerdir"
innerdir_path.mkdir(parents=True, exist_ok=True)

file_path = innerdir_path / "empty.txt"
file_path.touch()

for path, dirnames, filenames in innerdir_path.parent.walk():
    print(path, dirnames, filenames)

file_path.unlink()
innerdir_path.rmdir()
innerdir_path.parent.rmdir()


# Write a function that returns a list (or iterator) of all the file names with
# an extension from a directory. Give the path and the file extension as
# parameters.
def get_all_files(path, extension):
    p = Path(path)
    return p.rglob(f"*.{extension}")


for filename in get_all_files(".", "py"):
    print(filename)
