from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # this checks the renewal date

from django import forms


class RenewBookForm(forms.Form):
    """this is form for the librarian to add books """
    renewal_date = forms.DateField(
            help_text=" you must  Enter a date between now and 4 weeks (default would be 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # this will check the date is not past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        # this will allow the librarian allowed date
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        # this will return the initialized or clean data
        return data
