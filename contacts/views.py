from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import ContactForm
from .models import ContactSubmission


class ContactView(CreateView):
    model = ContactSubmission
    form_class = ContactForm
    template_name = "pages/contact.html"
    success_url = reverse_lazy("contacts:contact")

    def form_valid(self, form):
        messages.success(self.request, "Thanks. Your message has been saved and I will reply soon.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "page_title": "Contact | Your Name",
            "meta_description": "Contact me for full stack development work, design collaboration, or career opportunities.",
        }
