from djongo import models
import django.utils.timezone


# Create your models here.

class subject(models.Model):
    subject_id = models.CharField(null=False, max_length=5, primary_key='true')
    subject_name = models.CharField(null=False, max_length=30)
    subject_credit = models.BigIntegerField(null=False)
    subject_secured_score = models.BigIntegerField(default=0)
    subject_total_score = models.BigIntegerField(null=False)
    subject_grade = models.CharField(max_length=10, default="")


class semester(models.Model):
    subject = models.ManyToManyField(subject)
    cpi = models.BigIntegerField(default=0.0)
    spi = models.BigIntegerField(default=0.0)
    overall_grade = models.CharField(max_length=10, default="")


class Student(models.Model):
    student_id = models.CharField(max_length=30, primary_key='true')
    admission_type = models.CharField(max_length=30, blank=True, null=True)
    ddu_reporting_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    name_format = models.CharField(max_length=30, default="LFM")
    gender = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    birth_place = models.CharField(max_length=30, blank=True, null=True)
    acpc_seat_allotment_date = models.DateTimeField(blank=True, null=True)
    is_d2d = models.CharField(max_length=30, blank=True, null=True)
    enrollment_year = models.CharField(max_length=30, blank=True, null=True)
    degree = models.CharField(max_length=30, blank=True, null=True)
    qualifying_exam_rollno = models.CharField(
        max_length=30, blank=True, null=True)
    session_type = models.CharField(max_length=30, blank=True, null=True)
    session_no = models.IntegerField(default=0, blank=True, null=True)
    batch_year = models.CharField(max_length=30, blank=True, null=True)
    old_student_code = models.CharField(max_length=30, blank=True, null=True)
    students_allotment = models.CharField(max_length=30, blank=True, null=True)
    merit_rank = models.IntegerField(default=0, blank=True, null=True)
    re_shuffle_status = models.CharField(max_length=30, blank=True, null=True)
    re_shuffle_phase = models.IntegerField(default=0, blank=True, null=True)
    cast_category_code = models.CharField(max_length=30, blank=True, null=True)
    sub_cast = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.CharField(max_length=30, blank=True, null=True)
    mother_tongue = models.CharField(max_length=30, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    blood_group = models.CharField(max_length=30, blank=True, null=True)
    relation_type = models.CharField(max_length=30, blank=True, null=True)
    full_name = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    organization_name = models.CharField(max_length=30, blank=True, null=True)
    annual_income = models.IntegerField(default=0, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=70, blank=True, null=True)
    pin_code = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    phone_no = models.CharField(max_length=30, blank=True, null=True)
    mobile_no = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    local_address1 = models.CharField(max_length=30, blank=True, null=True)
    local_address2 = models.CharField(max_length=30, blank=True, null=True)
    local_address3 = models.CharField(max_length=30, blank=True, null=True)
    local_city = models.CharField(max_length=30, blank=True, null=True)
    local_mobile_no = models.CharField(max_length=30, blank=True, null=True)
    semester = models.ManyToManyField(semester)
