from django.db import models

class TblAlumno(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    alumno_nombre = models.CharField(max_length=100)
    alumno_email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alumno'


class TblMatricula(models.Model):
    matricula_id = models.AutoField(primary_key=True)
    matricula_grupo = models.CharField(max_length=255)
    alumno = models.ForeignKey(TblAlumno, models.DO_NOTHING)
    profesor = models.ForeignKey('TblProfesor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_matricula'


class TblProfesor(models.Model):
    profesor_id = models.AutoField(primary_key=True)
    profesor_nombre = models.CharField(max_length=255)
    profesor_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_profesor'
