from abc import ABC, abstractmethod


class IDatabase():
    def __init__(self):
        self.connection = None

    @abstractmethod
    def _establish_connection(self):
        pass

    @abstractmethod
    def _initialise_database(self):
        pass
