*** Settings ***
Resource    ../main.robot

*** Variables ***
&{hooks}
...    URL=http://www.automationpractice.pl/index.php
...    BROWSER=chrome

*** Keywords ***
Abrir browser
    open browser    ${hooks.URL}    ${hooks.BROWSER}
    maximize browser window

