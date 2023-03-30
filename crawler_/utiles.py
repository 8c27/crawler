import os
from crawler_.setting import DOWNLOADS_DIR


class Utiles:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)


