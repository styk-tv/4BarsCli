import argparse
from fourbars.core.spawn import Spawn
from fourbars.mid.mc_midi_list import McMidiList


class MidArgs(argparse.ArgumentParser):

    sub_args = None

    parsed = None
    pretty_table = None

    def __init__(self, in_sub_args):
        super(MidArgs, self).__init__()

        self.usage = argparse.SUPPRESS
        self.add_help = False

        # some fs names have dashes
        if len(in_sub_args) > 1:
            if "-" in in_sub_args[1]:
                in_sub_args[1] = in_sub_args[1].replace('-', '_')

        self.sub_args = in_sub_args

        # if single (this) subarg, then only help
        if len(self.sub_args) < 2:
            self.help()
            return

        self.add_argument('mid', help='Subcommand to run')
        self.add_argument('-d', action="store")

        args = self.parse_args(in_sub_args[1:])

        mc_midi_list = McMidiList().load_midi_files(args)
        if not hasattr(mc_midi_list, args.mid):
            self.help()
            exit(1)

        getattr(mc_midi_list, args.mid)()

    def help(self):
        Spawn.help_desc()

        print("""Usage: 4bars [-version] [-help] <command> [args]

MID commands operate on MIDI (.mid) files current or specified (-d) directory. Example: 4bars mid notes

mid commands:
    tracks      list tracks of all midi-based files in current directory
    notes       list notes in tracks using 4bars notation
    help        this help menu

optional:
    -d          directory folder""")