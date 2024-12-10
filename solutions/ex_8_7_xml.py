# Using books.xml, do the following:
# - read the XML file
# - append records in the XML file to books.csv: leave nonexistent fields empty,
# change genre:
#   - to be all lowercase
#   - to have spaces   replaced with underscores _
# - create a new XML file where genres become tags, and books are grouped by
# genre:
#   - include all tags under book, except genre
#   - change date format 2000-12-01 -> 1 December 2000
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
import shutil

current_path = Path().resolve()
docs_path = current_path.parent / "docs"
xml_file = docs_path / "books.xml"
csv_file = docs_path / "books.csv"
csv_file_copy = current_path / csv_file.name
new_xml_file = current_path / xml_file.name

shutil.copyfile(csv_file, csv_file_copy)

tree = ET.parse(xml_file)
root = tree.getroot()


def normalize_genre(value):
    """Convert genre to lowercase and replace spaces with underscores."""
    return value.lower().replace(" ", "_")


def change_format(date_str, format_old="%Y-%m-%d", format_new="%d %B %Y"):
    """Convert date format from 'YYYY-MM-DD' to 'DD Month YYYY'."""
    return datetime.strptime(date_str, format_old).strftime(format_new)


with csv_file_copy.open("r+") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    f.seek(0, 2)
    f.write("\n")  # Ensure new line before appending

    for book in root:
        row = {}
        for subelem in book:
            fieldname = subelem.tag.capitalize()
            if fieldname not in fieldnames:
                continue
            value = subelem.text
            if fieldname == "Genre":
                value = normalize_genre(value)
            row[fieldname] = value
        writer.writerow(row)

grouped_books = defaultdict(list)
for book in root:
    genre_elem = book.find("genre")
    genre = normalize_genre(genre_elem.text)
    grouped_books[genre].append(book)
    book.remove(genre_elem)

    publish_date = book.find("publish_date")
    publish_date.text = change_format(publish_date.text)

new_root = ET.Element("catalog")
for genre, books in grouped_books.items():
    genre_elem = ET.SubElement(new_root, genre)
    genre_elem.extend(books)

ET.indent(new_root, space="  ", level=0)
ET.ElementTree(new_root).write(new_xml_file)
