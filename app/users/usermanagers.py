from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User


class MyUserManagers(BaseUserManager):
    def create_user(self, id, password=None, **extra_fields):
        if not id:
            raise ValueError("The ID must be set")
        if not password:
            raise ValueError("The Password must set")

        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password, **extra_fields):
        extra_fields.setdefault("is_student", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_teacher", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_fakultet_admin", True)
        extra_fields.setdefault("is_kafedra_admin", True)

        # student
        if extra_fields.setdefault("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        # teacher
        if extra_fields.setdefault("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        # admin
        if extra_fields.setdefault("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        # staff
        if extra_fields.setdefault("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        # is_superuser
        if extra_fields.setdefault("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # is_fakultet_admin
        if extra_fields.setdefault("is_fakultet_admin") is not True:
            raise ValueError("Superuser must have is_fakultet_admin=True.")
        # is_kafedra_admin
        if extra_fields.setdefault("is_kafedra_admin") is not True:
            raise ValueError("Superuser must have is_kafedra_admin=True.")

        return self.create_user(id, password, **extra_fields)


#  student managers
class StudentManager(MyUserManagers):
    def create_studentuser(self, id, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_student", True)

        if extra_fields.setdefault("is_student") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.setdefault("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        return self.create_user(id, password, **extra_fields)

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(self.types == User.Types.STUDENT)


class AdminManager(MyUserManagers):
    def create_studentuser(self, id, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.setdefault("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.setdefault("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        return self.create_user(id, password, **extra_fields)

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(self.types == User.Types.TEACHER)


# is_admin
class TeacherManager(MyUserManagers):
    def create_teacheruser(self, id, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.setdefault("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.setdefault("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        return self.create_user(id, password, **extra_fields)

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(self.types == User.Types.TEACHER)


#  is_fakultet_admin
class FakultetAdminManager(MyUserManagers):
    def create_fakultetadminuser(self, id, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_fakultet_admin", True)

        if extra_fields.setdefault("is_fakultet_admin") is not True:
            raise ValueError("Superuser must have is_fakultet_admin=True.")
        if extra_fields.setdefault("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        return self.create_user(id, password, **extra_fields)

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(self.types == User.Types.FAKULTET_ADMIN)


# is_kafedra_admin
class KafidraAdminManager(MyUserManagers):
    def create_kafidraadminuser(self, id, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_kafedra_admin", True)

        if extra_fields.setdefault("is_fakultet_admin") is not True:
            raise ValueError("Superuser must have is_kafedra_admin =True.")
        if extra_fields.setdefault("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        return self.create_user(id, password, **extra_fields)

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(self.types == User.Types.KAFEDRA_ADMIN)
