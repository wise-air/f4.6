from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecipeSerializer
from .models import Recipe


#Standart views
class RecipeListView(ListView):
    model = Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# API view
class RecipeView(APIView):
    def get(self, request):
        output = [
            {
                'id': output.id,
                'title': output.title,
                'description': output.description,
                'created_at': output.created_at,
                'updated_at': output.updated_at
            } for output in Recipe.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


