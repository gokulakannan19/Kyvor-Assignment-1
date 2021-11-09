from django.forms import ModelForm
from .models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control', })
