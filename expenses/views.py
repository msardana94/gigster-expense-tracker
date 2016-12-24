from .forms import ExpenseCreateForm, ExpenseUpdateForm, ExpenseDeleteForm
from .models import ExpenseModel
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
import traceback
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import connection

@method_decorator(login_required, name='dispatch')
class CreateExpense(CreateView):
    login_url = reverse_lazy('login')
    model = ExpenseModel
    form_class = ExpenseCreateForm
    template_name = "create.html"
    success_url = reverse_lazy('create')

    def get_form(self, form_class=None):
        form_expense = super(CreateExpense, self).get_form(form_class)
        return form_expense

    def get_context_data(self, **kwargs):
		context = super(CreateExpense, self).get_context_data(**kwargs)
		context.update({
			'type': "Create",
			'urlval':'create'
			})
		return context



    def form_valid(self, form):
        try:
            create_exp = form.save(commit=False)
            create_exp.user_id = User.objects.get(pk=self.request.user.pk)
            create_exp.save()
            messages.success(self.request, 'Expense created successful')
            return redirect(reverse('create'))
        except Exception, e:
            print traceback.format_exc()
            messages.error(self.request, "%s" % str(e))
        print self
        return redirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class GetExpense(TemplateView):
    login_url = reverse_lazy('login')
    template_name = "read.html"
    model = ExpenseModel

    def get(self, request, *args, **kwargs):
        context = locals()
        expense = ExpenseModel()
        context['queryset'] = expense.get_list_expense(self.request.user)
        return render_to_response(self.template_name, context, context_instance=RequestContext(request))

@method_decorator(login_required, name='dispatch')
class UpdateExpense(CreateView):
	login_url = reverse_lazy('login')
	model = ExpenseModel
	form_class = ExpenseUpdateForm
	template_name = "create.html"
	success_url = reverse_lazy('update')

	def get_form(self, form_class=None):
	    form_expense = super(UpdateExpense, self).get_form(form_class)
	    return form_expense

	def get_context_data(self, **kwargs):
		context = super(UpdateExpense, self).get_context_data(**kwargs)
		context.update({
			'type': "Update",
			'urlval':'update'
			})
		return context
	def form_valid(self, form):
		try:
			# create_exp = form.save()
			# print form
			# print form.cleaned_data['expense_id']
			create_exp = get_object_or_404(ExpenseModel,pk=form.cleaned_data['expense_id'])
			if create_exp:
				if form.cleaned_data['date_time']:
					create_exp.date_time=form.cleaned_data['date_time']
				if form.cleaned_data['description']:
					create_exp.description=form.cleaned_data['description']
				if form.cleaned_data['amount']:
					create_exp.amount = form.cleaned_data['amount']
				create_exp.save()
				messages.success(self.request, 'Expense updated successful')
				return redirect(reverse('update'))
			else:
				message.error(self.request, 'Invalid Expense ID')
		except Exception, e:
			print traceback.format_exc()
			messages.error(self.request, "%s" % str(e))
			print self
		return redirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class DeleteExpense(CreateView):
	login_url = reverse_lazy('login')
	template_name = "create.html"
	model = ExpenseModel
	success_url = reverse_lazy('delete')
	form_class = ExpenseDeleteForm

	def get_form(self, form_class=None):
	    form_expense = super(DeleteExpense, self).get_form(form_class)
	    return form_expense

	def get_context_data(self, **kwargs):
		context = super(DeleteExpense, self).get_context_data(**kwargs)
		context.update({
			'type': "Delete",
			'urlval':'delete'
			})
		return context

	def form_valid(self,form):
		try:
			create_exp = ExpenseModel.objects.get(pk=form.cleaned_data['expense_id'])
			if create_exp:
				create_exp.delete()
				messages.success(self.request, 'Expense deleted!')
				return redirect(reverse('delete'))
			else:
				message.error(self.request, 'Invalid Expense ID')
		except Exception, e:
			print traceback.format_exc()
			messages.error(self.request, "%s" % str(e))
			# print self
		return redirect(self.get_success_url())

# def GetWeeklyAggregate():
# 	cursor = connection.cursor()
# 	cursor.execute(" SELECT WEEK(`date_time`) AS 'week', SUM(amount) AS 'Avg_Expense' FROM %s GROUP BY WEEK(`date_time`) ORDER BY WEEK(`date_time`)" % EventOccurrence._meta.db_table, [])

# 	data = []
# 	results = cursor.fetchall()
# 	for i, row in enumerate(results[:-1]):
# 	    data.append(row)

# 	    week = row[0] + 1
# 	    next_week = results[i+1][0]
# 	    while week < next_week:
# 	        data.append( (week, 0) )
# 	        week += 1
# 	data.append( results[-1] )

# 	print data
		

	