
from fourbars.schema.asset import Asset as SchemaAsset
from fourbars.api.asset import Asset as ApiAsset
from fourbars.alive.locations import Locations

class Plan(object):

    sub_args = None
    locations = None
    api_asset = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args
        self.locations = Locations()
        self.api_asset = ApiAsset()
        print

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

    def plan_folder(self):

        if self.sub_args.d:
            self.locations.pwd = self.sub_args.d

        # TODO: iterate through all - 0 is for testing now
        files = self.locations.get_aif_files()

        for file in files:
            print (file)
            # # obtain md5 of file to be submitted
            # schema_asset = SchemaAsset()
            # schema_asset.get_org_md5(file)
            #
            # # check if md5 of file to be submitted exists in 4bars database
            # existing_guid = self.api_asset.get_md5_quick(schema_asset.org_md5)
            # if existing_guid:
            #     # item abort, already exists in 4bars database
            #     print("PLAN: Skipping ORG: {0}".format(existing_guid))
            #     continue
            # else:
            #     print("PLAN: Processing: {0}".format(file))