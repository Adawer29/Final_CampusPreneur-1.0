from django.views.generic import *

class HomePage(TemplateView):
    template_name='preneur.html'

class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'

class Arena1(TemplateView):
    template_name='arena1.html'
class Leaderboard(TemplateView):
    template_name='leaderboard.html'


class Redirection(TemplateView):
    template_name='homeredirect.html'
