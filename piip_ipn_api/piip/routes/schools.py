from piip.command.school import get_all_schools
from piip.routes.resource import PIIPResource
from piip.schema.school import SchoolSchema


class Schools(PIIPResource):
    def get(self):
        return SchoolSchema(many=True).dump(get_all_schools())
