from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
    students=Student.objects.all()
    return render(request,'allstudents.html',{'students':students})

def getStudentById(request,id):
    student=get_object_or_404(Student,id=id)
    return render(request,'studentdetail.html',{'student':student,'id':id})

def addStudent(request):
    if request.method =='POST':
        form=StudentForm(request.POST) # It is taking the data from the form and creating the object of Student.
        if form.is_valid():
            student=form.save(commit=False) 
            # Default value of commit is "True".
            # This can be useful if you need to modify the instance or perform additional validation before saving it. 
            # Once you are done with any additional processing, you can call student(instance).save()
            student.save()
            return redirect('studentlist')
    else:
        form=StudentForm()
    return render(request,'addstudent.html',{'form':form})

def updateStudent(request,id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('studentlist')
    return render(request, 'addstudent.html', {'form': form})

def deleteStudent(request,id):
    student=get_object_or_404(Student,id=id)
    student.delete()
    return redirect('studentlist')

def deleteAllStudents(request):
    if request.method == 'POST':
        Student.objects.all().delete()
        return redirect('studentlist')
    return render(request, 'deleteallstudents.html')