from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class ThankView(TemplateView):
    template_name = 'thanks.html'

class TestView(TemplateView):
    template_name = 'test.html'
