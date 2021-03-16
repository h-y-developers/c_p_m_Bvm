from import_export import resources
from ..models import student_data
class studentResource(resources.ModelResource):
    class Meta:
        model = student_data