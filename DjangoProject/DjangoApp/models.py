from django.db import models

from django.core.validators import RegexValidator


class EmplloyeeModel(models.Model):
    name = RegexValidator(regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                     message="name ")
    gender = RegexValidator(regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                     message="gender ")
    Name = models.CharField(validators=[name], max_length=30)
    Email = models.EmailField(max_length=50,unique=True)
    Age=models.IntegerField()
    Gender=models.CharField(validators=[gender], max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    Phone_No = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    Address_Details =models.JSONField()
    hno = RegexValidator(regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                     message="gender ")
    H_No=models.CharField(validators=[hno], max_length=30)
    Street=models.CharField(validators=[hno], max_length=30)
    City=models.CharField(validators=[hno], max_length=30)
    State=models.CharField(validators=[hno], max_length=30)
    Work_Experience=models.JSONField()
    Company_Name=models.CharField(validators=[hno], max_length=30)
    From_Date=models.CharField(validators=[hno], max_length=30)
    To_Date=models.CharField(validators=[hno], max_length=30)
    Address=models.CharField(validators=[hno], max_length=30)
    Qualifications=models.JSONField()
    Qualification_Name=models.CharField(validators=[hno], max_length=30)
    Percentage=models.FloatField()
    Projects=models.JSONField()
    Title=models.CharField(validators=[hno], max_length=30)
    Description=models.CharField(validators=[hno], max_length=30)
    Photo=models.TextField()
    objects = models.Manager
    class Meta:
        db_table = "Employee_Table"