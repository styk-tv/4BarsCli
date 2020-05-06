import os
import mido
from mido import *
from prettytable import PrettyTable
from fourbars.alive.locations import Locations
from fourbars.alive.parser_track import ParserTrack
#from fourbars.mid.mc_midi_list import McMidi
import string


class McTrack(object):
    track = None
    name = None
    time_signature = None
    clip_notes = []
    playable = False

    def __init__(self, in_track, in_ticks_per_beat):
        self.clip_notes = []
        self.playable = False
        self.track = in_track
        self.ticks_per_beat = in_ticks_per_beat
        self._name_clear()
        self._get_time_signature()
        self.abletonize()

    def _name_clear(self):
        self.name = ''.join(filter(lambda x: x in set(string.printable), self.track.name))

    def _get_time_signature(self):
        for i, message in enumerate(self.track):
            if message.type == "time_signature":
                self.time_signature = message
                break
        pass

    def abletonize(self):
        pos_midi = 0
        pos_clip = 0
        for i, message in enumerate(self.track):
            pos_midi += message.time
            pos_clip += message.time / self.ticks_per_beat
            if message.type == "note_on":
                note = McNote()
                note.note = message.note
                note.position = pos_clip
                note.duration = None
                note.velocity = message.velocity
                self.clip_notes.append(note)
                self.playable = True
            elif message.type == "note_off":
                for note in self.clip_notes:
                    if not note.duration:
                        note.duration = pos_clip - note.position
                        pass


class McNote(object):
    note = None
    position = None
    duration = None
    velocity = None

    def __init__(self):
        self.note = None
        self.position = None
        self.duration = None
        self.velocity = None


class McMidi(mido.MidiFile):
    clips = None

    def __init__(self, *args, **kwargs):
        super(McMidi, self).__init__(*args, **kwargs)
        self.clips = []

        for i, track in enumerate(self.tracks):
            t = McTrack(track, self.ticks_per_beat)
            self.clips.append(t)

        pass

    # note position duration velocity
    """
    :param note:      (int)    MIDI note index
    :param position:  (float)  Position, in beats
    :param duration:  (float)  Duration, in beats
    :param velocity:  (int)    MIDI note velocity
            """
    # def clip_simple(self, t):

    # parser = None
    # locations = None
    # sub_args = None
    # pretty_table = None
    # files = None
    # count = None
    # index = 0
    # mitracks = []
    # ticks_per_beat = 0
    #
    # def __init__(self, in_sub_args):
    #     self.sub_args = in_sub_args
    #     self.locations = Locations()
    #
    # def load_midi_files(self):
    #
    #     if self.sub_args.d:
    #         self.locations.pwd = self.sub_args.d
    #
    #     self.files = [os.path.join(self.locations.pwd,f) for f in os.listdir(self.locations.pwd) if os.path.isfile(os.path.join(self.locations.pwd,f)) and f.lower().endswith(('.mid'))]
    #     self.count = len(self.files)
    #     if self.count == 0:
    #         print("No .mid files")
    #         exit(0)
    #
    #     for f in self.files:
    #         m = mido.MidiFile(f)
    #         self.ticks_per_beat = m.ticks_per_beat #TODO: please fix this asap, awful and temporary
    #         for i, track in enumerate(m.tracks):
    #             self.mitracks.append(track)

    # def tracks(self):

        # if self.sub_args.d:
        #     self.locations.pwd = self.sub_args.d
        #
        # files = self.get_mid_files()
        #
        # table = PrettyTable()
        # table.field_names = ['Name', '# Tracks', 'Track Name', 'Length (s)', 'Type', 'TicksPerBeat']
        # table.align = "l"
        #
        # for f in files:
        #
        #     mid = mido.MidiFile(f)
        #
        #     path_array = f.split('/')
        #     file_name = path_array[len(path_array)-1]
        #
        #     for i, track in enumerate(mid.tracks):
        #         #ptrack = ParserTrack(track)
        #         table.add_row([file_name, len(mid.tracks), track.name, mid.length, mid.type, mid.ticks_per_beat ])
        #
        # print(table)
        # print()

    # def notes(self):

        # if self.sub_args.d:
        #     self.locations.pwd = self.sub_args.d
        #
        # files = self.get_mid_files()
        #
        # for f in files:
        #
        #     mid = mido.MidiFile(f)
        #     path_array = f.split('/')
        #     file_name = path_array[len(path_array)-1]
        #
        #     pretty_table = PrettyTable()
        #     pretty_table.field_names = ['Name', 'Value']
        #     pretty_table.align = "l"
        #     pretty_table.add_row(["File Name", file_name])
        #     pretty_table.add_row(["MIDI Type", mid.type])
        #     pretty_table.add_row(["# Tracks", len(mid.tracks)])
        #
        #
        #     for i, track in enumerate(mid.tracks):
        #         ptrack = ParserTrack(track, mid.ticks_per_beat)
        #         pretty_table.add_row(["", ""])
        #         default = ""
        #         if ptrack.signature.time_is_default:
        #             default = " *D"
        #         pretty_table.add_row(["Track Name", ptrack.name])
        #         pretty_table.add_row(["Ticks Per Beat", ptrack.signature.mid_ticks_per_beat])
        #         pretty_table.add_row(["Time Signature{0}".format(default), ptrack.signature.time_signature])
        #         pretty_table.add_row(["Clocks Per Click{0}".format(default), ptrack.signature.time_clocks_per_click])
        #         pretty_table.add_row(["Notated 32nd notes per beat{0}".format(default), ptrack.signature.time_32nds_per_beat])
        #         pretty_table.add_row(["Track Notes (4bars format)".format(default), ptrack.track_string])
        #
        #     print(pretty_table)
#            print()


        #pmid = pretty_midi.PrettyMIDI(f)
        #pmid.get_piano_roll(self)
        #for i in pmid.instruments:
        #    roll = i.get_piano_roll(1)
        #    chroma = i.get_chroma()
        #    for n in i.notes:
        #        pass

#    def prefs(self):
#        print(Locations().get_fullpretty())


            #table.add_row([file_name, len(mid.tracks), pmid.get_end_time(), ""])

#            pmid.get_piano_roll(self)
#            for i, track in enumerate(mid.tracks):
#                print('Track {}: {}'.format(i, track.name))
#                pmid.instruments
#                for msg in track:
#                    print(msg)



#    def tracks_old(self):

#        files = self.get_mid_files()

#        import mido
#        import pretty_midi
#        from prettytable import PrettyTable

#        table = PrettyTable()
#        table.field_names = ['Name', '# Tracks', 'Tempo', 'Beats']
#        table.align = "l"
#        for f in files:
#            pmid = pretty_midi.PrettyMIDI(f)

#            print (f)
#            mid = mido.MidiFile(f)

#            path_array = f.split('/')
#            file_name = path_array[len(path_array)-1]
#            table.add_row([file_name, len(mid.tracks), pmid.get_end_time(), ""])
# iterate through tracks
#            for i, track in enumerate(mid.tracks):
#                print('Track {}: {}'.format(i, track.name))

#                #for msg in track:
#                #    print(msg)

#        print(table)
#        print()
