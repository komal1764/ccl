from django.shortcuts import render,redirect,get_object_or_404
from .models import NoteModel
from .forms import NoteForm

def home(request):
	data = NoteModel.objects.all().order_by("-dt")
	return render(request,"home.html",{"data":data})

def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "create.html", {"fm": form, "msg": "Form is invalid. Check your inputs."})
    else:
        form = NoteForm()
    return render(request, "create.html", {"fm": form})

def edit(request,id):
	d = NoteModel.objects.get(id=id)
	if request.method == "POST":
		data = NoteForm(request.POST,instance=d)
		if data.is_valid():
			data.save()
			return redirect("home")
		else:
			msg = "check issue"
			return redirect(request,"edit.html",{"fm":data})
	else: 
		fm = NoteForm(instance=d)
		return render(request,"edit.html",{"fm":fm})

def delete(request, id):
    d = get_object_or_404(NoteModel, id=id)
    d.delete()
    return redirect("home")