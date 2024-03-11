from django import forms
from .models import Movies
class UserAddForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'slug','plot', 'budget', 'director', 'time', 'release_date', 'language', 'actors', 'genres','trailer', 'image']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Pop the 'user' argument from kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.added_by = self.user  # Assign the current user to the 'added_by' field
        if commit:
            instance.save()
        return instance
class UserEditForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'slug', 'plot', 'budget', 'director', 'time', 'release_date', 'language', 'actors', 'genres', 'trailer', 'image']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Pop the 'user' argument from kwargs
        # print(self.user)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.added_by = self.user  # Assign the current user to the 'added_by' field
        if commit:
            instance.save()
        return instance