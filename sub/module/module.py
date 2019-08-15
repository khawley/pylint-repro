from ..other_folder import module
import collections

__all__ = [
    'Module',
]


class Module():
    inner = collections.Counter()

    def __init__(self, name=None):
        self.name = name
