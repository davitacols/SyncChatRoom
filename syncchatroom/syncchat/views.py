# syncchatroom/views.py
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Message  # Import Message model
from .forms import MessageForm  # Import MessageForm


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'syncchatroom/home.html'

    def get_queryset(self):
        return Message.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        context['messages'] = self.get_queryset()
        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return self.render_to_response(self.get_context_data())
        return self.render_to_response(self.get_context_data(form=form))
