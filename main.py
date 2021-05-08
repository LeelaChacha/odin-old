from odin.record.local import LocalRecord


if __name__ == "__main__":
    database = LocalRecord()
    database.pull_memos("APPOINTMENT_IN_EMAIL")
