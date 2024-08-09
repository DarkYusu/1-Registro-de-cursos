from django.db import models
from django.utils import timezone

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor = models.OneToOneField('Profesor', on_delete=models.SET_NULL, null=True, blank=True, related_name='curso')

    def __str__(self):
        return f"{self.nombre} (v{self.version})"


class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(default=timezone.now)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso, related_name='profesores', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nac = models.DateField(null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(default=timezone.now)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, related_name='direccion', unique=True)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}, {self.region}"
