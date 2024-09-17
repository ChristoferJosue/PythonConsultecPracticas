*** Settings ***

Resource     ../main.robot

*** Test Cases ***

Escenario 01: Crear un usuario - exitoso
    Abrir browser
    Dado que accedo a la página de inicio de sesión del sistema
    Y creo un nuevo usuario
    Cuando complete el registro     ${true}
    Entonces validar si el usuario fue creado con éxito
    Close Browser

