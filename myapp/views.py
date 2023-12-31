from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Patient_Records
from .models import Appointment_Schedule
from .forms import Patient_Records_Form
from .forms import Appointment_Schedule_Form
from .forms import Patient_Records_Form_Update
from .forms import Appointment_Schedule_Form_Update
from .forms import Search_Form, Search_Date
from datetime import date
import datetime

def dashboard_create(request):
    return render(request, 'myapp/dashboard_create.html')

def dashboard_view(request):
    return render(request, 'myapp/dashboard_view.html')

def dashboard_update(request):
    return render(request, 'myapp/dashboard_update.html')

def dashboard_index(request):
    return render(request, 'myapp/dashboard_index.html')


def patient_record_view(request):
    patient_records = Patient_Records.objects.all()
    return render(request, 'myapp/patient_record_view.html', {'patient_records' : patient_records})

def patient_record_detail(request, pk):
    patient_record = get_object_or_404(Patient_Records, pk=pk)
    return render(request, 'myapp/patient_record_detail.html', {'patient_record': patient_record})

def patient_record_search(request):

    if request.method == 'POST':
        form = Search_Form(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            patient_records = Patient_Records.objects.filter(last_name__icontains=last_name,first_name__icontains=first_name)

            context = {'patient_records': patient_records}
            return render(request, 'myapp/patient_record_search_results.html', context)
    else:
        form = Search_Form()

    return render(request, 'myapp/patient_record_search.html', {'form': form})

def patient_record_create(request):
    if request.method == 'POST':
        form = Patient_Records_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_record_view')
    else:
        form = Patient_Records_Form()

    return render(request, 'myapp/patient_record_form.html', {'form': form})

def patient_record_update(request, pk):
    patient_update = get_object_or_404(Patient_Records, pk=pk)
    form = Patient_Records_Form_Update(request.POST or None, instance = patient_update)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('patient_record_view')
        
    return render(request, 'myapp/patient_record_update.html', {'form': form, 'patient_update' : patient_update})


def appointment_schedule_view(request):
    appointment_schedules = Appointment_Schedule.objects.all()
    return render(request, 'myapp/appointment_schedule_view.html', {'appointment_schedules' : appointment_schedules})

def appointment_schedule_view_present(request):
    current_date = date.today()
    sort_by = request.GET.get('sort')
    

    if sort_by == 'view':
        #Sorts by Date
        appointments = Appointment_Schedule.objects.filter(current_appointment_schedule__gte=current_date).order_by('current_appointment_schedule', 'appointment_time')
    elif sort_by == 'name':
        #Sorts by Name
        appointments = Appointment_Schedule.objects.filter(current_appointment_schedule__gte=current_date).order_by('patient_id_id__last_name', 'patient_id_id__first_name' , 'current_appointment_schedule')
    else:
        #This first one gets displayed is appointments for TODAY ONLY, AS IN THE DATE TODAY
        appointments = Appointment_Schedule.objects.filter(current_appointment_schedule__range=(current_date, current_date))
 
    context = {'appointments': appointments}
    return render(request, 'myapp/appointment_schedule_view_present.html', context)

def appointment_schedule_search(request):
    return render(request, 'myapp/appointment_schedule_search.html')

def appointment_schedule_search_date(request):
    form1 = Search_Date(request.GET)
    appointments = []
    if form1.is_valid():
        date = form1.cleaned_data['date']

        appointments = Appointment_Schedule.objects.filter(current_appointment_schedule=date)
    return render(request, 'myapp/appointment_schedule_search_date.html', {'form1': form1, 'appointment_schedules': appointments})

def appointment_schedule_search_name(request):
    form = Search_Form(request.GET or None)
    appointment_schedules = []

    if form.is_valid():
        last_name = form.cleaned_data['last_name']
        first_name = form.cleaned_data['first_name']
        patient_records = Patient_Records.objects.filter(last_name__icontains=last_name, first_name__icontains=first_name)
        appointment_schedules = Appointment_Schedule.objects.filter(patient_id__in=patient_records)

    context = {
        'form': form,
        'appointment_schedules': appointment_schedules
    }
    return render(request, 'myapp/appointment_schedule_search_name.html', context)


def appointment_schedule_detail(request, pk):
    appointment_schedule = get_object_or_404(Appointment_Schedule, pk=pk) 
    return render(request, 'myapp/appointment_schedule_detail.html', {'appointment_schedule' : appointment_schedule})



def appointment_schedule_create(request):
    """Add solution for the problem where an appointment time is already occupied, it will verify"""
    if request.method == 'POST':
        form = Appointment_Schedule_Form(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            patient_id = form.cleaned_data['patient_id']
            last_appointments = Appointment_Schedule.objects.filter(patient_id=patient_id).order_by('-current_appointment_schedule').first()


            appointment_date = form.cleaned_data['current_appointment_schedule']
            appointment_time = form.cleaned_data['appointment_time']

            #Sets the value of last_appointment to the previous current_appointment_schedule value, also it sets the status to pending
            if last_appointments:
                appointment.last_appointment = last_appointments.current_appointment_schedule
                appointment.status = "Pending"
            appointment_exists = Appointment_Schedule.objects.filter(
                current_appointment_schedule=appointment_date,
                appointment_time=appointment_time
            ).exists()
            
            #checks if the inputted appointment time on that appointment date already exists
            if appointment_exists:
                form.add_error('appointment_time', 'Appointment already exists for this date and time.')
            
            # Checks if the current appointment schedule is older than the last appointment
            patient_id = form.cleaned_data['patient_id']
            last_appointment = Appointment_Schedule.objects.filter(
                patient_id=patient_id
            ).order_by('-current_appointment_schedule').first()
            
            if last_appointment and appointment_date < last_appointment.current_appointment_schedule:
                form.add_error('current_appointment_schedule', 'Current appointment schedule is older than the last appointment.')
            
            if form.errors:
                return render(request, 'create_appointment.html', {'form': form})
            
            # Save the appointment if all validations pass
            form.save()

            appointment.save()
            return redirect('appointment_schedule_view_present') 
    else:
        form = Appointment_Schedule_Form()

    return render(request, 'myapp/appointment_schedule_form.html', {'form': form})

def fetch_latest_appointment_schedule(request, patient_id):
    last_appointment = Appointment_Schedule.objects.filter(patient_id=patient_id).order_by('-current_appointment_schedule').first()
    if last_appointment:
        latest_schedule = last_appointment.current_appointment_schedule
    else:
        latest_schedule = None
    return JsonResponse({'last_appointment_schedule': latest_schedule.isoformat() if latest_schedule else None})

def appointment_schedule_update(request, pk):
    appointment_update = get_object_or_404(Appointment_Schedule, pk=pk)
    form = Appointment_Schedule_Form_Update(request.POST or None, instance = appointment_update)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('appointment_schedule_view')
        
    return render(request, 'myapp/appointment_schedule_form_update.html', {'form': form, 'appointment_update' : appointment_update})



def product_update(request, pk):
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/product_form.html', {'form': form, 'product': product})
    """

def product_delete(request, pk):
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'myapp/product_confirm_delete.html', {'product': product})
    """
# Create your views here.
