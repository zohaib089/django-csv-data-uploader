import csv,io
from django.shortcuts import render
from django.contrib import messages
from .models import User


def user_upload(request):
    template = "user_upload.html"

    if request.method == "GET":
        return render(request,template)

    csv_file = request.FILES['csv_file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for data in csv.reader(io_string, delimiter=',' , quotechar="|"):
        _, created = User.objects.update_or_create(
            codice_cliente = data[0],
            codice_fiscale = data[1],
            ragione_sociale = data[2],
            nome = data[3],
            indirizzo = data[4],
            cap = data[5],
            comune = data[6],
            provincia = data[7],
            codice_stato = data[8],
            email = data[9]
        )

    context = {}


    return render(request,template,context)    


