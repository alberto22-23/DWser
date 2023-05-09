# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import make_password # Necesario para encriptar la contrasena

class Tcines(models.Model):
    cinenombre = models.CharField(db_column='cineNombre', max_length=25)  # Field name made lowercase.
    cinelogo = models.CharField(db_column='cineLogo', max_length=255)  # Field name made lowercase.
    cantidadsalas = models.IntegerField(db_column='cantidadSalas')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tcines'


class Tentradas(models.Model):
    id_pelicula = models.ForeignKey('Tpeliculas', models.DO_NOTHING, db_column='id_pelicula')
    id_usuario = models.ForeignKey('Tusuarios', models.DO_NOTHING, db_column='id_usuario')
    id_cine = models.ForeignKey(Tcines, models.DO_NOTHING, db_column='id_cine')
    # fecha = models.DateField() # cambiado para resolver endpoint compra de entradas
    fecha = models.CharField(max_length=25)
    entradapreciounitario = models.FloatField(db_column='entradaPrecioUnitario')  # Field name made lowercase.
    entradacantbutacas = models.IntegerField(db_column='entradaCantButacas')  # Field name made lowercase.
    entradapreciototal = models.FloatField(db_column='entradaPrecioTotal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tentradas'


class Tpeliculas(models.Model):
    titulo = models.CharField(max_length=25)
    estreno = models.IntegerField()
    sinopsis = models.CharField(max_length=2000)
    peliculaprecio = models.FloatField(db_column='peliculaPrecio')  # Field name made lowercase.
    cartel = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tpeliculas'


class Tsalas(models.Model):
    numerosala = models.IntegerField(db_column='numeroSala')  # Field name made lowercase.
    aforosala = models.IntegerField(db_column='aforoSala')  # Field name made lowercase.
    id_cine = models.ForeignKey(Tcines, models.DO_NOTHING, db_column='id_cine')
    id_pelicula = models.ForeignKey(Tpeliculas, models.DO_NOTHING, db_column='id_pelicula')

    class Meta:
        managed = False
        db_table = 'tsalas'


class Tusuarios(models.Model):
    usuarionombre = models.CharField(db_column='usuarioNombre', max_length=25)  # Field name made lowercase.
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    token = models.CharField(max_length=255, blank=True, null=True)
    
    # Utilizar bcrypt para encriptar la contrasena antes de guardarla en la BD
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    class Meta:
        managed = False
        db_table = 'tusuarios'
