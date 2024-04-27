import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,"login index.html")

def admin_home(request):
    return render(request,"Admin/home index.html")

def authority_home(request):
    return render(request,"authority/home index.html")

def login_post(request):
    username=request.POST["textfield"]
    password=request.POST["textfield2"]
    log=Login.objects.filter(username=username,password=password)
    if log.exists():
        log1=Login.objects.get(username=username,password=password)
        request.session['lid']=log1.id
        if log1.type=='admin':
            return HttpResponse('''<script>alert('welcome');window.location='/myapp/admin_home/'</script>''')
        elif log1.type=='authority':
            return HttpResponse('''<script>alert('welcome');window.location='/myapp/authority_home/'</script>''')
        else:
            return HttpResponse('''<script>alert('Does not Match USername or password');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location="/myapp/login/"</script>''')


def admin_add_authority(request):
    return render(request,"Admin/add authority.html")

def admin_add_authority_post(request):
    Name=request.POST["textfield"]
    DOB=request.POST["textfield2"]
    Gender=request.POST["radio"]
    Email=request.POST["textfield3"]
    ph_no=request.POST["textfield4"]

    lobj=Login()
    lobj.username=Email
    lobj.password=ph_no
    lobj.type='authority'
    lobj.save()

    aobj=Authority()
    aobj.name=Name
    aobj.dateofbirth=DOB
    aobj.gender=Gender
    aobj.email=Email
    aobj.phone=ph_no
    aobj.LOGIN=lobj
    aobj.save()

    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_home/'</script>''')

def edit_authority(request,id):
    res=Authority.objects.get(pk=id)
    return render(request,"Admin/edit authority.html",{'data':res})

def edit_authority_post(request):
    id=request.POST['id']
    Name = request.POST["textfield"]
    DOB = request.POST["textfield2"]
    Gender = request.POST["radio"]
    Email = request.POST["textfield3"]
    ph_no = request.POST["textfield4"]

    #lobj = Login()
    #lobj.username = Email
    #lobj.password = ph_no
    #lobj.type = 'authority'
    #lobj.save()

    aobj = Authority.objects.get(pk=id)
    aobj.name = Name
    aobj.dateofbirth = DOB
    aobj.gender = Gender
    aobj.email = Email
    aobj.phone = ph_no
    #aobj.LOGIN = lobj
    aobj.save()

    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_view_authority/'</script>''')


def admin_Add_course(request):
    obj=Department.objects.all()
    return render(request,"Admin/Add course.html",{'data':obj})

def admin_Add_course_post(request):
    Course_name=request.POST["textfield"]
    Dept_name=request.POST["select"]

    cobj=Course()
    cobj.coursename=Course_name
    cobj.DEPARTMENT_id=Dept_name
    cobj.save()

    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_view_authority/'</script>''')

def edit_course(request,id):
    obj=Department.objects.all()
    res=Course.objects.get(pk=id)
    return render(request,"Admin/edit course.html",{'data':res,'data1':obj})

def edit_course_post(request):
    id=request.POST['id']
    Course_name=request.POST["textfield"]
    Dept_name = request.POST["select"]
    cobj=Course.objects.get(pk=id)
    cobj.coursename=Course_name
    cobj.DEPARTMENT_id = Dept_name
    cobj.save()
    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_view_course/'</script>''')

def admin_Add_dept(request):
    return render(request,"Admin/Add dept.html")

def admin_Add_dept_post(request):
    Department_name=request.POST["textfield"]

    dobj=Department()
    dobj.departmentname=Department_name
    dobj.save()

    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_home/'</script>''')

def edit_dept(request,id):
    res=Department.objects.get(pk=id)
    return render(request,"Admin/edit dept.html",{'data':res})

def edit_dept_post(request):
    id=request.POST['id']
    Department_name=request.POST["textfield"]
    dobj=Department.objects.get(pk=id)
    dobj.departmentname=Department_name
    dobj.save()
    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_view_dept/'</script>''')



def admin_Add_staff(request):
    obj = Department.objects.all()
    return render(request,"Admin/add staff.html",{'data':obj})

def admin_Add_staff_post(request):
    Name = request.POST["textfield"]
    DOB = request.POST["textfield2"]
    Gender = request.POST["radio"]
    Dept_name = request.POST["select"]
    Email = request.POST["textfield3"]
    Ph_no = request.POST["textfield5"]
    place = request.POST["textfield6"]
    post = request.POST["textfield7"]
    pin = request.POST["textfield8"]
    dist = request.POST["textfield9"]
    photo = request.FILES['photo']
    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fn = fs.save(date, photo)
    path = fs.url(date)

    lobj = Login()
    lobj.username = Email
    lobj.password = Ph_no
    lobj.type = 'staff'
    lobj.save()

    sobj=Staff()
    sobj.name=Name
    sobj.dateofbirth=DOB
    sobj.gender=Gender
    sobj.email=Email
    sobj.phone=Ph_no
    sobj.place=place
    sobj.post=post
    sobj.pin=pin
    sobj.dist=dist
    sobj.photo = path
    sobj.DEPARTMENT_id=Dept_name
    sobj.LOGIN=lobj
    sobj.save()


    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_home/'</script>''')

def edit_staff(request,id):
    obj = Department.objects.all()
    res = Staff.objects.get(pk=id)
    return render(request, "Admin/edit staff.html", {'data': res,'data1':obj})

def edit_staff_post(request):
    id = request.POST['id']
    Name = request.POST["textfield"]
    DOB = request.POST["textfield2"]
    Gender = request.POST["radio"]
    Dept_name = request.POST["select"]
    Email = request.POST["textfield3"]
    Ph_no = request.POST["textfield5"]
    place = request.POST["textfield6"]
    post = request.POST["textfield7"]
    pin = request.POST["textfield8"]
    dist = request.POST["textfield9"]
    sobj=Staff.objects.get(pk=id)

    if 'photo' in request.FILES:

        photo = request.FILES['photo']
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fn = fs.save(date, photo)
        path = fs.url(date)
        sobj.photo = path
        sobj.save()

    # lobj = Login()
    # lobj.username = Email
    # lobj.password = Ph_no
    # lobj.type = 'staff'
    # lobj.save()

    sobj.name=Name
    sobj.dateofbirth=DOB
    sobj.gender=Gender
    sobj.email=Email
    sobj.phone=Ph_no
    sobj.place=place
    sobj.post=post
    sobj.pin=pin
    sobj.dist=dist
    sobj.DEPARTMENT_id=Dept_name
    # sobj.LOGIN=lobj
    sobj.save()


    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_view_staff/'</script>''')

def admin_add_student(request):
    obj= Course.objects.all()
    return render(request,"Admin/add student.html",{'data':obj})

def admin_add_student_post(request):
    Name=request.POST["textfield"]
    DOB=request.POST["textfield2"]
    Gender=request.POST["radio"]
    Course=request.POST["select"]
    Email=request.POST["textfield3"]
    Ph_no=request.POST["textfield4"]
    place=request.POST["textfield5"]
    post=request.POST["textfield6"]
    pin=request.POST["textfield7"]
    dist=request.POST["textfield8"]
    guardian_name=request.POST["textfield9"]
    guardian_Phone=request.POST["textfield10"]
    guardian_email=request.POST["textfield11"]
    photo=request.FILES['photo']
    from datetime import datetime
    date=datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
    fs=FileSystemStorage()
    fn=fs.save(date,photo)
    path=fs.url(date)


    lobj = Login()
    lobj.username = Email
    lobj.password = Ph_no
    lobj.type = 'student'
    lobj.save()
    l=Login()
    l.username=guardian_email
    l.password=guardian_Phone
    l.type='parent'
    l.save()

    sobj = Student()
    sobj.name = Name
    sobj.dateofbirth = DOB
    sobj.gender = Gender
    sobj.email = Email
    sobj.phone = Ph_no
    sobj.place = place
    sobj.post = post
    sobj.pin = pin
    sobj.dist = dist
    sobj.photo =path
    sobj.guardianname=guardian_name
    sobj.guardianemail=guardian_email
    sobj.guardianphone=guardian_Phone
    sobj.COURSE_id=Course
    sobj.LOGIN = lobj
    sobj.save()
    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_home/'</script>''')


def edit_student(request,id):
    obj= Course.objects.all()
    res = Student.objects.get(pk=id)
    return render(request,"Admin/edit student.html",{'data':obj ,'data1':res})

def edit_student_post(request):
    id = request.POST['id']
    Name = request.POST["textfield"]
    DOB = request.POST["textfield2"]
    Gender = request.POST["radio"]
    Course = request.POST["select"]
    Email = request.POST["textfield3"]
    Ph_no = request.POST["textfield4"]
    place = request.POST["textfield5"]
    post = request.POST["textfield6"]
    pin = request.POST["textfield7"]
    dist = request.POST["textfield8"]
    guardian_name = request.POST["textfield9"]
    guardian_Phone = request.POST["textfield10"]
    guardian_email = request.POST["textfield11"]
    sobj = Student.objects.get(pk=id)

    if 'photo' in request.FILES:

        photo = request.FILES['photo']
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fn = fs.save(date, photo)
        path = fs.url(date)
        sobj.photo = path
        sobj.save()

    #lobj = Login()
    #lobj.username = Email
    #lobj.password = Ph_no
    #lobj.type = 'student'
    #lobj.save()

    sobj.name = Name
    sobj.dateofbirth = DOB
    sobj.gender = Gender
    sobj.email = Email
    sobj.phone = Ph_no
    sobj.place = place
    sobj.post = post
    sobj.pin = pin
    sobj.dist = dist
    sobj.guardianname = guardian_name
    sobj.guardianemail = guardian_email
    sobj.guardianphone = guardian_Phone
    sobj.COURSE_id = Course
    #sobj.LOGIN = lobj
    sobj.save()
    return HttpResponse('''<script>alert('Successfull');window.location='/myapp/admin_view_student/'</script>''')

def admin_view_attendance(request):
    res=Attendance.objects.all()
    return render(request,"Admin/view attendance.html",{'data':res})

def admin_view_attendance_post(request):
    From=request.POST["textfield"]
    to=request.POST["textfield2"]
    res = Attendance.objects.filter(date__range=[From,to])
    return render(request, "Admin/view attendance.html", {'data': res})


def admin_view_authority(request):
    abj=Authority.objects.all()
    return render(request,"Admin/view authority.html",{'data':abj})

def admin_view_authority_post(request):
    search=request.POST["textfield"]
    abj = Authority.objects.filter(name__icontains=search)
    return render(request, "Admin/view authority.html", {'data': abj})

def delete_authority(request,id):
    abj=Authority.objects.filter(LOGIN=id).delete()
    obj=Login.objects.filter(pk=id).delete()
    return redirect('/myapp/admin_view_authority/')

def admin_view_complaint(request):
    res=Complaint.objects.all()
    return render(request,"Admin/view complaint.html",{'data':res})

def admin_view_complaint_post(request):
    From=request.POST["textfield"]
    To=request.POST["textfield2"]
    res = Complaint.objects.filter(date__range=[From,To])
    return render(request, "Admin/view complaint.html", {'data': res})


def admin_view_course(request):
    abj = Course.objects.all()
    return render(request,"Admin/view course.html",{'data':abj})

def admin_view_course_post(request):
    Search=request.POST["textfield"]
    abj = Course.objects.filter(coursename__icontains=Search)
    return render(request, "Admin/view course.html", {'data': abj})

def delete_course(request,id):
    abj=Course.objects.filter(pk=id).delete()
    return redirect('/myapp/admin_view_course/')

def admin_view_dept(request):
    abj = Department.objects.all()
    return render(request,"Admin/view dept.html",{'data':abj})

def admin_view_dept_post(request):
    search=request.POST["textfield"]
    abj = Department.objects.filter(departmentname__icontains=search)
    return render(request, "Admin/view dept.html", {'data': abj})

def delete_dept(request,id):
    abj=Department.objects.filter(pk=id).delete()
    return redirect('/myapp/admin_view_dept/')


def admin_view_late_notification(request):
    abj=Attendance.objects.filter(time__gt='09:00')
    return render(request,"Admin/view late not.html", {'data': abj})

def admin_view_late_notification_post(request):
    From=request.POST["textfield"]
    to=request.POST["textfield2"]
    abj = Latenotification.objects.filter(From,to)
    return render(request, "Admin/view late not.html", {'data': abj})


def admin_view_staff(request):
    abj = Staff.objects.all()
    return render(request,"Admin/view staff.html",{'data':abj})

def admin_view_staff_post(request):
    search=request.POST["textfield"]
    abj = Staff.objects.filter(name__icontains=search)
    return render(request, "Admin/view staff.html", {'data': abj})

def delete_staff(request,id):
    abj=Staff.objects.filter(LOGIN=id).delete()
    obj=Login.objects.filter(pk=id).delete()
    return redirect('/myapp/admin_view_staff/')

def admin_view_student(request):
    abj = Student.objects.all()
    return render(request,"Admin/view student.html",{'data':abj})

def admin_view_student_post(request):
    search=request.POST["textfield"]
    abj = Student.objects.filter(name__icontains=search)
    return render(request, "Admin/view student.html", {'data': abj})

def delete_student(request,id):
    abj=Student.objects.filter(LOGIN=id).delete()
    obj=Login.objects.filter(pk=id).delete()
    return redirect('/myapp/admin_view_student/')

def admin_view_violence(request):
    var = Violence.objects.all()

    res = []
    for i in var:
        if Violenceincludedface.objects.filter(VIOLENCE=i).exists():
            res.append({
                'date': i.date,
                'time': i.time,
                'photo': i.photo,
                'id': i.id,
                        })

    return render(request, "admin/view violence.html", {'data': res})

def included_faces(request,id):
    var=Violenceincludedface.objects.filter(VIOLENCE_id=id)
    if len(var)>0:
        return render(request,"admin/included faces.html",{'data':var})
    else:
        return HttpResponse('''<script>alert('No Student Found');window.location='/myapp/admin_view_violence/'</script>''')


def authority_view_attendance(request):
    abj=Attendance.objects.all()
    return render(request,"authority/view attendance.html",{'data':abj})

def authority_view_student(request):
    var=Student.objects.all()
    return render(request,"authority/view student.html",{'data':var})

def authority_view_student_post(request):
    search=request.POST["textfield"]
    abj = Student.objects.filter(name__icontains=search)
    return render(request, "Authority/view student.html", {'data': abj})

def authority_view_profile(request):
    var=Authority.objects.get(LOGIN=request.session['lid'])
    return render(request,"authority/view profile.html",{'data':var})

def authority_view_violence(request):
    var=Violence.objects.all()

    return render(request,"authority/view violence.html",{'data':var})

def view_included_faces(request,id):
    var=Violenceincludedface.objects.filter(VIOLENCE_id=id)
    if len(var)>0:
        return render(request,"authority/view included faces.html",{'data':var})
    else:
        return HttpResponse('''<script>alert('No Student Found');window.location='/myapp/authority_view_violence/'</script>''')


def admin_change_password(request):
    return render(request,"admin/change password.html")

def admin_change_password_post(request):
    oldpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmnewpassword=request.POST['textfield3']
    lid=request.session['lid']
    var=Login.objects.get(id=lid)
    if var.password==oldpassword:
        if newpassword==confirmnewpassword:
            var.password=confirmnewpassword
            var.save()
            return HttpResponse("'''<script>alert('Successfull');window.location='/myapp/login/'</script>'''")

        else :
            return HttpResponse("'''<script>alert('Invalid');window.location='/myapp/login/'</script>'''")


    else :
        return HttpResponse("'''<script>alert('Invalid');window.location='/myapp/login/'</script>'''")

def authority_change_password(request):
    return render(request,"authority/change password.html")

def authority_change_password_post(request):
    oldpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmnewpassword=request.POST['textfield3']
    lid=request.session['lid']
    var=Login.objects.get(id=lid)
    if var.password==oldpassword:
        if newpassword==confirmnewpassword:
            var.password=confirmnewpassword
            var.save()
            return HttpResponse("'''<script>alert('Successfull');window.location='/myapp/login/'</script>'''")

        else :
            return HttpResponse("'''<script>alert('Invalid');window.location='/myapp/login/'</script>'''")


    else :
        return HttpResponse("'''<script>alert('Invalid');window.location='/myapp/login/'</script>'''")



def send_reply(request,id):
    return render(request,'admin/sendreply.html',{'id':id})


def send_reply_post(request):
    reply=request.POST['textfield']
    id=request.POST['id']
    res=Complaint.objects.filter(id=id).update(status='Replied',reply=reply)
    return HttpResponse("'''<script>alert('Sending');window.location='/myapp/admin_view_complaint/'</script>'''")


#========Android=================

def andLogin(request):
    username=request.POST['username']
    password=request.POST['password']
    log = Login.objects.filter(username=username, password=password)
    if log.exists():
        log1 = Login.objects.get(username=username, password=password)
        lid=log1.id
        if log1.type == 'parent':
            return JsonResponse({"status":"ok",'lid':str(lid),'type':'parent'})
        elif log1.type == 'student':
            return JsonResponse({"status":"ok",'lid':str(lid),'type':'student'})
        elif log1.type == 'staff':
            return JsonResponse({"status": "ok", 'lid': str(lid), 'type': 'staff'})
        else:
            return JsonResponse({"status": "No"})

    else:
        return JsonResponse({"status":"No"})

def staff_view_profile(request):
    lid=request.POST['lid']
    res=Staff.objects.get(LOGIN=lid)
    return JsonResponse({"status": "ok",
                         "name":res.name,
                         "DOB":res.dateofbirth,
                         'photo':res.photo,
                         "Gender":res.gender,
                         "department":res.DEPARTMENT.departmentname,
                         "email":res.email,
                         "phone":res.phone,
                         "place":res.place,
                         "post":res.post,
                         "dist":res.dist,
                         "pin":res.pin})

def student_view_profile(request):
    lid = request.POST['lid']
    res = Student.objects.get(LOGIN=lid)
    return JsonResponse({"status": "ok","name":res.name,"DOB":res.dateofbirth,

                         "Gender":res.gender,"course":res.COURSE.coursename,
                         "email":res.email,
                         'photo':res.photo,
                         "phone":res.phone,
                         "place":res.place,
                         "post":res.post,
                         "dist":res.dist,
                         "pin":res.pin,
                         "guardianname":res.guardianname,
                         "guardianemail":res.guardianemail,
                         "guardianphone":res.guardianphone})

def parent_view_student(request):
    lid = request.POST['lid']
    print(lid,'l')
    s = Login.objects.get(id=lid).username
    res=Student.objects.filter(guardianemail=s)
    print(res,'rrrr')

    l=[]
    for i in res:
        l.append({'id':i.id,

                  "name": i.name, "DOB": i.dateofbirth, "Gender": i.gender, "photo": i.photo,
                  "course": i.COURSE.coursename, "email": i.email, "phone": i.phone, "place": i.place,
                  "post": i.post,
                  "pin": i.pin, "dist": i.dist, "guardianname": i.guardianname,
                  "guardianemail": i.guardianemail,
                  "guardianphone": i.guardianphone
                  })

    return JsonResponse({"status": "ok", "data": l})


        # return JsonResponse({"status": "ok",
    #
    #                      "name":res.name,"DOB":res.dateofbirth,"Gender":res.gender,"photo":res.photo,
    #                      "course":res.COURSE.coursename,"email":res.email,"phone":res.phone,"place":res.place,"post":res.post,
    #                      "pin":res.pin,"dist":res.dist,"guardianname":res.guardianname,"guardianemail":res.guardianemail,
    #                      "guardianphone":res.guardianphone})


def parent_view_authority(request):
    res=Authority.objects.all()
    l=[]
    for i in res:
        l.append({"id":i.id,
                  "LOGIN_id":i.LOGIN.id,
                  "name":i.name,"email":i.email,"phone":i.phone})
    return JsonResponse({"status": "ok","data":l})

def parent_view_staff(request):
    res = Staff.objects.all()
    l = []
    for i in res:
        l.append({"name": i.name, "email": i.email, "phone": i.phone, "department":i.DEPARTMENT})
    return JsonResponse({"status": "ok","data":l})

def parent_view_violence(request):
    sid = request.POST['sid']
    res = Violenceincludedface.objects.filter(STUDENT_id=sid)
    l = []
    for i in res:
        l.append({"time": i.VIOLENCE.time, "date": i.VIOLENCE.date, "photo": i.VIOLENCE.photo})
    return JsonResponse({"status": "ok", "data": l})


def parent_view_attendance(request):
    sid=request.POST['sid']
    res = Attendance.objects.filter(STUDENT_id=sid)
    l = []
    for i in res:
        l.append({"time":i.hour,"date":i.date,"photo":i.STUDENT.photo,"status":'Present',"name":i.STUDENT.name,"id":i.id,})
    return JsonResponse({"status": "ok","data":l})



def student_view_attendance(request):
    lid = request.POST['lid']
    res = Attendance.objects.filter(STUDENT__LOGIN_id=lid)
    l = []
    for i in res:
        l.append({"time": i.hour, "date": i.date, "photo": i.STUDENT.photo, "status": 'Present'})
    return JsonResponse({"status": "ok","data":l})

def student_view_issue_list(request):
    sid=request.POST['lid']
    res = Violenceincludedface.objects.filter(STUDENT__LOGIN_id=sid)
    l = []
    for i in res:
        l.append({"time":i.VIOLENCE.time,"date":i.VIOLENCE.date,"photo":i.VIOLENCE.photo})
    return JsonResponse({"status": "ok","data":l})

def staff_view_student(request):
    abj = Student.objects.all()
    l = []
    for i in abj:
        l.append({"name": i.name, "DOB": i.dateofbirth, "Gender": i.gender, "Course": i.COURSE,"Email":i.email,"Phone":i.phone,"Place":i.place,"Post":i.post,"Pin":i.pin,"Dist":i.dist,"Guardianname":i.guardianname,"Guardianemail":i.guardianemail,"Guardianphone":i.guardianphone})
    return JsonResponse({"status":"ok",'data':l})

def staff_view_attendance(request):
    res = Attendance.objects.all()
    l = []
    for i in res:
        try:
            l.append({

                "id": i.id,
                "date": i.date,
                "hour": i.hour,
                "name": i.STUDENT.name,
                "DEPT": i.STUDENT.COURSE.DEPARTMENT.departmentname,

                # "time": i.time,
                #       "date": i.date,
                      "photo": i.STUDENT.photo,
                      "status": 'present',
                #       "name":i.STUDENT.name

            })
        except Exception as t:
            print(t)
            pass
    return JsonResponse({"status": "ok", "data": l})
def staff_view_violence(request):
    res = Violenceincludedface.objects.all()
    l = []
    for i in res:
        try:
            l.append({"time": i.VIOLENCE.time, "date": i.VIOLENCE.date, "photo": i.VIOLENCE.photo})
        except:
            pass
    return JsonResponse({"status": "ok","data":l})

def staff_change_password(request):
    oldpassword = request.POST['oldp']
    newpassword = request.POST['newp']
    confirmnewpassword = request.POST['confirmp']
    lid = request.POST['lid']
    var = Login.objects.get(id=lid)
    if var.password == oldpassword:
        if newpassword == confirmnewpassword:
            var.password = confirmnewpassword
            var.save()
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status": "no"})

def student_change_password(request):
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmnewpassword = request.POST['confirmpassword']
    lid = request.POST['lid']
    var = Login.objects.get(id=lid)
    if var.password == oldpassword:
        if newpassword == confirmnewpassword:
            var.password = confirmnewpassword
            var.save()
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status": "no"})


def parent_change_password(request):
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmnewpassword = request.POST['confirmpassword']
    lid = request.POST['lid']
    var = Login.objects.get(id=lid)
    if var.password == oldpassword:
        if newpassword == confirmnewpassword:
            var.password = confirmnewpassword
            var.save()
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status": "no"})


def send_complaint(request):
    lid=request.POST['lid']
    complaint=request.POST['complaint']
    date=datetime.datetime.now().today()
    sobj = Complaint()
    sobj.complaint=complaint
    sobj.status="pending"
    sobj.reply="pending"
    sobj.LOGIN_id= lid
    sobj.date=date
    sobj.save()
    return JsonResponse({"status":"ok"})

def view_reply(request):
    lid=request.POST['lid']
    res=Complaint.objects.filter(LOGIN_id=lid)
    l = []
    for i in res:
        l.append({"id": i.id, "date": i.date, "complaint": i.complaint,"status":i.status,"reply":i.reply})

    return JsonResponse({"status":"ok","data":l})


############################################################################3



def chat1(request,id):
    # cid = str(request.session["userid"])
    request.session["new"] = id
    s = Student.objects.get(LOGIN=id)
    qry = Login.objects.get(username=s.guardianemail, type='parent')
    request.session["userid"] = qry.id
    # qry = Student.objects.get(guardianemail=s)
    return render(request, "authority/Chat.html", {'photo': s.photo, 'name': s.guardianname, 'toid': qry.id})

def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    # qry = Student.objects.get(LOGIN=request.session["userid"])

    s = Student.objects.get(LOGIN=request.session["new"])
    print(s, 'sss')

    qry = Login.objects.get(username=s.guardianemail, type='parent')

    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM_id=fromid, TO_id=toid) | Q(FROM_id=toid, TO_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO_id, "date": i.date, "from": i.FROM_id})

    return JsonResponse({'photo': s.photo, "data": l, 'name': s.guardianname, 'toid': request.session["userid"]})

def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})




def User_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    print(FROM_id,'ffff')
    print(TOID_id,'tttt')
    msg=request.POST['message']

    from  datetime import datetime
    c=Chat()
    c.FROM_id=FROM_id
    c.TO_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})


def User_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    # lmid = request.POST["lastmsgid"]
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM_id=fromid, TO_id=toid) | Q(FROM_id=toid, TO_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "msg": i.message, "from": i.FROM_id, "date": i.date, "to": i.TO_id})

    return JsonResponse({"status":"ok",'data':l})


def get_alert(request):
    nid=request.POST['nid']
    lid=request.POST['lid']
    if nid == '':
        nid='0'
    print(nid, 'hee', lid)
    s = Login.objects.get(id=lid).username
    var=Violenceincludedface.objects.filter(STUDENT__guardianemail=s, id__gt=nid).order_by('id')
    l=[]
    st=''
    for i in var:
        message=st+' '+i.STUDENT.name + ' has been detected in an act of violence'
        nid=i.id
        return JsonResponse({"status":"ok", 'message':message,'nid':str(nid)})
    return JsonResponse({"status": "no", 'message': '', 'nid': str('')})

def get_alert_staff(request):
    nid=request.POST['nid']
    if nid == '':
        nid='0'
    var=Violenceincludedface.objects.filter(id__gt=nid).order_by('id')
    l=[]
    st=''
    for i in var:
        message=st+' '+i.STUDENT.name + ' has been detected in an act of violence'
        nid=i.id
        return JsonResponse({"status":"ok", 'message':message,'nid':str(nid)})
    return JsonResponse({"status": "no", 'message': '', 'nid': str('')})


##################attend



def viewattendance(request):


    c=Course.objects.all()

    return render(request,"Admin/viewattendancenew.html",{'c':c})


def viewattendance_post(request):
    course= request.POST["course"]
    # semsester= request.POST["semsester"]
    year= request.POST["year"]
    month= request.POST["month"]


    at= Attendance.objects.filter(STUDENT__COURSE__id=course, date__month=month,date__year=year)

    dates=[]
    dates2=[]
    dates2.append("name")
    for i in at:
        if i.date not in dates:
            dates.append(i.date)
            dates2.append(i.date)


    st=Student.objects.filter(COURSE__id=course)

    data=[]
    for i in st:

        m=[]
        m.append({'count':i.name, 'status':'name'})

        for j in dates:
            b = Attendance.objects.filter(STUDENT__COURSE__id=course, date=j,STUDENT=i,hour__lt=4)
            a = Attendance.objects.filter(STUDENT__COURSE__id=course, date=j,STUDENT=i,hour__gt=3)




            m.append({'count':str(len(b))+":"+str(len(a)), 'status':'attendance'})

        data.append(m)




    c=Course.objects.all()

    return render(request,"Admin/viewattendancenew.html",{'c':c, 'data':data,'dates':dates})

