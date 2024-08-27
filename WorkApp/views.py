from django.shortcuts import render,redirect
from .models import School, ParentGuardian, Student, Course, Payment

def add_school(request):
    success_message = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        # Ma'lumotlarni modelga saqlash
        school = School(name=name, address=address, phone_number=phone_number)
        school.save()

        # Muvaffaqiyatli xabarni o'rnatish
        success_message = "Maktab muvaffaqiyatli qo'shildi!"

    return render(request, 'add_school.html', {'success_message': success_message})

def add_parent_guardian(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        relationship = request.POST.get('relationship')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        student_id = request.POST.get('student_id')

        # Talaba bilan bog'lash
        student = Student.objects.get(id=student_id)
        
        # Ma'lumotlarni saqlash
        parent_guardian = ParentGuardian(
            first_name=first_name,
            last_name=last_name,
            relationship=relationship,
            phone_number=phone_number,
            email=email,
            student=student
        )
        parent_guardian.save()

        return redirect('add_parent_guardian')  # Yaratilgandan so'ng shu sahifaga qaytarish

    students = Student.objects.all()
    return render(request, 'add_parent_guardian.html', {'students': students})

def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        credits = request.POST.get('credits')

        # Ma'lumotlarni saqlash
        course = Course(name=name, description=description, credits=credits)
        course.save()

        return redirect('add_course')  # Yaratilgandan so'ng shu sahifaga qaytarish

    return render(request, 'add_course.html')
def add_payment(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        amount = request.POST.get('amount')
        payment_date = request.POST.get('payment_date')
        payment_status = request.POST.get('payment_status')

        student = Student.objects.get(id=student_id)
        
        # Ma'lumotlarni saqlash
        payment = Payment(student=student, amount=amount, payment_date=payment_date, payment_status=payment_status)
        payment.save()

        return redirect('add_payment')  # Yaratilgandan so'ng shu sahifaga qaytarish

    students = Student.objects.all()
    return render(request, 'add_payment.html', {'students': students})