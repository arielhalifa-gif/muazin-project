import elasticsearch as es
from datetime import datetime


mapping = {"mapping": {
    "properties": {
            "size": {"type": int},
            "file_name": {'type': str},
            "creation_date": {'type': datetime},
            "last_modified_date": {'type': datetime},
            "stt": {'type': object}
    }
}}