### **My project title**
# **Generate My own Website**
## **subtitle:** Creating a GitHub Codespaces development and production environment on an AWS LightSail Django instance.
#### Video Demo:  <URL HERE>()
#### Description:
## **Background of theme selection**
Having just retired from a 40-year career as a corporate employee, I found myself living every day like a Sunday, eager to do something I hadn't been able to do before. Also, trying new things can help with anti-aging. I decided to become a web designer, but nine years later, my MySite is still under construction.

I started this introductory course in the summer of 2021, which current students would complete in one semester. I haven't stopped. With the help of Duck AI, I managed to reach the Final Project. It would have been so much better if I had focused on this account from the beginning. Creating a web page involved learning a vast amount of knowledge that I wasn't sure would ever be useful, struggling, and then ultimately discarding it all. I've even forgotten the names of the development environment and page creation software my first teacher recommended. Three years later, I decided to use Linux and WordPress on AWS Lightsail, but at the time, just creating the instance and setting it up took countless hours. Now, most of the process is automated and can be completed in minutes. When it came time to work with the database, I suddenly couldn't log in to the admin board. I was bogged down in a loop between AWS, Bitnami, and WordPress, and paid support was no help at all, which was frustrating. Just when I was starting to have doubts about navigating the WordPress maze, where the latest specifications coexist with legacy relics, I finally submitted my first sensible work for the Homepage assignment in CS50X, which covered Python, SQL, HTML, CSS, JavaScript, and (Flask is not available) in a short period of time that made me wonder what all those years had been.

After eight years of research and research, where new things replaced the actual work and I had barely accumulated any useful knowledge, I decided to start again with a new approach.
## **Project Objectives**
### **To earn a certificate of completion for "CS50's Introduction to Computer Science."**
### **It also marks the culmination of nine years of struggling with web-related software.**

The project I'm sharing here was decided after numerous questions to ChatGPT. However, since starting this project, I've realized that the wonderful world of open source software can be very difficult for beginners, with so many different versions and approaches. For example, the official documentation for setting up Apache web server software on an AWS Bitnami-Django instance is often difficult to understand and extremely incomplete. It's impossible to complete without the help of generative AI. So, by recording my detours and what works well in this project, I hope to inspire freeware developers to automate their own projects.
# **Step1: Project overview**
[1] Preparing the local Code development environment

[2] Building a Lightsail instance & the Django online app settings

[3] Creating a cloud development environment with GitHub Codespaces

[4] Bitnami, Apache and Django deploying and configuring

[5] Staging server environment generation, operation check, publication, and operational evaluation

[6]Creating a Mysite and publishing it on the web - Renewing the CS50 Problem Set 8 Homepage with Flask.

[7]Creating a final project submission and receiving a certificate of completion.

##### **References: Note (1)**
## **Work Plan**
### **[1] Django local development environment setup**
##### **References: Note (2)**
##### **References: Procedure (1)**
### **[2] Creating an AWS Lightsail (Bitnami Django) instance**
#### **(1)Creating a Django instance and more**
   ①Creating an instance itself takes just a few minutes.

   ②initial setup has been largely automated over the past few years.
   ```
DNS settings, domain assignment, IP address forwarding settings, certificate issuance, etc.
   ```
##### **References Figure 1:[Creating an AWS Lightsail instance]**

③PUTTY usage settings: To access the development management board, a port tunnel connection is made. (SSH connection itself can be made from the instance-specified port.)

④FileZilla Client settings:(SFTP is required for Requirements updates of Apache and Bitnami, and Server Search)


### **[3] Django online development and operation environment setup**
##### **References: Note (3)**
##### **References: Procedure (2)**
##### **References: Note (4)**

### **[4] Bitnami, Apache and Django deploying and configuring with GitHub Codespaces**
#### Discription : [2] has already been executed, and [1] and [3] will be re-executed and additional work will be performed.  The execution results of [1], [2], and [3] are described as Procedure A. After that, new work will begin and the subsequent work is described as Procedure B.
### **[4]-Procedure A**
#### **[4]-A1-0 Environment Configuration and Prerequisites**
```
- AWS Lightsail Bitnami Django (Apache + Gunicorn)
- Django virtual environment (venv)
- AWS Route53, two domains
- GitHub account
```
**[4]-A1-1 (Windows PowerShell) Activating the Python virtual environment**
```
Open the project folder in VS Code
cd C:\projects\< project directory >
.\venv\Scripts\activate → Launch the virtual environment
(venv) PS C:\projects\< project directory >> pip freeze | findstr
   Django
   Django==4.2 LTS
(venv) PS C:\projects\< project directory >> pip install -r requirements.txt
   ((pip install django)(python -m pip install --upgrade pip))
(venv) PS C:\projects\< project directory >> python -m pip install --upgrade pip
   Requirement already satisfied:～Successfully installed pip-25.3
(venv) PS C:\projects\< project directory >> python manage.py runserver
   ～System check identified no issues (0 silenced).～
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.

```
Check browser access via http://127.0.0.1:8000/ or http://localhost:8000/
##### **References: Note (5)**　If the port is in use,
**[4]-A1-2 Log in to GitHub**
```
   <user name> /< project name >     Repository exists
   manage.py,<project_name>/settings.py
   and requirements.txt exists.
```
**[4]-A1-3 Edit the blank requirements.txt file**

   using the "✏ Edit" button → Commit:
```
   Django>=4.2,<5.0
   Gunicorn
   python-dotenv
```
**[4]-A1-4 Create a GitHub repository for Django**

   https://github.com/\<user name\>/\<project name\>

 Create a new repository from the GitHub Web UI.**
```
   Create a new repository → Check "Add a README" →
   Add .gitignore → Select "Python"
```
**[4]-A1-5 Launch GitHub Codespaces and configure local Git integration.**
```
   Repository → Green Code button → Codespaces tab →
   Select "Create codespace on main"
```
After launching Codespaces, open Extensions (square icon) in the left sidebar and confirm that it's installed.
```
   - Python (ms-python.python)
   - Django
   - GitLens  (Optional)
```
**[4]-A1-6 Open VSCode in your browser → Launch New Terminal from the menu.**

@Honda-Manabu ➜ /workspaces/<project-name> (main)
```
   $ python3 –version
      Python 3.12.1
      pip install -r requirements.txt
   $ python3 -m django –version
      4.2.26
   $ python3 manage.py runserver 0.0.0.0:8000
      System check identified no issues (0 silenced).
      November 19, 2025 - 06:47:07
      Django version 4.2.26, using settings
      'my_django_project.settings'
      Starting development server at http://0.0.0.0:8000/
   Quit the server with CONTROL-C.
```
Display the Django homepage: "Hello, Django!"

The Django development server successfully starts on Codespaces
##### **References: Note (6)**  Bookmark the dedicated domain for opening the editor.
**[4]-A1-7 GitHub integration (remote connection)**

##### **References: Note (7)**　Confirming past experiences
Confirm Git initial setup
```
   PS C:\projects\<project directory>> git --version
      git version 2.50.1.windows.1
   PS C:\projects\<project directory>> git config --global user.name
      "Honda-Manabu"
   PS C:\projects\my-django-app> git config --global user.email
      "honda-m103742@coast.ocn.ne.jp"
   PS C:\projects\my-django-app> git config --list
      …
   :        exit
```
```
   PS C:\projects\<project directory>> git init
      Reinitialized existing Git repository in C:
      /projects/<project directory>/.git/
   PS C:\projects\<project directory>> git add .
      warning: in the working copy of 'my_django_project/.env.example',
      LF will be replaced by CRLF the next time Git touches it
      warning: in the working copy of 'my_django_project/conf/bitnami/
      bitnami.conf', LF will be replaced by CRLF the next time
      Git touches it
      warning: in the working copy of 'my_django_project/vhostts/
      myproject-vhost.conf', LF will be replaced by CRLF the next time
      Git touches it
   PS C:\projects\<project directory>> git commit -m "Initial commit"
      …
```
Confirm GitHub remote settings
```
   PS C:\projects\<project directory>> git remote -v
      origin https://github.com/<your user.name>/<project directory>
      .git (fetch)
      origin https://github.com/<your user.name>/<project directory>
      .git (push)
   PS C:\projects\<project directory>> git push -u origin main
      …
```
##### **References: Note (8)**  Git operations in VS Code

#### **[4]-A2 Preparation on AWS Lightsail**

For information on creating and initializing a Bitnami Django instance, see [2] Creating an AWS Lightsail (Bitnami Django) instance.

##### **References: Note (9)** 　Verifying Completion
**[4]-A2-1 Setting up Git on your Lightsail Django instance**

Connect via SSH using PuTTY or the SSH button in the Lightsail instance's connection tab:
```
   bitnami@ip-172-26-15-83:~$ sudo apt update Get:1
   file:/etc/apt/mirrors/debian.list Mirrorlist [38 B]
   …
   2 packages can be upgraded. Run 'apt list --
   upgradable' to see them.
```
```
   bitnami@ip-172-26-15-83:~$ sudo apt install git -y
   Reading package lists... Done
   …
   git is already the newest version (1:2.39.5-
   0+deb12u2). 0 upgraded, 0 newly installed, 0
   to remove and 2 not upgraded.
```
**[4]-A2-2 Display your Lightsail public key and register it on GitHub.**

Generate a key (Ed25519)(with the SSH connection established above)
```
   ssh-keygen -t ed25519 -C "your-email@example.com"
   (Your GitHub registered email address)
   (Press Enter repeatedly.)
   Enter file in which to save the key
      (/home/bitnami/.ssh/id_ed25519):
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
      SHA256:sxwE8bJBU05zoy4VH0AcTEDllrfzPyrn38WK
      ZSOApdYyour-email@example.com
      The key's randomart image is:
      +--[ED25519 256]--+
      | .BX@o+ |
      | . BoB o |
      | o X + |
      | O * . |
      | o S E |
      | + + + . |
      | o o + o|
      | . .*.+.|
      | ++o+..|
      +----[SHA256]-----+
```
Create two files: ~/.ssh/id_ed25519 (private key) and ~/.ssh/id_ed25519.pub (public key)

Display your public key and Register on GitHub
```
   cat ~/.ssh/id_ed25519.pub

   Copy the displayed key → GitHub Click your profile
   icon → Settings → In the left sidebar, under
   "Access," click SSH and GPG keys → New SSH key →
   Title:Lightsail Django → Key:Paste → Add SSH key
```
Confirming the connection
```
   bitnami@ip-172-26-15-83:~$ ssh -T git@github.com
(first time connection)
   The authenticity of host 'github.com
   (20.27.177.113)'can't be established. ED25519 key
   fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/
   zLDA0zPMSvHdkr4UvCOqU.
   This key is not known by any other names.
   Are you sure you want to continue connecting
   (yes/no/[fingerprint])?
   yes                     (y Not possible)
   Warning: Permanently added 'github.com' (ED25519) to
   the list of known hosts.
   Hi Honda-Manabu! You've successfully authenticated,
   but GitHub does not provide shell access.
```
**[4]-A2-3 Clone a Django project from GitHub to Lightsail**

Check the URL at the top of your GitHub repository.
```
   https://github.com/[your user.name]/[your repository name]
```
Execute git clone and verify.
```
   bitnami@ip-172-26-15-83:/opt/bitnami/projects$ git clone
   git@github.com:Honda-Manabu/my-django-app.git
      Cloning into 'my-django-app'...
      remote: Enumerating objects: 47, done.
      …Resolving deltas: 100% (12/12), done.
   bitnami@ip-172-26-15-83:/opt/bitnami/projects$ ls -l
   /opt/bitnami/projects
      total 12
      drwxr-xr-x 5 bitnami bitnami 4096 Nov 21 21:56 my-django-app
      drwxr-xr-x 6 bitnami daemon 4096 Oct 12 23:07 myproject
      drwxr-xr-x 5 bitnami bitnami 4096 Nov 1 11:48 venv
```
**[4]-A2-4 Create a separate venv for each project (my-django-app)**

The procedure is the same as [4]-A1-1.
```
   cd /opt/bitnami/projects/my-django-app
   /opt/bitnami/python/bin/python3 -m venv venv
   source venv/bin/activate

   ((venv) ) bitnami@ip-172-26-15-83:
      pip install --upgrade pip
      pip install -r requirements.txt
```
Modify settings.py ALLOWED_HOSTS
```
   [ host.strip() for host in os.getenv("DJANGO_
   ALLOWED_HOSTS", "").split(",") if host.strip() ]
   →
   ALLOWED_HOSTS = ['<your domain>',
      'www.<your domain>',
      '00.00.00.000',     #<your ip address>
      '127.0.0.1',
      'localhost',
      ]
```
**[4]-A2-5 Django DB migration and static file collection**

Continue with the above virtual environment active.
```
   ((venv) ) bitnami@ip-172-26-15-83:/opt/bitnami/projects/
   my-django-app$
         ./venv/bin/python manage.py migrate
         Operations to perform:
          Apply all migrations: admin, auth, contenttypes,
          sessions Running migrations:
         No migrations to apply.

   (Set STATIC_ROOT)
         python manage.py collectstatic --noinput
         125 static files copied to '/opt/bitnami/projects/
         my-django-app/staticfiles'.
```
**[4]-A2-6 Verify the Django development server is working**
```
   ((venv) ) bitnami@ip-172-26-15-83:/opt/bitnami/projects/
   my-django-app$
      python manage.py runserver 0.0.0.0:8000
         Watching for file changes with StatReloader
         Performing system checks...
         System check identified no issues (0 silenced).
         November 25, 2025 - 04:29:56
         Django version 4.2.26, using settings
         'my_django_project.settings'
         Starting development server at http://0.0.0.0:8000/
         Quit the server with CONTROL-C.

   ((venv) ) bitnami@ip-172-26-15-83:/opt/bitnami/projects/my-django-app$ curl -I http://<00.00.00.000>:8000/
      HTTP/1.1 200 OK
      ...
      Hello, Django!
```
##### **References: Note (10)** Alternatively, run curl
### **[4]-Procedure B**
#### **[4]-A3 Django Settings (Second Half)**

**[4]-A3-1 Gunicorn startup test and persistence**
##### **References: Note (11)** Verifying Gunicorn installation
Test Gunicorn startup
```
   gunicorn --bind 0.0.0.0:8000 my_django_project.wsgi
   :application
      ...
      [2025-11-26 21:32:13 +0900] [918406] [INFO] Booting worker
       with pid: 918406
```
Access http://00.00.00.000:8000/ and check if it displays.
            \<Your IP address>

**[4]-A3-2 Run Gunicorn as a resident service to automatically start it**

Create mydjango.service: ChatGPT support
```
   [Unit]
   Description=Gunicorn for my-django-app
   After=network.target

   [Service]
   User=bitnami
   Group=www-data
   WorkingDirectory=/opt/bitnami/projects/my-django-app
   Environment="PATH=/opt/bitnami/projects/my-django-app/venv/bin"
   ExecStart=/opt/bitnami/projects/my-django-app/
   venv/bin/gunicorn \
      --workers 3 \
      --bind unix:/opt/bitnami/projects/my-django-app/
      gunicorn.sock \
   my_django_project.wsgi:application

   Restart=always

   [Install]
   WantedBy=multi-user.target
```
Place it in /etc/systemd/system/mydjango.service.
##### **References: Note (12)** Methods other than sudo nano
Execute sequentially over an SSH connection
```
   bitnami@ip-172-26-15-83:/opt/bitnami/projects/my-django-app$
   sudo systemctl daemon-reload
   bitnami@ip-172-26-15-83:/opt/bitnami/projects/my-django-app$
   sudo systemctl enable mydjango Created symlink
      /etc/systemd/system/multi-user.target.wants/mydjango.service → /etc/systemd/system/mydjango.service.
   bitnami@ip-172-26-15-83:/opt/bitnami/projects/my-django-app$
   sudo systemctl start mydjango
   bitnami@ip-172-26-15-83:/opt/bitnami/projects/my-django-app$
   sudo systemctl status mydjango
      ● mydjango.service - Gunicorn for my-django-app Loaded:
      ．．．
      Nov 27 12:15:25 ip-172-26-15-83 gunicorn[922395]: [2025-11-27 12:15:25 +0900] [>
      lines 1-20/20 (END)

  (Stop Gunicorn:) Ctrl + C 
```
##### **References: Note (13)** Memo
 Regarding the following part [4]-A4, I cannot provide the execution procedure for the reasons mentioned above memo, so I will search for the current situation and present the work content.

**[4]-A4-1 Django settings: Modify settings.py**

Adding a static IP address of AWS Lightsail to [4]-A2-4 settings.py ALLOWED_HOSTS, was done at this point.
Also check the following:
```
   settings.py
      STATIC_URL = 'static/'
      STATIC_ROOT = BASE_DIR / "staticfiles"
```
**[4]-A4-2 Modify /opt/bitnami/apache/conf/httpd.conf**

Comment out and Add last line
```
   # Secure (SSL/TLS) connections
   # Include conf/extra/httpd-ssl.conf"
   # Memory settings
   Include "/opt/bitnami/apache/conf/bitnami/httpd.conf"
```
##### **References: Note (14)** caution
### **warning:** Bitnami's default settings must be maintained on the following settings.
Even if you try to replicate this section, various issues will arise depending on the environment and slight differences in settings.

**[4]-A4-3 Create only one Django.conf file in /opt/bitnami/apache/conf/vhosts.**
mydjango-vhost: (Name can be changed,conventionally, the project name is used.)
```
<VirtualHost *:80>
    ServerName michealfamily.com
    ServerAlias www.michealfamily.com

    # 静的ファイル
    Alias /static /opt/bitnami/projects/my-django-app/staticfiles
    <Directory /opt/bitnami/projects/my-django-app/staticfiles>
        Require all granted
    </Directory>
    # Gunicornへのプロキシ設定を安定化
    <Proxy http://127.0.0.1:8000>
        ProxySet timeout=60
    </Proxy>

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
    # Gunicorn UNIX socket
    #ProxyPass / unix:/opt/bitnami/projects/my-django-app/gunicorn.sock|http://localhost/
    #ProxyPassReverse / unix:/opt/bitnami/projects/my-django-app/gunicorn.sock|http://localhost/

    ErrorLog "/opt/bitnami/apache/logs/mydjango-error.log"
    CustomLog "/opt/bitnami/apache/logs/mydjango-access.log" combined
</VirtualHost>

<VirtualHost *:443>
    ServerName michealfamily.com
    ServerAlias www.michealfamily.com

    SSLEngine on
    SSLCertificateFile "/opt/bitnami/letsencrypt/certificates/michealfamily.com.crt"
    SSLCertificateKeyFile "/opt/bitnami/letsencrypt/certificates/michealfamily.com.key"
    #SSLCertificateFile "/opt/bitnami/apache/conf/bitnami/certs/server.crt"
    #SSLCertificateKeyFile "/opt/bitnami/apache/conf/bitnami/certs/server.key"
    <Proxy http://127.0.0.1:8000>
        ProxySet timeout=60
    </Proxy>
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/

    #ProxyPass / unix:/opt/bitnami/projects/my-django-app/gunicorn.sock|http://localhost/
    #ProxyPassReverse / unix:/opt/bitnami/projects/my-django-app/gunicorn.sock|http://localhost/

    ErrorLog "/opt/bitnami/apache/logs/mydjango-error.log"
    CustomLog "/opt/bitnami/apache/logs/mydjango-access.log" combined
</VirtualHost>
```
ChatGPT's initial code is only eight lines long, but the original is Bitnami's default settings (the code to be modified below), and we created it to modify based on the log and error messages.

**[4]-A4-4 Modify /opt/bitnami/apache/conf/bitnami/bitnami.conf**

Of the 40 lines of code, only the fourth line remains; the rest all comment out. Add an Include line:

bitnami.conf:
```
   EnvIf X-Forwarded-Proto https HTTPS=on
   ．．．
   Include "/opt/bitnami/apache/conf/vhosts/mydjango-vhost.conf"
```
**[4]-A4-5 Modifying bitnami-ssl.conf**

Change the certificate directory and file name. Adding an ErrorDocument is optional.

bitnami-ssl.conf：
```
   ．．．
   SSLCertificateFile "/opt/bitnami/letsencrypt/certificates
   /michealfamily.com.crt"
   SSLCertificateKeyFile "/opt/bitnami/letsencrypt/certificates
   /michealfamily.com.key"
   ．．．
   # Error Documents
   ErrorDocument 503 /503.html
```
##### **References: Note (15)** stumble
**[4]-A4-6 Check for Apache errors and restart**
```
bash
   sudo apachectl -t
      Syntax OK
   sudo /opt/bitnami/ctlscript.sh restart apache
      Restarted apache
```
Check the connection.
curl -I http://00.00.00.000/








