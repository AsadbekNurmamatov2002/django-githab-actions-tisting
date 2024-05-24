import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .usermanagers import MyUserManagers, StudentManager



class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, unique=True)
    class Types(models.TextChoices):
        STUDENT = "STUDENT", "student"
        TEACHER = "TEACHER", "teacher"
        FAKULTET_ADMIN = "FAKULTET_ADMIN", "fakultet admin"
        KAFEDRA_ADMIN = "KAFIDRA_ADMIN", "kafidra admin"
        ADMIN = "ADMIN", "admin"
    types = models.CharField(max_length=14, default=Types.STUDENT, choices=Types.choices)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_fakultet_admin = models.BooleanField(default=False)
    is_kafedra_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = MyUserManagers()
    
    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return str(self.id)
    
    def has_perm(self, perm, obj=None) -> bool:
        return self.is_admin
    
    def has_module_perms(self, app_label) -> bool:
        return True
    def save(self, *args, **kwargs):
        if self.types == self.Types.STUDENT:
            self.is_student = True
        elif self.types == self.Types.TEACHER:
            self.is_teacher = True
        elif self.types == self.Types.KAFEDRA_ADMIN:
            self.is_fakultet_admin = True
        elif self.types == self.Types.FAKULTET_ADMIN:
            self.is_kafedra_admin = True
        elif self.types == self.Types.ADMIN:
            self.is_admin = True
        return super().save(*args, **kwargs)
            

class Student(User):
    
    class Meta:
        proxy = True
        
    objects = StudentManager()
    
    def save(self, *args, **kwargs):
        self.types == User.Types.STUDENT
        self.is_student = True
        return super().save(*args, **kwargs)
    
    
class Teacher(User):
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.types == User.Types.TEACHER
        self.is_teacher = True
        return super().save(*args, **kwargs)
    
# kafidra admin
class KafedraAdmin(User):
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        self.types == User.Types.FAKULTET_ADMIN
        self.is_kafedra_admin = True
        return super().save(*args, **kwargs)
    
# Fakultet admin
class FakultetAdmin(User):
    class Meta:
        proxy = True
        
    def save(self, *args, **kwargs):
        self.types == User.Types.FAKULTET_ADMIN
        self.is_fakultet_admin = True
        return super().save(*args, **kwargs)
    
class Admin(User):
    class Meat:
        proxy = True
        
    def save(self, *args, **kwargs):
        self.types == User.Types.ADMIN
        self.is_admin == True
        return super().save(*args, **kwargs)
    

        
        
        
