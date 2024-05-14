# views.py
from django.shortcuts import *
from django.core import serializers

from .forms import *
from .models import *

def StudentDetail_Table():
    """
    Retrieve all student details from the database and serialize them into a Python dictionary.

    Returns:
        dict: A dictionary containing serialized student details.
    """
    context = {
        'data': serializers.serialize("python", StudentDetail.objects.all())
    }
    return context

def SelectByStandardStudentDetail_Table(std):
    """
    Retrieve student details filtered by standard from the database and serialize them into a Python dictionary.

    Args:
        std (int): Standard of the students to filter.

    Returns:
        dict: A dictionary containing serialized student details filtered by standard.
    """
    context = {
        'data': serializers.serialize("python", StudentDetail.objects.filter(standard=std))
    }
    return context

def SelectStandard(request):
    """
    Extract the selected standard from the request.

    If a POST request is received, extract the standard from the form data. Otherwise, set a default standard.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        int: Selected standard.
    """
    global std
    std = 8
    if request.method == 'POST':
        form = SelectStandardForm(request.POST)
        if form.is_valid():
            std = form.cleaned_data['standard']
    return std

def SelectRegisterNo(request):
    """
    Extract the selected register number from the request session.

    If the register number is not found in the session, set it to None. If a POST request is received, extract the register number from the form data and update the session.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        str or None: Selected register number.
    """
    if 'register_no' in request.session:
        register_no = request.session['register_no']
    else:
        register_no = None

    if request.method == 'POST':
        form = SelectRegisterNoForm(request.POST)
        if form.is_valid():
            register_no = form.cleaned_data['registerNo']
            request.session['register_no'] = register_no

    return register_no

def Index(request): 
    """
    Render the index page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered index page.
    """
    return render(request, 'Index.html')

# def About(request): 
#     """
#     Render the about page.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: The HTTP response containing the rendered about page.
#     """
#     return render(request, 'About.html')

def AddNewStudent(request):
    """
    Add a new student to the database.

    If a POST request is received, process the form data and save the new student details.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.
    """
    std = None
    if request.method == 'POST':
        form = AddStudentDetailForm(request.POST)
        if form.is_valid():
            form.instance.attendance = 'Absent'
            form.instance.marks = 0
            form.instance.result = 'Fail'
            form.save()
    else:
        form = AddStudentDetailForm()
    return render(request, 'AddNewStudent.html', {'std': std})

def UpdateStudent(request):
    """
    Update student details.

    If a POST request is received, process the form data and update the student details.
    If a GET request is received, extract the standard from the request.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.
    """
    form = None
    std = SelectStandard(request)
    students = None
    if std:
        students = StudentDetail.objects.filter(standard=std)

    if request.method == 'POST':
        form = AddAttendanceForm(request.POST)
        if form.is_valid():
            register_no = form.cleaned_data['registerNo']
            student = get_object_or_404(StudentDetail, registerNo=register_no)
            student.studentName = form.data['studentName']
            student.save()
    else:
        std = request.GET.get('standard')
    return render(request, 'UpdateStudentDetails.html', {'form': form, 'std': std, 'students': students})


# double linked list
class Node:
    """
    Represents a node in a doubly linked list.

    Attributes:
        data: Data stored in the node.
        prev: Reference to the previous node.
        next: Reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """
    Represents a doubly linked list.

    Attributes:
        head: Reference to the first node in the list.
        current: Reference to the current node in the list.
    """
    def __init__(self):
        self.head = None
        self.current = None  # Added current pointer to keep track of the current node

    def append(self, data):
        """
        Append a new node with the given data to the end of the list.

        Args:
            data: Data to be stored in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.current = self.head  # Set current to head initially
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def next(self):
        """
        Move the current pointer to the next node and return its data.

        Returns:
            str: Data of the next node.
        """
        if self.current.next:
            self.current = self.current.next
            return self.current.data
        else:
            return "End of the list"

    def prev(self):
        """
        Move the current pointer to the previous node and return its data.

        Returns:
            str: Data of the previous node.
        """
        if self.current.prev:
            self.current = self.current.prev
            return self.current.data
        else:
            return "Start of the list"

    def display_current(self):
        """
        Display the data of the current node.
        """
        if self.current:
            print("Current node:", self.current.data)
        else:
            print("List is empty")

    def display(self):
        """
        Display all nodes in the list.
        """
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def delete_all(self):
        """
        Delete all nodes in the list.
        """
        current = self.head
        while current:
            temp = current.next
            del current.data
            del current.prev
            del current.next
            current = temp
        self.head = None

# Example usage:
dll = DoublyLinkedList()

# Below are the Django views with added documentation:

def Attendance(request):
    """
    View function to manage attendance.

    Retrieves student details, updates attendance status, and renders the attendance page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered attendance page.
    """
    std = SelectStandard(request)
    register_no = SelectRegisterNo(request)  # Retrieve the selected register number
    form = None
    students = None
    if std:
        students = StudentDetail.objects.filter(standard=std).exclude(attendance='Present')
    if request.method == 'POST':
        form = AddAttendanceForm(request.POST)
        if form.is_valid():
            register_no = form.cleaned_data['registerNo']
            student = get_object_or_404(StudentDetail, registerNo=register_no)
            student.attendance = 'Present'
            student.save()
            # Redirect to the same page to reload the data
            return HttpResponseRedirect(request.path_info)
    student_list = []
    dll.delete_all()
    if students is not None:
        for student in students:
            dll.append(student.registerNo)
            student_list.append(student.registerNo)
    return render(request, 'Attendance.html', {'form': form, 'std': std, 'register_no': register_no, 'students': student_list})

def RemoveStudent(request):
    """
    View function to remove a student.

    Retrieves student details, removes a student, and renders the remove student page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered remove student page.
    """
    form = None
    std = SelectStandard(request)
    students = None
    if std:
        students = StudentDetail.objects.filter(standard=std)
    if request.method == 'POST':
        form = AddAttendanceForm(request.POST)
        if form.is_valid():
            register_no = form.cleaned_data['registerNo']
            student = get_object_or_404(StudentDetail, registerNo=register_no)
            student.delete()
    else:
        std = request.GET.get('standard')
    return render(request, 'RemoveStudent.html', {'form': form, 'std': std, 'students': students})

# def GetStudentDetails(request):
#     """
#     View function to retrieve student details.

#     Retrieves student details based on the selected standard and renders the student details page.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: The HTTP response containing the rendered student details page.
#     """
#     context = {}
#     if request.method == 'POST':
#         form = GetStudentDetailsForm(request.POST)
#         if form.is_valid():
#             std = form.cleaned_data['standard']
#             students = StudentDetail.objects.filter(standard=std)
#             sl_no = list(range(1, len(students) + 1))
#             context = {'students': students, 'sl_no': sl_no}
#     return render(request, 'GetStudentDetails.html', context)

def GetStudentDetails(request):
    """
    View function to retrieve student details.

    Retrieves student details based on the selected standard and renders the student details page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered student details page.
    """
    context = {}
    if request.method == 'POST':
        form = GetStudentDetailsForm(request.POST)
        if form.is_valid():
            std = form.cleaned_data['standard']
            students = StudentDetail.objects.filter(standard=std)
            sl_no = list(range(1, len(students) + 1))
            students_with_sl_no = zip(students, sl_no)  # Pair each student with its serial number
            context = {'students': students_with_sl_no}
            context['std'] = std
    return render(request, 'GetStudentDetails.html', context)

def GetStudentDetailsPDF(request):
    """
    View function to retrieve student details for PDF generation.

    Retrieves student details based on the selected standard and renders the student details PDF generation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered student details PDF generation page.
    """
    context = {}
    if request.method == 'POST':
        form = GetStudentDetailsForm(request.POST)
        if form.is_valid():
            std = form.cleaned_data['standard']
            students = StudentDetail.objects.filter(standard=std)
            sl_no = list(range(1, len(students) + 1))
            students_with_sl_no = zip(students, sl_no)  # Pair each student with its serial number
            context = {'students': students_with_sl_no}
            context['std'] = std
    return render(request, 'GetStudentDetailsPDF.html', context)

# def SetMarks(request):
#     std = SelectStandard(request)
#     form = None
#     students = None
#     if std:
#         students = StudentDetail.objects.filter(standard=std)
#     if request.method == 'POST':
#         form = SetMarksForm(request.POST)
#         if form.is_valid():
#             register_no = form.cleaned_data['registerNo']
#             student = get_object_or_404(StudentDetail, registerNo=register_no)
#             student.marks = form.cleaned_data['marks']
#             if student.marks >= 20:
#                 student.result = 'Pass'
#             else:
#                 student.result = 'Fail'
#             student.save()
#     else:
#         std = request.GET.get('standard')
#     student_list = []
#     dll.delete_all()
#     if students is not None:
#         for student in students:
#             dll.append(student.registerNo)
#             student_list.append(student.registerNo)
#     return render(request, 'SetMarks.html', {'form': form, 'std': std, 'students': student_list})

# def SetMarks(request):
#     std = request.GET.get('standard')
#     students = None
#     if std:
#         students = StudentDetail.objects.filter(standard=std)
#     if request.method == 'POST':
#         if students is not None:
#             for student in students:
#                 form_field_name = f'marks_{student.registerNo}'
#                 marks = request.POST.get(form_field_name)
#                 # Update student marks
#                 student.marks = marks
#                 # Update result
#                 student.result = 'Pass' if int(marks) >= 20 else 'Fail'
#                 student.save()
#     return render(request, 'SetMarks.html', {'std': std, 'students': students})

def SetMarks(request):
    """
    View function to set marks for students.

    Retrieves student details, updates marks, determines pass or fail status, and renders the set marks page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered set marks page.
    """
    std = request.GET.get('standard')
    students = None
    if std:
        students = StudentDetail.objects.filter(standard=std)
    if request.method == 'POST':
        if students is not None:
            for student in students:
                form_field_name = f'marks_{student.registerNo}'
                marks = request.POST.get(form_field_name)
                # Update student marks
                student.marks = marks
                # Update result
                student.result = 'Pass' if int(marks) >= 20 else 'Fail'
                student.save()
    return render(request, 'SetMarks.html', {'std': std, 'students': students})

def UpdateMarks(request):
    std = request.GET.get('standard')
    students = None
    if std: students = StudentDetail.objects.filter(standard=std).exclude(marks__lte=19)
    if request.method == 'POST':
        if students is not None:
            for student in students:
                form_field_name = f'marks_{student.registerNo}'
                marks = request.POST.get(form_field_name, None)  # Initialize marks
                if marks is not None:  # Check if marks are provided
                    # Update student marks
                    student.marks = int(marks)
                    # Update result
                    student.result = 'Pass' if int(marks) >= 20 else 'Fail'
                    student.save()
    return render(request, 'UpdateMarks.html', {'std': std, 'students': students})

def GetMarks(request):
    """
    View function to retrieve marks for students.

    Retrieves marks for students based on the selected standard and renders the get marks page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered get marks page.
    """
    context = {}
    if request.method == 'POST':
        form = GetMarksForm(request.POST)
        std = form.data['standard']
        context = {'data': serializers.serialize("python", StudentDetail.objects.filter(standard = std))}
    return render(request, 'GetMarks.html', context)

def GetMarksPDF(request):
    """
    View function to retrieve marks for PDF generation.

    Retrieves marks for students based on the selected standard and renders the get marks PDF generation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered get marks PDF generation page.
    """
    context = {}
    if request.method == 'POST':
        form = GetMarksPDFForm(request.POST)
        std = form.data['standard']
        context = {'data': serializers.serialize("python", StudentDetail.objects.filter(standard = std))}
        context['std'] = std
    return render(request, 'GetMarksPDF.html', context)

def RanksCalc(table, std):
    """
    Calculate ranks for students based on marks.

    Args:
        table: Model for storing ranks.
        std (int): Standard of the students.

    Returns:
        dict: Dictionary containing serialized rank data.
    """
    table.objects.all().delete()
    if std == 0:
        data = serializers.serialize("python", StudentDetail.objects.all())
    else:
        data = serializers.serialize("python", StudentDetail.objects.filter(standard=std))
    detailsData = {'registerNo': [], 'studentName': [], 'marks': [], 'rank': [], 'standard': []}
    for i in data:
        detailsData['registerNo'].append(i['pk'])
        detailsData['studentName'].append(i['fields']['studentName'])
        detailsData['marks'].append(i['fields']['marks'])
        detailsData['standard'].append(i['fields']['standard'])
    marks = sorted(set(detailsData['marks']), reverse=True)[:3]
    marks = [mark for mark in marks if mark > 20]
    rank_counter = 1
    for mark in marks:
        students_with_rank = [student for student, m in zip(detailsData['registerNo'], detailsData['marks']) if m == mark]
        for student_pk in students_with_rank:
            student = StudentDetail.objects.get(pk=student_pk)
            table.objects.create(registerNo=student.registerNo, studentName=student.studentName, marks=student.marks, rank=rank_counter, standard=student.standard)
        rank_counter += 1
    context = {'data': serializers.serialize("python", table.objects.all())}
    return context

def Ranks(request):
    """
    View function to calculate and display ranks for students.

    Calculates ranks based on the selected standard and renders the ranks page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered ranks page.
    """
    context = {}
    if request.method == 'POST':
        form = GetRanksForm(request.POST)
        std = form.data['standard']
        print(std)
        if std == '8':
            context = RanksCalc(Class8Ranks, 8)
        elif std == '9':
            context = RanksCalc(Class9Ranks, 9)
        elif std == '10':
            context = RanksCalc(Class10Ranks, 10)
        elif std == '0':
            context = RanksCalc(SchoolRanks, 0)
    return render(request, 'Ranks.html', context)

def RanksPDF(request):
    """
    View function to calculate and display ranks for PDF generation.

    Calculates ranks based on the selected standard and renders the ranks PDF generation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered ranks PDF generation page.
    """
    context = {}
    if request.method == 'POST':
        form = GetRanksPDFForm(request.POST)
        std = form.data['standard']
        print(std)
        if std == '8':
            context = RanksCalc(Class8Ranks, 8)
        elif std == '9':
            context = RanksCalc(Class9Ranks, 9)
        elif std == '10':
            context = RanksCalc(Class10Ranks, 10)
        elif std == '0':
            context = RanksCalc(SchoolRanks, 0)
        context['std'] = std
    return render(request, 'RanksPDF.html', context)

def StaffSignIn(request):
    """
    View function to render the staff sign-in page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered staff sign-in page.
    """
    return render(request, 'StaffSignIn.html')

def StaffSignUp(request):
    """
    View function to render the staff sign-up page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered staff sign-up page.
    """
    return render(request, 'StaffSignUp.html')

def Contact(request):
    """
    View function to render the contact page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered contact page.
    """
    return render(request, 'Contact.html')

# def UserManual(request):
#     """
#     View function to render the user manual page.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: The HTTP response containing the rendered user manual page.
#     """
#     return render(request, 'UserManual.html')
