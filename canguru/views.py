from django.shortcuts import render, redirect
from .models import Comment, LegendaryKangaroo, KangarooType
from .forms import CommentForm, LegendaryKangarooForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
  comment = Comment.objects.all()
  legendary_kangaroo = LegendaryKangaroo.objects.all()
  kangaroo_type = KangarooType.objects.all()
  
  context = {
    "comments": comment, 
    "legendary_kangaroos": legendary_kangaroo, 
    "kangaroo_types": kangaroo_type, 
  }
  
  return render(request, "home.html", context)


@login_required
def add_comment(request):
  form = CommentForm()
  
  context = {
    "action": "Adicionar",
    "form": form
  }
  
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      form.save()

    return redirect("home")
  return render(request, "comment_form.html", context)


@login_required
def add_legendary_kangaroo(request):
  form = LegendaryKangarooForm
  
  context = {
    "action": "Adicionar",
    "form": form
  }
  
  if request.method == "POST":
    form = LegendaryKangarooForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect("home")  
  return render(request, "legendary_kangaroo_form.html", context)


@login_required
def update_comment(request, id):
  comment = Comment.objects.get(id = id)
  
  if request.method == "GET":
    form = CommentForm(instance = comment)
    context = {
      "action": "Atualizar",
      "comment": comment,
      "form": form
    }
    return render(request, "comment_form.html", context)
    
  elif request.method == "POST":
    form = CommentForm(request.POST, instance = comment)
    context = {
      "action": "Atualizar",
      "comment": comment,
      "form": form
    }
    if form.is_valid():
      form.save()
      return redirect("home")  
    return render(request, "comment_form.html", context)


@login_required
def update_legendary_kangaroo(request, id):
  legendary_kangaroo = LegendaryKangaroo.objects.get(id = id)

  if request.method == "GET":
    form = LegendaryKangarooForm(instance = legendary_kangaroo)
    context = {
      "action": "Atualizar",
      "legendary_kangaroo": legendary_kangaroo,
      "form": form
    }
    return render(request, "legendary_kangaroo_form.html", context)
    
  elif request.method == "POST":
    form = LegendaryKangarooForm(request.POST, instance = legendary_kangaroo)
    context = {
      "action": "Atualizar",
      "legendary_kangaroo": legendary_kangaroo,
      "form": form
    }
    if form.is_valid():
      form.save()
      return redirect("home")  
  return render(request, "legendary_kangaroo_form.html", context)


@login_required
def delete_comment(request, id):
  comment = Comment.objects.get(id = id)
  context = {
    "comment": comment
  }
  
  if request.method == "POST":
    if "confirm" in request.POST: 
      comment.delete()
      
    return redirect("home")
  return render(request, "delete_comment.html", context)


@login_required
def delete_legendary_kangaroo(request, id):
  legendary_kangaroo = LegendaryKangaroo.objects.get(id = id)
  context = {
    "legendary_kangaroo": legendary_kangaroo
  }
  
  if request.method == "POST":
    if "confirm" in request.POST: 
      legendary_kangaroo.delete()
      
    return redirect("home")
  return render(request, "delete_legendary_kangaroo.html", context)


def create_user(request):
  context={
    "action": "Adicionar"
  }
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"], 
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "registration/user_form.html", context)


@login_required
def update_user(request, id):
  user = User.objects.get(id = id)

  if request.method == "GET":
    form = UserForm(instance = user)
    context = {
      "action": "Atualizar",
      "user": user,
      "form": form
    }
    return render(request, "registration/update_user_form.html", context)
    
  elif request.method == "POST":
    form = UserForm(request.POST, instance = user)
    context = {
      "action": "Atualizar",
      "user": user,
      "form": form
    }
    if form.is_valid():
      form.save()
      return redirect("home")  
  return render(request, "registration/update_user_form.html", context)
