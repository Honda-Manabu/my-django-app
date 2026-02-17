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
### Note (10):
#### Alternatively, run curl from another terminal while the virtual environment is active.
```
    bitnami@ip-172-26-15-83:~$ curl -I http://52.69.81.143:8000/
        HTTP/1.1 200 OK
        ...

    Hello, Django!
```
### Note (11):
#### Verifying Gunicorn installation
```
    ((venv) ) bitnami@ip-172-26-15-83:/opt/bitnami/projects/
    my-django-app$ pip freeze | grep gunicorn
        gunicorn==23.0.0
```
### Note (12):
#### Methods other than sudo nano
Even if I created it locally and tried to copy it using FTS, it would be rejected due to root privileges and wouldn't be able to be placed. So I intentionally placed it in the opt directory and moved it.
```
    sudo mv mydjango.service /etc/systemd/system/
```
### Note (13):
#### Memo
Coordinating Gunicorn and Apache proved difficult, leading to ChatGPT going around in circles and never arriving at a solution. Inductively, even after correcting the code, the old executable format remained in Apache, and ChatGPT's reasoning was riddled with errors, so one correction led to other errors. These factors combined to cause confusion, making it impossible to confirm the correct location. Another issue was a change in Bitnami's specifications, which caused the automatic update of bncert-tool to end with an error, resulting in an expired certificate (HTTP worked, but HTTPS was inaccessible).

In conclusion, Gemini was able to help us solve this issue as well, but the crucial chat records were lost, making it impossible to trace the correct procedure. The chat with ChatGPT went on for so long that I began to organize the steps of the work I had done so far, trying to determine what had been completed and what hadn't. Partway through, I realized that it would be better to create a ReadMe.md file directly, and it looks like this process will take two months.
### Note (14):
#### caution
If the procedure is correct from the beginning, there is no problem. However, if necessary corrections are missing, you may need to modify the code and clear the DNS cache in your browser and Windows. Alternatively, you can run the process in your browser's "private browsing mode," such as "Secret Mode" in Chrome.
### Note (15):
#### stumble
ChatGPT also completely identified the cause on November 30, 2025. The SSL certificate expired on November 13, 2025. However, there were numerous incorrect answers and inconsistencies along the way. There was an underlying assumption that the certificate should be automatically renewed. Furthermore, while checking the update status, I was asked to view the full text of bitnami-ssl.conf, and when I did so, ChatGPT changed course and concluded that the cause was the .conf settings. I found myself going around in circles with no end in sight. After a month, I finally gave up and terminated the chat. As mentioned above, I solved the problem with Gemini. The response patterns were very similar, but ChatGPT seemed more opinionated, and Gemini seemed more trustworthy.

After that, I tried running bncert-tool manually, but I'll skip that as it's off topic. For reference, I've included the Bitnami Django SSL auto-update setting Cron registration for "Standalone mode".
```
Bash
    sudo nano /opt/bitnami/letsencrypt/renew-certificate.sh
        #!/bin/bash

        # 1. Apacheを停止してポート80を空ける
        sudo /opt/bitnami/ctlscript.sh stop apache

        # 2. SSL証明書の更新 (Standaloneモード)
        # --http ポート80を使用して直接認証を行います
        sudo /opt/bitnami/letsencrypt/lego
         --path /opt/bitnami/letsencrypt \
        --email="honda-m103742@coast.ocn.ne.jp" \
        --domains="michealfamily.com" \
        --http \
        renew --days 30

        # 3. Apacheを再起動（更新が成功しても失敗しても実行）
        sudo /opt/bitnami/ctlscript.sh start apache

    sudo chmod +x /opt/bitnami/letsencrypt/renew-certificate.sh

    sudo crontab -u bitnami -e
    (Replace the current line)
        34 6 1 * * /opt/bitnami/letsencrypt/renew-certificate.sh > /opt/bitnami/letsencrypt/renewal.log 2>&1
```
Checking the update status
```
Bash
    cat /opt/bitnami/letsencrypt/renewal.log
```
### Note (15):
#### Configuring for a Docker environment
Here I am again, moving from traditional to modern methods. I recommended AI three months ago, and now I'm being told it's a double whammy. It's inevitable in two ways. Generative AI is the reason I'm making progress. Similarly, talented developers around the world are speeding up and working on better automation. Meanwhile, I'm completely self-taught, and my 70-something brain has forgotten what I did three months ago. I thought Docker was a given, but ChatGPT pointed out my mistake. I chose to use SQLite as my database (still using SQLite) so I could focus on that while building my development environment. Now I'll correct course and move forward with the de facto standard configuration of Django + PostgreSQL. Hopefully, by the time this is over, I won't have to call it traditional again!
