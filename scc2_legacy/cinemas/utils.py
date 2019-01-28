# from django.shortcuts import render
# from .models import *
#
# class FilterMixin():
#     model = None
#     template = None
#
#     def get(self, request, **kwargs):
#         obj = self.model.objects.values(kwargs.keys())
#         return render(request, self.template, context={})