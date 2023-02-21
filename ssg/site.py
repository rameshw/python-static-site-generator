from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self._dest = Path(dest)
        self._source = Path(source)

    def create_dir(self, path):
        directory = self._dest / path.relative_to(self._source)
        directory.mkdir(parents=True, exists_ok=True)

    def build(self):
        self._dest.mkdir(parents=True, exists_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
