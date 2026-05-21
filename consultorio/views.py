from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Paciente
from .models import Cita
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
     
    if request.method == "POST":

        form_type = request.POST.get("form_type")

        # ---------------- PACIENTE ----------------
        if form_type == "paciente":
            nombre = request.POST.get("nombre")
            telefono = request.POST.get("telefono")
            fecha = request.POST.get("fecha_nacimiento")

            Paciente.objects.create(
                nombre=nombre,
                telefono=telefono,
                fecha_nacimiento=fecha
            )

            messages.success(request, "Paciente guardado correctamente")
            return redirect('/')

        # ---------------- CITA ----------------
        elif form_type == "cita":
            paciente = request.POST.get("paciente")
            fecha_cita = request.POST.get("fecha_cita")
            hora = request.POST.get("hora")
            motivo = request.POST.get("motivo")

            Cita.objects.create(
                paciente=paciente,
                fecha_cita=fecha_cita,
                hora=hora,
                motivo=motivo
            )

            messages.success(request, "Cita guardada correctamente")
            return redirect('/')

    pacientes = Paciente.objects.all()
    citas = Cita.objects.all()
  
    return render(request, 'index.html', {
        'pacientes': pacientes,
        'citas': citas
    })
def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id_paciente=id)
    paciente.delete()

    messages.success(request, "Paciente eliminado correctamente")
    return redirect('/')
def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id_cita=id)
    cita.delete()

    messages.success(request, "Cita eliminada correctamente")
    return redirect('/')
def editar_paciente(request, id):

    paciente = Paciente.objects.get(id_paciente=id)

    if request.method == "POST":

        paciente.nombre = request.POST["nombre"]
        paciente.telefono = request.POST["telefono"]
        paciente.fecha_nacimiento = request.POST["fecha_nacimiento"]

        paciente.save()

        return redirect("/")

    return render(request, "editar_paciente.html", {
        "paciente": paciente
    })
def editar_cita(request, id):

    cita = Cita.objects.get(id_cita=id)

    if request.method == 'POST':

        cita.paciente = request.POST['paciente']
        cita.fecha_cita = request.POST['fecha_cita']
        cita.hora = request.POST['hora']
        cita.motivo = request.POST['motivo']

        cita.save()

        return redirect('/')
    return render(request, "editar_cita.html", {
        "cita": cita
    })