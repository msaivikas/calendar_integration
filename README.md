# calendar_integration

I've used WSL ubuntu on vscode while working on this project.
Clone the project using github
Get into the folder and then into 'calint' which is a short notation for 'calendar integration' using django-python
You need to run the command 'python3 apps.py' 
Make sure that you run this command inside the 'calint' folder which contains 'apps.py' inside the folder 'calint' which is different from main project folder 'calendar_integration'
Now when you run this command, it should automatically open a google authentication page and when you accept it, it specifically mentions the kind of permissions it needs. As we only need 'read only' access, we can also just use 'https://www.googleapis.com/auth/calendar.events.readonly' API. We can minimize the scopes to decrease the amount of control that we have on the user account.
As you open the currently obtained link after running the command, you'll be asked to login using your google account.
Currently the test users were just limited to 2 of my accounts while creating the project in Google developer console. 
We need to add more test users if it needs to work on other accounts as I'm not interested in using this app to take permissions of every other google calendar user.
When you give required permissions to the app with your google account, it'll show you the event list corresponding to your permitted google account. 
For example, this is my obtained event list screenshot in vscode terminal below.

![image](https://user-images.githubusercontent.com/112486342/215845682-2610dd8e-e051-4d70-84f0-b075f42d85af.png)
![Screenshot (34)](https://user-images.githubusercontent.com/112486342/215845805-20ffe9a2-13cf-4593-8dfb-1b620b3e99b3.png)
