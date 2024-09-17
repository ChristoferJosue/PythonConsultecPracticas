*** Settings ***
Library    SeleniumLibrary

*** Variables ***

&{addNewUser}
...    URL=http://www.automationpractice.pl/index.php
...    inputCreateAccount_Email=//input[@id='email_create']
...    buttonCreateAnAccount=//button[@id='SubmitCreate']
...    radioTitle=//div[@id ='uniform-id_gender1']
...    inputFirstName=//input[@id='customer_firstname']
...    inputLastName=//input[@id ='customer_lastname']
...    actionButtonEmail=//input[@id ='email']
...    actionButtonPassword=//input[@id ='passwd']
...    selectBirthDay=//select[@id ='days']
...    selectBirthMonth=//select[contains(@id,'months')]
...    selectBirthYear=//select[contains(@id,'years')]
...    buttonRegister=//button[@id ='submitAccount']

*** Keywords ***
Y creo un nuevo usuario
    ${random_value} =   Evaluate    random.randint(0,100000)
    Input Text  ${addNewUser.inputCreateAccount_Email}  javierry${random_value}@vorak.com
    click element    ${addNewUser.buttonCreateAnAccount}

Cuando complete el registro
    [Arguments]    ${fillAll}
    BuiltIn.Sleep   3s
    Wait Until Page Contains Element    ${addNewUser.radioTitle}
    Click Element   ${addNewUser.radioTitle}
    run keyword If  ${fillAll}  completar los campos del registro del formulario
    click element    ${addNewUser.buttonRegister}

Completar los campos del registro del formulario

    Input Text  ${addNewUser.inputFirstName}    Michael
    input text  ${addNewUser.inputLastName}     Alba
    click element    ${addNewUser.actionButtonEmail}
    input text    ${addNewUser.actionButtonPassword}    Teste@123
    Select from list by index    ${addNewUser.selectBirthDay}   5
    Select from list by index    ${addNewUser.selectBirthMonth}   2
    select from list by value    ${addNewUser.selectBirthYear}   1994

Entonces validar si el usuario fue creado con éxito
    Page Should contain     Your account has been created

Entonces validar mng no exitoso
    Page Should Contain     There are 3 error

