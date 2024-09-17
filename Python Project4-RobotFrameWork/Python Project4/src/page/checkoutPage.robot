*** Settings ***
Library  SeleniumLibrary

*** Variables ***
&{checkout}
...    productBlouse=http://www.automationpractice.pl/index.php?id_product=2&controller=product
...    productColorBlack=//a[contains(@class,'color_pick selected')]
...    productColorWhite=//a[contains(@name,'White')]
...    buttonAddToCart=//*[@id="add_to_cart"]/button/span
...    buttonPreceedToCheckout=//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span
...    buttonPreceedToCheckoutt2=//*[@id="center_column"]/p[2]/a[1]/span
...    addressAddress=//input[@id='address1']
...    addressCity=//input[@id='city']
...    addressState=//select[@id='id_state']
...    addressZipCode=//input[@id='postcode']
...    addressHomePhone=//input[@id='phone']
...    addressCelPhone=//input[@id='phone_mobile']
...    buttonSaveAdress=//*[@id="submitAddress"]/span
...    buttonPreceedToCheckoutt3=//*[@id="center_column"]/form/p/button/span
...    buttonAcceptTerms=//input[@id='cgv']
...    buttonPreceedToCheckoutt4=//*[@id="form"]/p/button/span
...    buttonPayByCheck=//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a
...    buttonConfirmMyOrder=//*[@id="cart_navigation"]/button/span

*** Keywords ***
Y adiciono un producto en la categoría
    [Arguments]  ${category}
    Click Element    //a[translate(text(), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')='${category}']
    go to    http://www.automationpractice.pl/index.php?id_product=2&controller=product
    #Click Element    ${checkout.productBlouse}
    BuiltIn.Sleep  4s


    click element    ${checkout.productColorWhite}
    Wait Until Page Contains Element  ${checkout.buttonAddToCart}
    Click Element    ${checkout.buttonAddToCart}
    BuiltIn.Sleep  3s
    Wait Until Page Contains Element  ${checkout.buttonPreceedToCheckout}
    Click Element    ${checkout.buttonPreceedToCheckout}
    BuiltIn.Sleep  3s
    Wait Until Page Contains Element  ${checkout.buttonPreceedToCheckoutt2}
    Click Element    ${checkout.buttonPreceedToCheckoutt2}
    BuiltIn.Sleep  3s
    Input Text  ${checkout.addressAddress}   Fernanda Bella 705
    Input Text  ${checkout.addressCity}   Sorocaba
    Select From List By Index  ${checkout.addressState}  3
    Input Text  ${checkout.addressZipCode}  10001
    Input Text  ${checkout.addressHomePhone}  11988364275
    Input Text  ${checkout.addressCelPhone}  10001
    Click Element    ${checkout.buttonSaveAdress}
    BuiltIn.Sleep  2s
    Wait Until Page Contains Element  ${checkout.buttonPreceedToCheckoutt3}
    Click Element    ${checkout.buttonPreceedToCheckoutt3}
    Wait Until Page Contains Element  ${checkout.buttonAcceptTerms}
    Click Element    ${checkout.buttonAcceptTerms}
    Wait Until Page Contains Element  ${checkout.buttonPreceedToCheckoutt4}
    Click Element    ${checkout.buttonPreceedToCheckoutt4}
    Wait Until Page Contains Element  ${checkout.buttonPayByCheck}
    Click Element    ${checkout.buttonPayByCheck}
    Wait Until Page Contains Element  ${checkout.buttonConfirmMyOrder}
    Click Element    ${checkout.buttonConfirmMyOrder}
    Page Should Contain  Your order on My Shop is complete.