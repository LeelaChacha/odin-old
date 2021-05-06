import datetime
import sqlite3

from odin.database.base import IRecord
from odin.database.helpers.pathfinder import PathFinder


class LocalRecord(IRecord):
    def __init__(self, record_path=""):
        super().__init__()

        self._custom_record_path = record_path
        self._connection = None
        self._create_memo_table_if_doesnt_exist()

    def _establish_connection(self):
        if self._connection is None:
            if self._custom_record_path == "":
                path_finder = PathFinder()
                record_path = path_finder.return_record_path()
            else:
                record_path = self._custom_record_path

            self._connection = sqlite3.connect(record_path)

    def _destroy_connection(self):
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def _execute_sql(self, sql_command, parameters=None, commit=False):
        cursor = self._connection.cursor()
        query_result = cursor.execute(sql_command) \
                        if parameters is None\
                        else cursor.execute(sql_command, parameters)

        if commit:
            self._connection.commit()
        return query_result

    def _create_memo_table_if_doesnt_exist(self):
        self._establish_connection()

        self._execute_sql("CREATE TABLE IF NOT EXISTS ODIN_MEMOS"
                          "(PUSHED_AT TIMESTAMP,"
                          "STAMP VARCHAR(255),"
                          "MEMO TEXT)",
                          commit=True)

        self._destroy_connection()

    def _delete_memo(self, pushed_at, stamp, memo):
        self._execute_sql("DELETE FROM ODIN_MEMOS "
                          "WHERE PUSHED_AT=:pushed_at "
                          "AND STAMP=:stamp "
                          "AND MEMO=:memo",
                          parameters={"pushed_at": pushed_at, "stamp": stamp, "memo": memo},
                          commit=True)

    def push_memos(self, stamp, memo):
        self._establish_connection()

        pushed_at = datetime.datetime.now()
        self._execute_sql("INSERT INTO ODIN_MEMOS "
                          "VALUES(?, ?, ?)",
                          parameters=(pushed_at, stamp, memo),
                          commit=True)

        self._destroy_connection()

    def pull_memos(self, stamp):
        memos = []

        self._establish_connection()

        result = self._execute_sql("SELECT * FROM ODIN_MEMOS "
                                   "WHERE STAMP=:stamp ",
                                   parameters={"stamp": stamp})

        for row in result:
            memos.append(row[2])
            self._delete_memo(row[0], row[1], row[2])

        self._destroy_connection()
        return memos