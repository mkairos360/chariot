from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, resolve, path
import re
from django.http import HttpResponse

from dashboard.views import runurl


class ChurchAuthMiddleware:
    def __init__(self, get_response):
        # self.whitelisted_urls = '/dashboard/factual/limiting/(?P<token>[^/]+)\\Z'
        self.whitelisted_urls = '/accounts/confirm-email/(?P<token>[^/]+)\\Z'

        self.exception_urls = list([
            reverse('admin:login'),
            reverse('login'),
            reverse('register_user'),
        ])
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.user.is_authenticated:
            if request.path not in self.exception_urls:
                return self.utilityfunc(response)
        return response

    def utilityfunc(self, rpath):
        if rpath in self.exception_urls:
            return redirect(rpath)
        else:
            return redirect('login')

    def utilityfunc_wl(self, rpath):
        return redirect(rpath)