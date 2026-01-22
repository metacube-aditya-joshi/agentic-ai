import datetime
from pydantic import BaseModel
from src.file_manager import open_json  # your JSON helper

class Request(BaseModel):
    def __init__(self, description, client, project):
        # Load existing requests
        requests = open_json("requests.json", "read") or []

        if requests:
            # Get the max ID and add 1
            max_id = max(int(r['id']) for r in requests)
            self.id = max_id + 1
        else:
            self.id = 1  # first request

        self.description = description
        self.client = client
        self.project = project
        self.timestamp = datetime.datetime.now().isoformat()
