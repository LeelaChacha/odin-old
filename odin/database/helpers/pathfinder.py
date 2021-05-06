import os, platform


class PathFinder:
    def __init__(self):
        self.database_name = "odin_record.db"

    def return_record_path(self):
        operating_system = platform.system()

        if operating_system == "Windows":
            return self._get_path_to_record_windows()
        elif operating_system == "Linux":
            return self._get_path_to_record_linux()
        elif operating_system == "Darwin":
            return self._get_path_to_record_mac()

    def _get_path_to_record_windows(self):
        appdata_dir = os.getenv('APPDATA')
        odin_dir = os.path.join(appdata_dir, "Odin/")
        os.makedirs(odin_dir, mode = 0o777, exist_ok = True)
        return os.path.join(odin_dir, self.database_name)

    def _get_path_to_record_linux(self):
        odin_dir = os.getenv('~\.Odin')
        os.makedirs(odin_dir, mode = 0o777, exist_ok = True)
        return os.path.join(odin_dir, self.database_name)

    def _get_path_to_record_mac(self):
        appdata_dir = os.path.expanduser('~/Library/Application')
        odin_dir = os.path.join(appdata_dir, "Odin/")
        os.makedirs(odin_dir, mode = 0o777, exist_ok = True)
        return os.path.join(odin_dir, self.database_name)
