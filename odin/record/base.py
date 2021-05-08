from abc import ABC, abstractmethod


class IRecord():
    def __init__(self):
        self._connection = None

    @abstractmethod
    def _establish_connection(self):
        pass

    @abstractmethod
    def _destroy_connection(self):
        pass

    @abstractmethod
    def _create_memo_table_if_doesnt_exist(self):
        pass

    @abstractmethod
    def push_memos(self, stamp, memo):
        pass

    @abstractmethod
    def pull_memos(self, stamp):
        pass
