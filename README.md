# NightGuard-Proxy-Monitor
Since this solution aims to mitigate downtime of banking systems, the areas is currently valueble to the industry. Its need be accuracte and fidality when dealing with people's money. Therefore, development of the project basically covers protecting data and sensitive information, security of the valuable assests, decresing the downtime of the system and reducing company expenses. While developing the project we mainly focused on the above points as well as the security and the ease-of-use (usability) of the system.

# Design
The designing part consists of five major parts. First parts is the main stakeholder of the project. In this case its the Bank. Futhermore, the cash management systems, payment switches, netowrk management systems, terminal management systems and etc. are sub parts of the area.

Seconds place goes to the Proxy monitor and it basically checkes aliveness of the the above mentioned each area and communicates to the Alert Manager for triggering alerts.

Third place is the Alert Manager.  Basically, the alert manager receives inpits from the Proxy Monitor whether the are incidents and then trigging alarms among Stackeholders such as Technical & Non-Technical employees.

The proxy database takes the forth place of the design of this project and it primarary store incident details and manage them. It also holds employee details such as name, address, email, mobile numbers and emergency telephone number to provide to the system when needed.

The Final part of the design is the "Stakeholders". The employees who are receiving alerts when there is an incident are belongs to this area. There can be multiple categories of employees such as IT Specialists, System Engineers, Database Engineers, Development, Test and etc.

# Implementation
The implementation part does using the latest & secure technologies and Frameworks such as Python, Angular, Html, CSS, TyeScript. The implementation part mainly conststs a Backend, Frontend and a Database. For the database development part we used MySQL and the Aparche, Tomcat servers.

For the Backend, Python and related libraries are used. PyCharm IDE is used to develop the code.

Fort he Frontend, Angular framrwork with HTML, CSS and TypeScript used. and for the development, Visual Studio Code is used.

# Testing
Testing of the implementation mainly initiates as two stages. The first stage take place where the code is developing and integrating. A application called "Postman" used during this process. The second phase initiates when the development is 100% completed. During this phase we triggers manual failures of the developed system and verify whether the developed systsm reacts accordinly.

# Validation
To validate the project we use a predefined scenarios. As an example, Manually stop a module called Cash Management System and once the module stopped the Proxy Monitor identifies it within 20 seconds and thereafter, it stores the details in the database and then call the Alert Manager by passing the relevant data. The Alert Manager receives the message from the Proxy Monitor and it starts to send emails and notifications to the Stakeholders immedietly. The whole process takes up to 40 seconds when the incident happened.

# Critical Evaluation
This solution completly achived the intended aims and goals we planned during the planning and the documentation process. Since it reacts within 40 seconds once a incident happened, the solutions totally matches industry current purposes. Running this system on servers and maintainans, single maintainer guy and the hourly payments for Stakeholders when only incidents happenes are the only areas that the company has to care about. Therefore, we can get prove than the proposed solution met its aims & goals
