# forms.py
from typing import Any
from django import forms
from .models import *

class AddStudentDetailForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = ['registerNo', 'studentName', 'standard']
        
class AddAttendanceForm(forms.Form):
    registerNo = forms.CharField(max_length=10, required=False)
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        registerNo = cleaned_data.get('registerNo')
        if not registerNo:
            raise forms.ValidationError('The registerNo field is required.')
        return cleaned_data

class RemoveStudentForm(forms.Form):
    registerNo = forms.CharField(max_length=10, required=False)
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        registerNo = cleaned_data.get('registerNo')
        if not registerNo:
            raise forms.ValidationError('The registerNo field is required.')
        return cleaned_data
    
class GetStudentDetailsForm(forms.ModelForm):
    class Meta: 
        model = StudentDetail
        fields = ['standard']

class GetStudentDetailsPDFForm(forms.ModelForm):
    class Meta: 
        model = StudentDetail
        fields = ['standard']

class UpdateStudentDetailsForm(forms.Form):
    registerNo = forms.CharField(max_length=10, required=False)
    studentName = forms.CharField()
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        registerNo = cleaned_data.get('registerNo')
        studentName = cleaned_data.get('studentName')
        if not registerNo and studentName:
            raise forms.ValidationError('The fields are required.')
        return cleaned_data

class UpdateStudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = ['registerNo', 'studentName']
        
class SetMarksForm(forms.Form):
    registerNo = forms.CharField(max_length=10, required=False)
    marks = forms.IntegerField()
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        registerNo = cleaned_data.get('registerNo')
        marks = cleaned_data.get('marks')
        if not registerNo and marks:
            raise forms.ValidationError('The fields are required.')
        return cleaned_data

class GetMarksForm(forms.ModelForm):
    class Meta: 
        model = StudentDetail
        fields = ['standard']
        
class GetMarksPDFForm(forms.ModelForm):
    class Meta: 
        model = StudentDetail
        fields = ['standard']

class GetRanksForm(forms.ModelForm):
    class Meta: 
        model = StudentDetail
        fields = ['standard']

class GetRanksPDFForm(forms.ModelForm):
    class Meta: 
        model = StudentDetail
        fields = ['standard']

class SelectStandardForm(forms.Form):
    standard = forms.ChoiceField(choices=[(8, '8'), (9, '9'), (10, '10')])

class SelectRegisterNoForm(forms.Form):
    registerNo = forms.CharField(max_length=10, required=False)
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        registerNo = cleaned_data.get('registerNo')
        if not registerNo:
            raise forms.ValidationError('The registerNo field is required.')
        return cleaned_data
