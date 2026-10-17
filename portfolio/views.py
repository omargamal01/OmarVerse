from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
def home(request):
    return render(request,"portfolio/home.html",{"featured_projects":Project.objects.filter(published=True,featured=True)[:3],"recent_projects":Project.objects.filter(published=True)[:6],"project_count":Project.objects.filter(published=True).count()})
def about(request):
    return render(request,"portfolio/about.html")
def projects(request):
    category=request.GET.get("category","").strip()
    items=Project.objects.filter(published=True)
    if category: items=items.filter(category=category)
    return render(request,"portfolio/projects.html",{"projects":items,"active_category":category,"categories":Project.CATEGORY_CHOICES})
def project_detail(request,slug):
    return render(request,"portfolio/project_detail.html",{"project":get_object_or_404(Project,slug=slug,published=True)})
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name","").strip()
        email=request.POST.get("email","").strip()
        subject=request.POST.get("subject","").strip()
        message=request.POST.get("message","").strip()
        if not all([name,email,subject,message]):
            messages.error(request,"Please complete every field.")
        else:
            messages.info(request,"Thanks for your message. Email delivery needs to be configured by the site owner; you can also contact Omar directly at gamalomar4321@gmail.com.")
            return redirect("contact")
    return render(request,"portfolio/contact.html")
