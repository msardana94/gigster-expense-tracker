from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


class ExpenseModel(models.Model):
	expense_id = models.AutoField("Expense ID",primary_key=True)
	description = models.TextField("Description")
	date_time = models.DateTimeField("Date Time")
	amount = models.DecimalField("Amount",max_digits=10, decimal_places=2)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')

	def get_list_expense(self, user):
		user = User.objects.get(email=user.email)
		list_expense = ExpenseModel.objects.filter(user_id=user.id)
		list_expense = list_expense.order_by('-date_time')
		return list_expense


	class Meta:
		verbose_name = "Expense"
		verbose_name_plural = "Expenses"