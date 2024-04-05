from django.db import models
from django.core.validators import RegexValidator

class EmplloyeeModel(models.Model):
    name_validator = RegexValidator(
        regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
        message="Name should be between 3 to 12 characters and contain only letters."
    )
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        message="Invalid email format."
    )
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,14}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed."
    )
    alpha_numeric_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9]+$',
        message="This field must contain only letters and numbers."
    )

    Name = models.CharField(validators=[name_validator], max_length=30)
    Email = models.EmailField(max_length=50, unique=True)
    Age = models.IntegerField()
    Gender = models.CharField(validators=[name_validator], max_length=30)
    Phone_No = models.CharField( max_length=13, unique=True)
    Address_Details = models.JSONField()
    H_No = models.CharField(max_length=30)  # Updated to accept strings and numbers
    Street = models.CharField(validators=[alpha_numeric_validator], max_length=30)
    City = models.CharField(validators=[alpha_numeric_validator], max_length=30)
    State = models.CharField(validators=[alpha_numeric_validator], max_length=30)
    Work_Experience = models.JSONField()
    Company_Name = models.CharField(validators=[alpha_numeric_validator], max_length=30)
    From_Date = models.CharField(max_length=30)  # Updated to accept strings and numbers
    To_Date = models.CharField(max_length=30)    # Updated to accept strings and numbers
    Address = models.CharField(validators=[alpha_numeric_validator], max_length=30)
    Qualifications = models.JSONField()
    Qualification_Name = models.CharField(validators=[alpha_numeric_validator], max_length=30)
    Percentage = models.FloatField()
    Projects = models.JSONField()
    Title = models.CharField(validators=[alpha_numeric_validator], max_length=30)
    Description = models.CharField(validators=[alpha_numeric_validator], max_length=30)
    Photo = models.TextField()
    
    objects = models.Manager()

    class Meta:
        db_table = "Employee_Table"
