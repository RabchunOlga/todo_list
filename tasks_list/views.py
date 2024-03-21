from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import (CreateView, DeleteView,
                                       UpdateView)
from django.views.generic.list import ListView

from tasks_list.models import Task


class TasksListView(LoginRequiredMixin, ListView):
    template_name = 'tasks_list/tasks.html'
    model = Task
    context_object_name = 'tasks'
    # login_url = 'users/login/'

    # def get_queryset(self):
    #     queryset = super(TasksListView, self).get_queryset()
    #     return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__contains=search_input)

        context['search_input'] = search_input

        return context

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks_list/task_update.html'
    model = Task
    fields = ['title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks:index')
    login_url = 'users/login/'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'tasks_list/task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:index')
    login_url = 'users/login/'

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tasks_list/task_update.html'
    model = Task
    fields = ['title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks:index')
    login_url = 'users/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)



