from django.db import models

# Create your models here.
    
class Mp(models.Model):

    Nombre = models.CharField(max_length=50, help_text='Nombre Completo empezando por Nombre, Apellido Paterno, Apellido Materno')
    Cargo = models.CharField(max_length=50,help_text='Ingrese el cargo de la Autoridad')
    Adscripcion = models.CharField(max_length=100, help_text='Ingrese el lugar de Agencia o Unidad')      
    def __str__(self):
      return '%s' % (self.Nombre)
  
 

class Indicio(models.Model):

    Expediente = models.CharField(max_length=100, help_text = 'Ingrese el Numero de Carpeta')
    
    Fecha_Ingreso = models.DateField(null=True, blank=True)       
    
    Hora_Ingreso = models.TimeField(null= True, blank=True)       
    
    Oficio = models.CharField(max_length= 15)

    No_Indicio = models.CharField(max_length = 10, help_text ='Ingrese el numero de indicio')       
    
    tipo_indicio = ( ('F' , 'Fisico'),
                     ('O' , 'Organico'),
                     ('B' , 'Biologico'),
                     ('M' , 'Fisico/Organico')         
                  )       

    Tipo = models.CharField(max_length = 1, choices = tipo_indicio, default = 'F')       
    
    Descripcion = models.TextField(max_length = 500, help_text = 'Describe el indicio como la etiqueta')       
    
    Rue = models.CharField (max_length = 15, help_text = 'Format = OM/F/100/2019')       


    clase_indicio  = (
                     ('AC','Arma de Fuego Corta'),
                     ('AL', 'Arma de Fuego Larga'),       
                     ('AB','Arma Blanca'),       
                     ('EM','Estupefaciente-Marihuana'),
                     ('EC', 'Estupefaciente-Cocaina'),
                     ('EH', 'Estupefaciente-Heroina'),
                     ('EA', 'Estupefaciente-Anfetamina'),
                     ('ET', 'Estupefaciente-Tabaco'),
                     ('AL', 'Alcohol'),       
                     ('P','Perecedero'),       
                     ('E','Electronico'),       
                     ('AP','Autopartes'),       
                     ('H' , 'Herramientas'),       
                     ('AB', ' Articulos de Belleza'), 
                     ('J','Joyeria'),      
                     ('R' ,' Ropa'),       
                     ('N' ,' Numerario'),
                     ('O', 'Otro'),
                      )
      
    Clasificacion = models.CharField(max_length= 2, choices = clase_indicio, default = 'A')
    
    Si_No = ( ('S', 'Si'),
              ('N', 'No'),
            )           
    Deposito_Banco = models.CharField(max_length = 1, choices = Si_No, default = 'S')
    Cantidad  = models.IntegerField(default=0)


    Entrega = models.ForeignKey('Mp', on_delete = models.SET_NULL, null = True)  

    sicadena = ( ('S', 'Si'),
               ('N', 'No'),
               ('CS', 'Copia Simple'),
               ('CC', 'Copia Certificada'),
               )

    Cadena  = models.CharField(max_length = 2, choices = sicadena, default = 'S')

    tipo_embalaje = ( ('B',  'Bolsa de Plastico'),
                      ('BP', 'Bolsa de Papel'),
                      ('SB', 'Sobre Blanco'),
                      ('SM', 'Sobre Manila'),
                      ('EM', 'Emplayado'),
                      ('CJ', 'Caja de Carton'),
                      ('SE', 'Sin Embalaje'),
                      ( 'O', 'Otro'),
                    )
    Embalaje = models.CharField(max_length = 2, choices = tipo_embalaje, default = "B")
    edo_ambalaje = ( ('C','Cerrado'),
                     ('A', 'Abierto'),
                     ('AL', 'Alterado'),
                     ('R', 'Roto'),
                     ('O', 'Otro')
                    )

    Estado_embalaje = models.CharField(max_length = 2, choices = edo_ambalaje, default = "C")

    Ubicacion = models.CharField(max_length = 10, help_text ='Ingrese ubicacion del indicio')
    Imagen = models.ImageField(upload_to="userlogo/", blank=True, null=True) 
    Observaciones = models.TextField(max_length = 200, help_text= 'Aqui puede hacer observaciones del indicio y embalaje, entre otras')
    def __str__(self):  
       return '%s (%s)' % (self.Expediente,self.Rue)     
      
          





