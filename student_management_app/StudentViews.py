from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage # To upload Profile Picture
from django.urls import reverse
import datetime # To Parse input DateTime into Python Date Time Object

from .models import CustomUser, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent, FeedBackStudent, StudentResult

def student_home(request):
    try:
        student_obj = Students.objects.get(admin=request.user.id)
        total_attendance = AttendanceReport.objects.filter(student_id=student_obj).count()
        attendance_present = AttendanceReport.objects.filter(student_id=student_obj, status=True).count()
        attendance_absent = AttendanceReport.objects.filter(student_id=student_obj, status=False).count()

        course_obj = Courses.objects.get(id=student_obj.course_id.id)
        total_subjects = Subjects.objects.filter(course_id=course_obj).count()

        subject_name = []
        data_present = []
        data_absent = []
        subject_data = Subjects.objects.filter(course_id=student_obj.course_id)
        for subject in subject_data:
            attendance = Attendance.objects.filter(subject_id=subject.id)
            attendance_present_count = AttendanceReport.objects.filter(attendance_id__in=attendance, status=True, student_id=student_obj.id).count()
            attendance_absent_count = AttendanceReport.objects.filter(attendance_id__in=attendance, status=False, student_id=student_obj.id).count()
            subject_name.append(subject.subject_name)
            data_present.append(attendance_present_count)
            data_absent.append(attendance_absent_count)

        context = {
            "total_attendance": total_attendance,
            "attendance_present": attendance_present,
            "attendance_absent": attendance_absent,
            "total_subjects": total_subjects,
            "subject_name": subject_name,
            "data_present": data_present,
            "data_absent": data_absent
        }
        return render(request, "student_template/student_home_template.html", context)
    except Students.DoesNotExist:
        messages.error(request, "Student record not found.")
        return redirect('home')
    except Exception as e:
        messages.error(request, "An error occurred: " + str(e))
        return redirect('home')


def student_view_attendance(request):
    try:
        student = Students.objects.get(admin=request.user.id)  # Getting Logged in Student Data
        course = student.course_id  # Getting Course Enrolled of LoggedIn Student
        subjects = Subjects.objects.filter(course_id=course)  # Getting the Subjects of Course Enrolled
        context = {
            "subjects": subjects
        }
        return render(request, "student_template/student_view_attendance.html", context)
    except Students.DoesNotExist:
        messages.error(request, "Student record not found.")
        return redirect('home')
    except Exception as e:
        messages.error(request, "An error occurred: " + str(e))
        return redirect('home')


def student_view_attendance_post(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('student_view_attendance')
    else:
        try:
            # Getting all the Input Data
            subject_id = request.POST.get('subject')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Parsing the date data into Python object
            start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

            # Getting all the Subject Data based on Selected Subject
            subject_obj = Subjects.objects.get(id=subject_id)
            # Getting Logged In User Data
            user_obj = CustomUser.objects.get(id=request.user.id)
            # Getting Student Data Based on Logged in Data
            stud_obj = Students.objects.get(admin=user_obj)

            # Now Accessing Attendance Data based on the Range of Date Selected and Subject Selected
            attendance = Attendance.objects.filter(attendance_date__range=(start_date_parse, end_date_parse), subject_id=subject_obj)
            # Getting Attendance Report based on the attendance details obtained above
            attendance_reports = AttendanceReport.objects.filter(attendance_id__in=attendance, student_id=stud_obj)

            context = {
                "subject_obj": subject_obj,
                "attendance_reports": attendance_reports
            }

            return render(request, 'student_template/student_attendance_data.html', context)
        except Subjects.DoesNotExist:
            messages.error(request, "Subject record not found.")
            return redirect('student_view_attendance')
        except Students.DoesNotExist:
            messages.error(request, "Student record not found.")
            return redirect('student_view_attendance')
        except Exception as e:
            messages.error(request, "An error occurred: " + str(e))
            return redirect('student_view_attendance')


def student_apply_leave(request):
    try:
        student_obj = Students.objects.get(admin=request.user.id)
        leave_data = LeaveReportStudent.objects.filter(student_id=student_obj)
        context = {
            "leave_data": leave_data
        }
        return render(request, 'student_template/student_apply_leave.html', context)
    except Students.DoesNotExist:
        messages.error(request, "Student record not found.")
        return redirect('home')
    except Exception as e:
        messages.error(request, "An error occurred: " + str(e))
        return redirect('home')


def student_apply_leave_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('student_apply_leave')
    else:
        try:
            leave_date = request.POST.get('leave_date')
            leave_message = request.POST.get('leave_message')

            student_obj = Students.objects.get(admin=request.user.id)
            leave_report = LeaveReportStudent(student_id=student_obj, leave_date=leave_date, leave_message=leave_message, leave_status=0)
            leave_report.save()
            messages.success(request, "Applied for Leave.")
            return redirect('student_apply_leave')
        except Students.DoesNotExist:
            messages.error(request, "Student record not found.")
            return redirect('student_apply_leave')
        except Exception as e:
            messages.error(request, "Failed to Apply Leave: " + str(e))
            return redirect('student_apply_leave')


def student_feedback(request):
    try:
        student_obj = Students.objects.get(admin=request.user.id)
        feedback_data = FeedBackStudent.objects.filter(student_id=student_obj)
        context = {
            "feedback_data": feedback_data
        }
        return render(request, 'student_template/student_feedback.html', context)
    except Students.DoesNotExist:
        messages.error(request, "Student record not found.")
        return redirect('home')
    except Exception as e:
        messages.error(request, "An error occurred: " + str(e))
        return redirect('home')


def student_feedback_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method.")
        return redirect('student_feedback')
    else:
        try:
            feedback = request.POST.get('feedback_message')
            student_obj = Students.objects.get(admin=request.user.id)

            add_feedback = FeedBackStudent(student_id=student_obj, feedback=feedback, feedback_reply="")
            add_feedback.save()
            messages.success(request, "Feedback Sent.")
            return redirect('student_feedback')
        except Students.DoesNotExist:
            messages.error(request, "Student record not found.")
            return redirect('student_feedback')
        except Exception as e:
            messages.error(request, "Failed to Send Feedback: " + str(e))
            return redirect('student_feedback')


def student_profile(request):
    try:
        user = CustomUser.objects.get(id=request.user.id)
        student = Students.objects.get(admin=user)

        context = {
            "user": user,
            "student": student
        }
        return render(request, 'student_template/student_profile.html', context)
    except CustomUser.DoesNotExist:
        messages.error(request, "User record not found.")
        return redirect('home')
    except Students.DoesNotExist:
        messages.error(request, "Student record not found.")
        return redirect('home')
    except Exception as e:
        messages.error(request, "An error occurred: " + str(e))
        return redirect('home')


def student_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('student_profile')
    else:
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            address = request.POST.get('address')

            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password and password != "":
                customuser.set_password(password)
            customuser.save()

            student = Students.objects.get(admin=customuser.id)
            student.address = address
            student.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('student_profile')
        except CustomUser.DoesNotExist:
            messages.error(request, "User record not found.")
            return redirect('student_profile')
        except Students.DoesNotExist:
            messages.error(request, "Student record not found.")
            return redirect('student_profile')
        except Exception as e:
            messages.error(request, "Failed to Update Profile: " + str(e))
            return redirect('student_profile')


def student_view_result(request):
    try:
        student = Students.objects.get(admin=request.user.id)
        student_result = StudentResult.objects.filter(student_id=student.id)
        context = {
            "student_result": student_result,
        }
        return render(request, "student_template/student_view_result.html", context)
    except Students.DoesNotExist:
        messages.error(request, "Student record not found.")
        return redirect('home')
    except Exception as e:
        messages.error(request, "An error occurred: " + str(e))
        return redirect('home')
