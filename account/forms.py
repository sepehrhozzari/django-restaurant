from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget = forms.TextInput(
            attrs={"placeholder": "نام کاربری"})
        self.fields["email"].widget = forms.TextInput(
            attrs={"placeholder": "ایمیل"})
        self.fields["password1"].widget = forms.TextInput(
            attrs={"placeholder": "پسورد"})
        self.fields["password2"].widget = forms.TextInput(
            attrs={"placeholder": "تکرار پسورد"})

        self.fields["email"].help_text = "برای تایید ثبت نام لینکی به این ایمیل ارسال میشود!"

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)

        if not user.is_superuser:
            self.fields["username"].disabled = True
            self.fields["is_chef"].disabled = True
            self.fields["email"].disabled = True

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "is_chef", "email", "profile_picture", "bio"]


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)

        self.fields["address"].required = True
        self.fields["city"].required = True
        self.fields["address"].help_text = "غذا هایی که سفارش میدهید به این آدرس فرستاده میشوند"
        self.fields["city"].help_text = "شهر هایی که ما درآنها سرویس میدهیم متاسفانه فعلا کم هستند"

    class Meta:
        model = User
        fields = ["address", "city"]
