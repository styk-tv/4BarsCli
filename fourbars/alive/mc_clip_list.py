from fourbars.mid.mc_midi_list import McMidiList


# THIS CLASS IS TO PREPARE EXACT LIST OF CLIPS READY FOR ADDING
# NO ADDITIONAL WORK AFTER THIS CLASS
class McClipList(list):


    def __init__(self, in_sub_args):
        super().__init__()
        #self.extend(McMidiList(directory=in_sub_args.d))
        self.validate(McMidiList(directory=in_sub_args.d))
        pass

    def validate(self, in_midi_list):
        for midi_file in in_midi_list:
            for clip in midi_file.clips:
                if clip.playable:
                    self.append(clip)

# methods for serving different variations
