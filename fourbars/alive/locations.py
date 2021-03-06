from os.path import expanduser
import os
import errno
from prettytable import PrettyTable


class Locations(object):

    home = None
    config = None
    fourbars_library = None
    preferences_latest = None
    full_pretty = None
    log = None
    default_set = None
    user_library = None
    pwd = None

    def __init__(self):
        self.set_home()
        self.set_config()
        self.set_fourbars_library()
        self.set_preferences_latest()
        self.set_log()
        self.set_pwd()
        self.set_default_set()
        self.set_user_library()

    def get_fullpretty(self):
        table = PrettyTable()
        table.field_names = ['Name', 'Absolute Path']
        table.add_row(['HOME', self.home])
        table.add_row(['Current Folder', self.pwd])
        table.add_row(['4bars Configuration', self.config])
        table.add_row(['4bars Library', self.fourbars_library])
        table.add_row(['Ableton Preferences', self.preferences_latest])
        table.add_row(['Ableton Default Live Set', self.default_set])
        table.add_row(['Ableton User Library', self.user_library])
        table.add_row(['Ableton Log', self.log])
        table.align = "l"
        return table

    def get_aif_files(self):
        return self.get_files('aif')

    def get_files(self, ext):
        files = [os.path.join(self.pwd, f) for f in os.listdir(self.pwd) if os.path.isfile(os.path.join(self.pwd, f)) and f.lower().endswith(('.{0}'.format(ext)))]
        if len(files) == 0:
            print("No .{0} files".format(ext))
            exit(0)

        return files

    def set_home(self):
        self.home = expanduser("~")

    def set_config(self):
        self.config = os.path.join(self.home, ".config", "4bars")
        if not os.path.exists(self.config):
            self.mkdir_p(self.config)

    def set_fourbars_library(self):
        self.fourbars_library = os.path.join(self.config, "LIBRARY")
        if not os.path.exists(self.fourbars_library):
            self.mkdir_p(self.fourbars_library)

    def set_preferences_latest(self):
        # mac location assumption
        relative_preferences_base = "Library/Preferences/Ableton/"
        absolute_preferences_base = os.path.join(self.home, relative_preferences_base)
        latest = sorted(os.listdir(absolute_preferences_base), reverse=True)[0]
        self.preferences_latest = os.path.join(absolute_preferences_base, latest)

    def set_log(self):
        self.log = os.path.join(self.preferences_latest, "Log.txt")

    def set_pwd(self):
        with open(os.path.join(self.config, ".cache/pwd"), 'r') as file:
            self.pwd = file.read().replace('\n', '')

    def set_default_set(self):
        self.default_set = os.path.join(self.preferences_latest, "BaseFiles/DefaultLiveSet.als")

    def set_user_library(self):
        self.user_library = os.path.join(self.home, "Music/Ableton/User Library")

    # TODO: move to Spawn
    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


