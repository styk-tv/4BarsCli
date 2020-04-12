
from fourbars.alive.locations import Locations
from fourbars.alive.import_clip import ImportClip
from fourbars.core.spawn import Spawn

# ALive is 4bars Live class abstraction (Live name is taken by pylive)
class ALive(object):

    sub_args = None
    locations = None

    def __init__(self, in_sub_args):
        self.locations = Locations()
        self.sub_args = in_sub_args

    def init(self):

        print("Copying default Live project to current location...")
        Spawn.cp(self.locations.default_set, self.locations.pwd)


    def up(self):
        pass

    def limport(self):



        lv = ImportClip(self.sub_args)
        lv.set_tempo(126.25)
        #lv.ctl_insert_record_4bars_at_index(15)
        lv.add_tracks_as_clips()
        #lv.add_note()


        #import_clip = ImportClip()
        #import_clip.debug_track_access_assume_first_is_midi()
        #import_clip.add_clip()
        #import_clip.add_note()

    def record(self):
        pass

    def locations(self):
        print(Locations().get_fullpretty())
