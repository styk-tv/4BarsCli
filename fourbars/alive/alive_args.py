import argparse
from fourbars.core.spawn import Spawn
from fourbars.alive.alive import ALive


class ALiveArgs(argparse.ArgumentParser):

    sub_args = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args
        super(ALiveArgs, self).__init__()

        self.usage = argparse.SUPPRESS
        self.add_help = False

        # if single (this) subarg, then only help
        if len(self.sub_args) < 2:
            self.help()
            return

        self.add_argument('live', help='Subcommand to run')
        self.add_argument('-d', action="store")

        args = self.parse_args(in_sub_args[1:])
        #args = self.parse_args(self.sub_args[1:2])

        alive = ALive(args)
        # fix to use word import on arg but import is a reserved name
        if args.live == "import":
            args.live = "limport"
        if not hasattr(alive, args.live):
            self.help()
            exit(1)

        getattr(alive, args.live)()

    def help(self):
        Spawn.help_desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

LIVE commands initialize relate to operations on Ableton Live. Example: 4bars live init

set commands:
    init        [WIP] initialize new song/set in current folder
    up          [WIP] start Live and load current project
    import      [WIP] import current folder mid files as clips into current project and track prefixed with 4BARS_
    record      [WIP] record MIDI track prefixed with 4BARS_ and collect recorded assets
    locations   show absolute paths to your Ableton installation
    help        this help menu""")