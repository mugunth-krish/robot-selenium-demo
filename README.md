# robot-selenium-demo
Library setup and execution :
1) Run setup.sh using cmd -->  ```./setup.sh```
2) To run the robot file  -->  ```browserstack-sdk robot <your_filename>.robot```


## Task 1
Create task1.robot

Perform a login with instructions provided in the URL
    https://practicetestautomation.com/practice-test-login/

Use robotframework-selenium and Builtin libraries with Robot framework to do the automation
https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
https://robotframework.org/robotframework/latest/libraries/BuiltIn.html 


After login verify if the webpage contains ‘Logged In Successfully | Practice Test Automation’

Use ```browserstack-sdk robot task1.robot```

## Task 2

Create task2.robot

Perform a login with instructions provided in the URL
    https://practicetestautomation.com/practice-test-login/

Use selenium and CustomLib.py with Robot framework to do the automation
Fill the CustomLib.py with relevant methods and use it in Task2.robot
Libraries have been imported in CustomLib already.

Use ```browserstack-sdk robot task2.robot```


