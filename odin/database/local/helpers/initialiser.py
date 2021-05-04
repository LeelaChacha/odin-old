import sqlite3

from pathfinder import PathFinder


class Initialiser:
    def __init__(self, connection):
        self.connection = connection

    def _create_tables_if_dont_exist(self):
        pass # TODO: implement structure Initialisation
