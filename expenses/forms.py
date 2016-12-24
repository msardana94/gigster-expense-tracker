from django import forms
from .models import ExpenseModel


class ExpenseCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ExpenseCreateForm, self).__init__(*args, **kwargs)
        self.fields['date_time'].widget.attrs.update({'data-provide': 'datepicker', 'data-date-format': 'YYYY-MM-DD HH:mm', 'readonly': True})
        self.fields['amount'].widget.attrs.update({'max': 10000000})

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "placeholder": self.fields[field].label,
                "class": "form-control",
                'required': self.fields[field].required
            })

    class Meta:
        model = ExpenseModel
        fields = ['description', 'date_time', 'amount']

class ExpenseUpdateForm(forms.ModelForm):
    expense_id = forms.IntegerField('Expense ID',min_value=1, required=True)
    def __init__(self, *args, **kwargs):
        super(ExpenseUpdateForm, self).__init__(*args, **kwargs)
        self.fields['date_time'].widget.attrs.update({'data-provide': 'datepicker', 'data-date-format': 'YYYY-MM-DD HH:mm', 'readonly': True, 'required':False})
        self.fields['description'].widget.attrs.update({'max': 10000000,'required':False})
        self.fields['amount'].widget.attrs.update({'required':False})

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "placeholder": self.fields[field].label,
                "class": "form-control",
                'required': self.fields[field].required
            })

    class Meta:
        model = ExpenseModel
        fields = ['description', 'date_time', 'amount','expense_id']

class ExpenseDeleteForm(forms.ModelForm):
    expense_id = forms.IntegerField('Expense ID',min_value=1, required=True)
    def __init__(self, *args, **kwargs):
        super(ExpenseDeleteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "placeholder": self.fields[field].label,
                "class": "form-control",
                'required': self.fields[field].required
            })

    class Meta:
        model = ExpenseModel
        fields = ['expense_id']