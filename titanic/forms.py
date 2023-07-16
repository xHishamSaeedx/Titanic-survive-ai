from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import data

class DataForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Iterate over the fields and change the labels and help texts
        for field_name, field in self.fields.items():
            if field_name == 'name':  # Replace 'your_field_name' with the actual name of your field
                field.label = "Your Name"
            
            if field_name == 'pclass':  # Replace 'your_field_name' with the actual name of your field
                field.label = "Which Class would you want to travel in ?"
             
            if field_name == 'sex':  # Replace 'your_field_name' with the actual name of your field
                field.label = "Sex"
               
            if field_name == 'age':  # Replace 'your_field_name' with the actual name of your field
                field.label = "Age"
                
            if field_name == 'sibsp':  # Replace 'your_field_name' with the actual name of your field
                field.label = "How many siblings/spouses would you travel with"
                
            if field_name == 'parch':  # Replace 'your_field_name' with the actual name of your field
                field.label = "How many parents/children would you travel with"
                
            if field_name == 'embark':  # Replace 'your_field_name' with the actual name of your field
                field.label = "Which one would be your Port of Embarkation"        

    class Meta:
        model = data
        fields = ['name','pclass','sex','age','sibsp','parch','embark']

