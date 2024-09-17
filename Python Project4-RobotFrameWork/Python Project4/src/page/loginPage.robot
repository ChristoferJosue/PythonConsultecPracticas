*** Settings ***
Library    SeleniumLibrary

*** Variables ***
&{login}
...     buttonSinginMenu=//a[contains(text(),'Sign in')]
...     inputCreateAccount_Email=//input[@id='email_create']
...     buttonCreateAnAccount=//span[contains(.,'Create an account')]
...     inputSignIn_Email=//input[@id='email']
...     inputSingIn_Password=//input[@id='email']
...     buttonSingIn=//span[contains(.,'Sign in')]
...     email_suces=teste_michael@vorak.com
...     password_sucess=teste@123
...     login.buttonSingIn=//*[@id="SubmitLogin"]/span

*** Keywords ***
Dado que accedo a la página de inicio de sesión del sistema
    click element    ${login.buttonSinginMenu}
Y ingreso los datos de inicio de sesion
    input Text    ${login.inputSignIn_Email}    ${login.email_suces}
    Input Text      ${login.inputSingIn_Password}    ${login.password_sucess}
    Click Element       ${login.buttonSingIn}


