How to configure PyCharm for Odoo development in Windows?

	Installing Odoo in windows is the really easy task. We can do it by just running the ‘.exe’ file. But for development purposes, this method is not preferred. Pycharm is an IDE which can be used for Odoo development in Windows, Linux, and mac. In this blog, we will discuss setting up Odoo development environment in windows using pycharm.

These are the steps we need to follow.

1. Download and install python 2.7 from here
   https://www.python.org/downloads/release/python-2713/
   based on your system architecture.

2. After installing python, we need to install Microsoft Visual C++ compiler. Go to this link https://www.microsoft.com/en-us/download/details.aspx?id=44266
   Download and install it.

3. Download PostgreSQL and configure.
   https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows

a.Create a new user for Odoo
You can either create a user (role) using the pgadmin or directly from the command prompt. For creating a user with pgadmin, first, configure pgadmin and then go to the roles section and create a new role. Then under the privileges tab of this role, provide all the access.
From the command prompt, you can create the user with the following commands.
First, go to the postgresql installation directory using ‘cd’ (usually “C:\Program Files\PostgreSQL”)

cd "C:\Program Files\PostgreSQL\9.6\bin"

(Here ‘9.6’ is my postgresql version. Change it accordingly)

createuser.exe --createdb --username postgres --no-createrole --pwprompt odoo

You will be asked for the password, provide a password and remember it. We may need it during odoo installation.

4. Now download Pycharm from here https://www.jetbrains.com/pycharm/download/#section=windows  and install.

5. Download odoo https://github.com/odoo/odoo/archive/10.0.zip  and extract the contents to a folder.

6. Open pycharm and create a project with the folder which we have extracted in the last step.

7. Now we need to install some packages for odoo. In the extracted odoo folder, we can find a ‘requirements.txt’ file.
            > cd C:\ python27 (change to the location where python is installed. You can also do this from any location if you add python path to your system’s path variable.
For this, go to My PC > Properties > Advanced System Settings > Environment Variables > and edit the path and add your python path)
python -m pip install -r C:\Users\Odoo-10.0\requirements.txt  (we have to specify the ‘requirements.txt’ file with its complete path.)

8. Download and install pywin32 from here.
https://sourceforge.net/projects/pywin32/files/pywin32/Build%20217/
You need to download the correct version based on your system architecture and python.
Note that you cannot install 64 bit pywin32 on a system with 32-bit python installed. It will show an error saying that ‘Python is not found’.

9. Download and install pip.
https://bootstrap.pypa.io/get-pip.py  . Download the file get-pip.py and move it to python installation location.

		> cd C:\python27
		>python get-pip.py

10. Now we need to configure odoo.
Open pycharm and edit the file ‘odoo-server.conf’  (usually, this file may be inside the Debian folder in odoo’s folder)
		Edit the contents like this,

		; admin_passwd = admin
		db_host = localhost
		db_port = 5432
		db_user = odoo
		db_password =odoo (the password you have provided when the user is created)
		addons_path = C:\Users\odoo10\addons

	You can change the default port of odoo by using ‘xmlrpc_port = new port no.’

11.Additional installations
We need to install some other features also, for working without errors.

- Install setuptools.
		From cmd, run
			> cd C:\python27
			> python -m pip install --upgrade setuptools

- Install Wheel & Lxml-3.6.4-cp27-cp27m-win32.Whl
			> cd C:\python27
			> python -m pip install wheel
Go to this link http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml and then from terminal,
			> python -m pip install lxml-3.6.4-cp27-cp27m-win32.whl

- Install PSYCOPG2 from http://www.stickpeople.com/projects/python/win-psycopg/

- Install nodejs
	Go to https://nodejs.org/en/

> cd C:\Program Files\nodejs (here you specify installation location nosejs)
> npm install -g less less-plugin-clean-css

Install wkhtmltopdf from here https://wkhtmltopdf.org/downloads.html (I prefer using version 12.1)

12.Now we need to create a service with pycharm.

For this, open pycharm and under the run menu, go to edit configurations option and click on the ‘+’ to create a new configuration, select python from the list. Now we need to select script and script parameters. In the script field, select the odoo-bin file.

In the script parameters section fill it like this, -c /path to odoo.conf file, i.e., for example, -c /home/odoo/odoo-10.0/odoo.conf.

Now we can run Odoo from pycharm.
