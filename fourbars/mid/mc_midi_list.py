import os
import mido
from mido import *
from prettytable import PrettyTable
from fourbars.alive.locations import Locations
from fourbars.mid.mc_midi import McMidi
from fourbars.alive.parser_track import ParserTrack


# list of mido files loaded
class McMidiList(list):

    def __init__(self, *args, **kwargs):
        super(McMidiList, self).__init__(*args, **kwargs)
        file_paths = self._set_location(kwargs)
        self._load_midi_files(file_paths)

    def _set_location(self, kwargs):
        directory = kwargs.pop('directory', None)

        locations = Locations()
        if directory:
            locations.pwd = directory

        file_paths = [os.path.join(locations.pwd, f) for f in os.listdir(locations.pwd) if os.path.isfile(os.path.join(locations.pwd, f)) and f.lower().endswith(('.mid'))]
        if len(file_paths) == 0:
            print("No .mid files")
            exit(0)

        return file_paths

    def _load_midi_files(self, file_paths):
        for f in file_paths:
            print(f)
            self.append(McMidi(f))
            pass