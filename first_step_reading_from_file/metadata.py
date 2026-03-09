from pathlib import Path
import datetime
import logger as l


def create_json(size, fileN, creationD, lastM):
    l.logger.info('creatin json file....')
    file = {
        "size": size,
        "file name": fileN,
        "creation date": creationD,
        "last modified date": lastM
    }
    return file

def extract_metadata(path: Path):
    l.logger.info('extracting metadada')
    statistics = path.stat()
    size = statistics.st_size
    file_name = path.name
    creation_date = datetime.datetime.fromtimestamp(statistics.st_birthtime)
    last_modified = datetime.datetime.fromtimestamp(statistics.st_mtime)
    file_json = create_json(size, file_name, creation_date, last_modified)
    l.logger.info('metadata extracted')
    return file_json