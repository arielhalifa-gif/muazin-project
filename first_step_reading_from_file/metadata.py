from pathlib import Path
import datetime


def create_json(size, fileN, creationD, lastM):
    file = {
        "size": size,
        "file name": fileN,
        "creation date": creationD,
        "last modified date": lastM
    }
    return file

def extract_metadata(path: Path):
    statistics = path.stat()
    size = statistics.st_size
    file_name = path.name
    creation_date = datetime.datetime.fromtimestamp(statistics.st_birthtime)
    last_modified = datetime.datetime.fromtimestamp(statistics.st_mtime)
    file_json = create_json(size, file_name, creation_date, last_modified)
    return file_json

extract_metadata(Path('data/podcasts/podcasts/download (1).wav'))