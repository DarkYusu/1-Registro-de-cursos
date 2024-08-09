from .models import Estudiante, Profesor, Curso, Direccion
from django.core.exceptions import ObjectDoesNotExist

def crear_curso(codigo, nombre, version, profesor=None):
    try:
        curso = Curso.objects.create(codigo=codigo, nombre=nombre, version=version, profesor=profesor)
        return curso
    except Exception as e:
        return f"Error creando el curso: {e}"

def crear_profesor(rut, nombre, apellido, creado_por):
    try:
        profesor = Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, creado_por=creado_por)
        return profesor
    except Exception as e:
        return f"Error creando el profesor: {e}"

def crear_estudiante(rut, nombre, apellido, fecha_nac, creado_por):
    try:
        estudiante = Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, creado_por=creado_por)
        return estudiante
    except Exception as e:
        return f"Error creando el estudiante: {e}"

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante):
    try:
        direccion = Direccion.objects.create(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
        return direccion
    except Exception as e:
        return f"Error creando la dirección: {e}"

def obtiene_estudiante(rut):
    try:
        estudiante = Estudiante.objects.get(rut=rut)
        print(f"Estudiante encontrado: {estudiante.nombre} {estudiante.apellido}, RUT: {estudiante.rut}")
    except Estudiante.DoesNotExist:
        print(f"No se encontró un estudiante con RUT: {rut}")
        return None

def obtiene_profesor(rut):
    try:
        profesor = Profesor.objects.get(rut=rut)
        print(f"Profesor encontrado: {profesor.nombre} {profesor.apellido}, RUT: {profesor.rut}")
    except Profesor.DoesNotExist:
        print(f"No se encontró un profesor con RUT: {rut}")
        return None

def obtiene_curso(codigo):
    try:
        curso = Curso.objects.get(codigo=codigo)
        print(f"Curso encontrado: {curso.nombre}, Código: {curso.codigo}, Profesor: {curso.profesor}")
    except Curso.DoesNotExist:
        print(f"No se encontró un curso con código: {codigo}")
        return None

def agrega_profesor_a_curso(profesor, curso):
    try:
        curso.profesor = profesor
        curso.save()
        return f"Profesor {profesor.nombre} {profesor.apellido} asignado al curso {curso.nombre}."
    except Exception as e:
        return f"Error asignando el profesor al curso: {e}"

def agrega_cursos_a_estudiante(estudiante, cursos):
    try:
        estudiante.cursos.add(*cursos)
        return f"Cursos agregados al estudiante {estudiante.nombre} {estudiante.apellido}."
    except Exception as e:
        return f"Error agregando los cursos al estudiante: {e}"

def imprime_estudiante_cursos(estudiante):
    try:
        cursos = estudiante.cursos.all()
        return [f"{curso.nombre} (v{curso.version})" for curso in cursos]
    except Exception as e:
        return f"Error obteniendo los cursos del estudiante: {e}"
