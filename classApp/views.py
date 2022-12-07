from django.shortcuts import render,redirect,HttpResponse
from .models import StudentInfo
from weasyprint import HTML
import tempfile
from django.template.loader import render_to_string
import datetime
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def exam(request):
    return render(request,'exam.html')

def add(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST['name']
        nickname = request.POST['nickname']
        roll = request.POST['roll']
        address = request.POST['address']
        phone = request.POST['phone']
        info = StudentInfo.objects.create(image = image,name= name,nickname = nickname,roll = roll,address = address,phone =phone)
        info.save()
        return redirect('home')
    return render(request,'add.html')

def profile(request):
    data = StudentInfo.objects.all()
    return render(request,'profile.html',{'data':data})


def export_pdf(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename = members' + \
        str(datetime.datetime.now()) + '.pdf'
    
    response['Content-Transfer-Encoding'] = 'binary'
    students = StudentInfo.objects.all()

    html_string = render_to_string('export_pdf.html',{'students':students})
    html = HTML(string = html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output = open(output.name,'rb')
        response.write(output.read())
    return response

def my_view(request):
    messages.add_message(request,  'A serious error occurred.')