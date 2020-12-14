
from fourbars.ingest.transcode import Transcode
from fourbars.ingest.plan import Plan


class Ingest(object):

    sub_args = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args

    def transcode(self):
        Transcode(self.sub_args).transcode_folder()

    def plan(self):
        Plan(self.sub_args).plan_folder()

    def share(self):
        print("echo: 4bars ingest process (work in progress)")
        pass