from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import ProtectedError


class ObjectCreateMixin:
    model_form = None
    object_name = None
    object_url = None

    def get(self, request):
        model_form = self.model_form()
        context = {'model_form': model_form, 'object_name': self.object_name, 'object_url': self.object_url}
        return render(request, 'cinemas/add_object.html', context)

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            obj = bound_form.save()
            return redirect(obj)
        return HttpResponse('Bound form is not valid, maybe this object has already exist')


class ObjectEditMixin:
    model = None
    model_form = None

    def get(self, request, **kwargs):
        obj = self.model.objects.get(**kwargs)
        bound_form = self.model_form(instance=obj)
        return render(request, 'cinemas/edit_object.html', {'model_form': bound_form, 'model': obj})

    def post(self, request, **kwargs):
        obj = self.model.objects.get(**kwargs)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            edit_obj = bound_form.save()
            return redirect(edit_obj)
        return HttpResponse('Bound form is not valid')


class ObjectDeleteMixin:
    model = None
    redirect_url = None

    def get(self, request, **kwargs):
        obj = self.model.objects.get(**kwargs)
        return render(request, 'cinemas/delete_object.html', {'model': obj})

    def post(self, request, **kwargs):
        obj = self.model.objects.get(**kwargs)
        try:
            obj.delete()
        except ProtectedError:
            return HttpResponse('it is related object, removal was blocked')
        return redirect(self.redirect_url)



























