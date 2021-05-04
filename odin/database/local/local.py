from base import IDatabase


class DatabaseLocal(IDatabase):
    def __init__(self):
        self.connection = None
        self._establish_connection()
        self._initialise_database()

    def _establish_connection(self):
        from pathfinder import PathFinder
        path_finder = PathFinder()
        database_path = path_finder.return_database_path()

        self.connection = sqlite3.connect(database_path)

    def _initialise_database(self):
        pass

    #TODO
