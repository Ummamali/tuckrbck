from json import load, dump
import os
from pathlib import Path


class FlatFileCollection:

    def __init__(self, filepath, cache=True):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = Path(os.path.join(base_dir, filepath))
        # checks if path exists
        if not self.file_path.exists():
            print('Path does not extsis: Creating path....')
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            self.file_path.write_text('{}')

        self.cache = cache
        self.items = {} if not cache else self.read_from_file()

    def write_to_file(self, obj):
        with open(self.file_path, mode='w') as f:
            dump(obj, f)

    def read_from_file(self):
        with open(self.file_path) as f:
            return load(f)

    def read_all(self):
        return self.items if self.cache else self.read_from_file()

    def read_one(self, id):
        return self.items[id] if self.cache else self.read_from_file()[id]

    def create(self, id, item):
        items = self.items
        if not self.cache:
            items = self.readAll()
        items[id] = item
        self.write_to_file(items)

    def update(self, id, delta):
        items = self.items
        if not self.cache:
            items = self.readAll()

        items[id].update(delta)
        self.write_to_file(items)
        return items[id]

    def delete(self, id):
        items = self.items if self.cache else self.readAll()
        removed = items.pop(id, None)
        self.write_to_file(self.items)
        return id if removed is not None else None

    def exists(self, id):
        return id in self.items
