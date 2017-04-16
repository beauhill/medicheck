from django.shortcuts import render

from patients.models import Patient,Profile,Note
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User


from .forms import NoteForm




# Create your views here.


def submit_patient(request, id):
    doctor = User.objects.get(pk=id)

    patient = Patient.objects.get(pk=request.session.get('patient_target'))



    #patient.index_id = doctor

    Patient.objects.create(index_id=doctor.id, first_name=patient.first_name, last_name=patient.last_name, ethnicity=patient.ethnicity, weight=patient.weight, height=patient.height, gender= patient.gender, age = patient.age )

    return render(request, "profile/home.html", {})


def share_patient(request, id):
    patient = Patient.objects.get(pk=id)
    doctors = User.objects.all().exclude(pk= request.user.id)

    request.session["patient_target"] = patient.id


    return render(request, "profile/share.html", {'patient': patient, 'doctors' : doctors })


def delete_post(request):
    query = request.GET.get('id')
    pat = Note.objects.get(pk=query) # patient_id = request.session.get('patient_target') )
    pat.delete()

    data = {
'delete' : True
    }

    return JsonResponse(data)


def edit_post(request):
    title = request.GET.get('title', None)
    body = request.GET.get('body', None)
    query = request.GET.get('query', None)



    note = Note.objects.get(pk=query)  # patient_id = request.session.get('patient_target') )

    note.note = title
    note.message= body

    note.save()



    data = {
    'new_note' : note.note,
    'new_message' : note.message,
    'id' : query,
    }

    return JsonResponse(data)


def home(request):
    if request.user.is_authenticated() is False:
        return render(request, 'index.html')

    profile = Profile.objects.get(pk=request.user.id)


    sort = request.GET.get('sort', 1)
    patients = Patient.objects.all().filter(index_id=1).order_by("last_name")
    page = request.GET.get('page', 1)
    paginator = Paginator(patients, 10)


    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


     #x = Patient.objects.all().filter(index_id=1)

    context = { "user" : request.user,
                "patients" : patients,
                "profile" : profile,
                         }
    return render(request, 'profile/home.html', context)


def detail(request, id ):

    patient = Patient.objects.get(pk=id)
    request.session["patient_target"] = id

    add_notes = Note.objects.filter(note_type__startswith="Additional Notes", patient_id=id)
    per_notes = Note.objects.filter(note_type__startswith="Prescription", patient_id=id)
    ct_notes = Note.objects.filter(note_type__startswith="CT", patient_id=id)
    bw_notes = Note.objects.filter(note_type__startswith="Blood", patient_id=id)
    all_notes =  Note.objects.filter(note_type__startswith="Allergy", patient_id=id)






    context = { "param" : id,
                "patient": patient,
                "add_notes": add_notes,
                "per_notes": per_notes,
                "ct_notes": ct_notes,
                "bw_notes": bw_notes,
                "all_notes": all_notes,}
    return render(request, 'profile/patient.html', context)



def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.last_modified = timezone.now()
            post.date_ended = timezone.now()
            post.date_started = timezone.now()
            pat = Patient.objects.get(pk=request.session.get('patient_target'))
            post.patient = pat
            post.save()
            return redirect('id', id=request.session.get('patient_target'))
    else:
        form = NoteForm()
        return render(request, "patients/note_new.html", {'form': form})











    return render(request, "patients/note_new.html", {'form': form})
