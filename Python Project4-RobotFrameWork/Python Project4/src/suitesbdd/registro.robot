*** Settings ***

Resource     ../main.robot

*** Test Cases ***

#Escenario 01: Crear un usuario - exitoso
 #   Abrir browser
  #  Dado que accedo a la página de inicio de sesión del sistema
   # Y creo un nuevo usuario
    #Cuando complete el registro     ${true}
    #Entonces validar si el usuario fue creado con éxito
    #Close Browser

#Escenario 02: Crear un usuario - exitoso
 #   Abrir browser
  #  Dado que accedo a la página de inicio de sesión del sistema
   # Y creo un nuevo usuario
    #Cuando complete el registro     ${false}
    #Entonces validar mng no exitoso
    #Close Browser
#Escenario 03: iniciar sesión con un usuario ya registrado
 #   Abrir browser
  #  Dado que accedo a la página de inicio de sesión del sistema
   # y ingreso los datos de inicio de sesion
    #close browser


Escenario 04: Crear un usuario y hacer una compra
     Abrir browser
     Dado que accedo a la página de inicio de sesión del sistema
     Y creo un nuevo usuario
     Cuando complete el registro    ${true}
     Entonces validar si el usuario fue creado con éxito
     Y adiciono un producto en la categoría  WOMEN
     close browser


