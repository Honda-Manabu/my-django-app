# **Note**
###  **Note (1)**
**Statement:**
Getting an AI to concisely answer only the questions you really want to know is extremely difficult. Because AI doesn't understand the meaning of words, its answers will inevitably contain errors. After much trial and error, I had to revise my work plan.
1. I created a local Django project for code development.
2. I created a Lightsail Django instance and built an online environment for my Django app.

Based on my experience, I knew that my first attempt wouldn't go smoothly, so I first understood the process above, then revisited it.

3. I've now moved on to the steps to get everything running in a GitHub, Django, and AWS/Lightsail cloud environment.

### Note (2):
If the Git path is not registered in the Windows environment variable PATH when you install Git, add it by editing the system environment variables.
```
C:\Program Files\Git\bin
C:\Program Files\Git\cmd
(or Program Files (x86))
```
###  **Procedure (1)**
### **Ⅰ. Local Django Development Environment Setup Instructions (Windows + VS Code)**
1. Create a working directory  and open it in VS Code.
```
C:\projects\<directory name>
```
2. Create a virtual environment:
```
python -m venv venv
```
3. Activate the virtual environment:
```
.\venv\Scripts\activate
```
4. Install Django:
```
>>> pip install django
```
5. Create a Django project:
```
>>> django-admin startproject my_django_app .
```
6. Start the development server:
```
>>> python manage.py runserver
```
7. Check http://127.0.0.1:8000 in your browser.
```
Note:After executing the command, you will often need to exit the program. such as pressing Ctrl+C, deactivate, or q (exit).
```
###  **Note (3)**
I have a Word document that documents the main points of what I learned and the chronological order of the work that I did. If I organized it, I could have made it into a work procedure manual. Despite my nine years of experience, I must confess that the records are too long and confusing to refer to later. The following work procedure has been reconstructed by going back through the last steps that went well.
###  **Procedure (2)**
### **Ⅱ. Online Django Environment Setup Guide (Bitnami Django on AWS Lightsail)**
####  myproject : <my Django_project_directory>
1. SSH Login:
```
ssh -i
Private Key File: <YOUR_KEY.pem>
Connection Destination: bitnami@<YOUR_LIGHTSAIL_IP>
```
2. Project Deployment:
```
sudo mkdir -p /opt/bitnami/projects/myproject
sudo chown -R bitnami:bitnami /opt/bitnami/projects/myproject
cd /opt/bitnami/projects/myproject
```
3. Create and Activate a Virtual Environment:
```
python3 -m venv venv
source venv/bin/activate
```
4. Install Django:
```
>>> pip install django
```
5. Create a Project:
```
>>> django-admin startproject myproject .
```
6. Create an Admin User:
```
cd your_project_directory
python manage.py migrate
python manage.py createsuperuser
```
7. Collect Static Files:
```
python manage.py collectstatic --noinput
```
8. Apache VirtualHost configuration:

sudo nano /opt/bitnami/apache/conf/vhosts/myproject-vhost.conf
#### Note: #This code was created by ChatGPT.
```
<VirtualHost *:80>
ServerName <YOUR_DOMAIN_OR_IP>
DocumentRoot "/opt/bitnami/projects/myproject"

<Directory "/opt/bitnami/projects/myproject">
AllowOverride All
Require all granted
</Directory>

WSGIDaemonProcess myproject
   python-path=/opt/bitnami/projects/myproject
   python-home=/opt/bitnami/projects/myproject/venv
WSGIProcessGroup myproject
WSGIScriptAlias ​​/ /opt/bitnami/projects/myproject/myproject/wsgi.py
</VirtualHost>
```
9. Restart Apache:
```
sudo /opt/bitnami/ctlscript.sh restart Apache
```
10. Check the admin page: http://<YOUR_LIGHTSAIL_IP>/admin

### Note (4):
Bitnami and other similar services are used by people all over the world, each with a different combination of apps and server environments. Therefore, adjustments are always necessary, but the reality is that they are very complicated. The freeware software itself is full of # (comment lines), with many lines of comment lines, and has only a few moving parts. I tried to understand where and what I had changed by commenting out the default settings, but even that was difficult.
### Note (5):　
#### If the port is in use, try 8001, 8002, etc.
（Windows PowerShell）

    netstat -ano | findstr :8000
        TCP    127.0.0.1:8000     0.0.0.0:0     LISTENING      99999
    tasklist /FI "PID eq 99999"
### Note (6):
- URL (title): https://zany-...8000.app.github.dev/

    Cannot be changed
- Only when creating a new repository locally for the first time

    `django-admin startproject <project-name>`

    Do not run this command this time.

### Note (7):
I used GitHub remote connection 3 or 4 years ago for CS50. I'll check it this time.
### Note (8):
#### Git operations in VS Code

1. Click the ✔ icon (Source Control)
2. View a list of modified, added, deleted, and renamed files
3. Click a file name to view the diff (diff)
4. Enter a commit message in the text box and click Commit (✓)
5. View the Sync Changes (🔄)
6. Click to push or click "..." in Source Control → Push
7. Click Source Control → ... → Pull or click the notification in the lower right
8. Branch operations: Click the current branch name (e.g., main) in the lower left
9. 🔁 Undo changes/unstage: Right-click the file name

### Note (9):
#### AWS Lightsail Side Verifying Completion
```
    1.SSH Login OK
    2.Git Package Installation OK
    3.Check Bitnami's Python/virtual environment
        bitnami@ip-172-26-15-83:~$ /opt/bitnami/
        python/bin/python3 --version
        Python 3.12.11
        bitnami@ip-172-26-15-83:~$ /opt/bitnami/
        python/bin/pip3 --version
        pip 25.1.1 from /opt/bitnami/python/lib/
        python3.12/site-packages/pip
        (python 3.12)
        bitnami@ip-172-26-15-83:~$ ls -l
        /opt/bitnami/projects total 8 drwxr-xr-x 6
        bitnami daemon 4096 Oct 12 23:07 myproject
        drwxr-xr-x 5 bitnami bitnami 4096Nov 1
        11:48 venv
 ```
