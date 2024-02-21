# syncchatroom/views.py
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from syncchat.models import Message  # Updated import for Message model
from syncchat.forms import MessageForm  # Updated import for MessageForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Add this line
from django.contrib.auth import login  # Add this line
from django.shortcuts import redirect
from django.http import JsonResponse
import json


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'syncchatroom/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        message = request.POST.get('message', '')
        # Broadcast the message to WebSocket consumers
        self.send_chat_message(message)
        return JsonResponse({'status': 'ok'})

    async def send_chat_message(self, message):
        # Send message to WebSocket
        await self.channel_layer.group_add(
            'chat_group',
            self.channel_name
        )

        await self.channel_layer.group_send(
            'chat_group',
            {
                'type': 'chat.message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        # Receive message from WebSocket
        message = event['message']

        # Send message to room group
        await self.send(text_data=json.dumps({
            'message': message,
        }))


class RegistrationView(TemplateView):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to the home page or any desired URL
        return self.render_to_response({'form': form})


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to the home page or any desired URL after login
        return self.render_to_response({'form': form})