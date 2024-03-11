from django.db import models

# HERENCIA DE MODELOS
class CRideModel(models.Model):
    """
     Comparte Ride base model
     
     CRirdeModel actua como una clase base abstracta a partir de
     la cual cada model en el proyecto heredará. Esta clase provee con los siguientes atributos:
        - created
        - modified
    """
    
    created = models.DateTimeField("created_at", 
                                   auto_now_add=True,
                                   help_text="Date time on which the object was created")
    
    modified = models.DateTimeField("modified", 
                                    auto_now=True,
                                    help_text="Date time on which the object was last modified")
    class Meta:
        
        abstract = True
        
        get_latest_by = "created"
        
        ordering = ['-created', '-modified']
        
        
# MODELO PROXY

# class Person(models.Model):
#     full_name = models.CharField(max_length=100)
    
# class MyPerson(Person):
#     class Meta:
#         proxy = True
        
#     def do_something(self):
#         pass