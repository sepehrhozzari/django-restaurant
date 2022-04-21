from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import BookTable


class BookTableForm(forms.ModelForm):
    phone_number = forms.CharField(
        help_text="برای هماهنگی شماره تلفن الزامی میباشد")
    guest = forms.CharField(label="تعداد مهمان ها")

    def clean_date(self):
        date = self.cleaned_data.get("date")
        next_day = timezone.now() + timedelta(days=1)
        if not date >= next_day:
            raise forms.ValidationError(
                "تاریخ درخواست شده حداقل باید برای ۱ روز بعد باشد")
        return date

    class Meta:
        model = BookTable
        fields = ['phone_number', 'date', 'guest']
