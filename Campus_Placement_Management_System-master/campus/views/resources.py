from import_export import resources
from ..models import User
class studentResource(resources.ModelResource):
    class Meta:
        model = User