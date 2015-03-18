## Setup the development environment ##

Here you will find the basic instructions for coding Vikuit. We use Eclipse with PyDev like development environment. But, of course, you can use your favourite Python ide.

For this tutorial we asume you have basic python  and eclipse knowledge.

### Tools, code and libraries: ###

  1. Download and install Phython 2.5.2. This is the version that runs on the Google App Engine and should therefore be used. http://www.python.org/download/releases/2.5.2/

> 2. Download the Python version of the Google App Engine from Download Site for the GAE

> 3. Install PyDev via the Eclipse update manager via the following update site. http://pydev.org/updates

> 4. As code repository we use Mercurial. You can install the mercurial plugin for eclipse from the following update site: http://cbes.javaforge.com/update

> 5. Checkout the code form this site, ` hg clone https://vikuit.googlecode.com/hg/ vikuit `

### Configure Eclipse ###

After we checkout the source, we only need some few steps for setting up the project within eclipse:

  1. We need to add the GAE SDK to the pythonpath. Right click your project and select properties. Select PYTHONPATH and press "Add source folder" in the "External Source Folder". Select the installation directory of the GAE SDK.

> 2. Also we need to add the follow libraries: lib/django, lib/webob and lib/yaml

### Launch the server ###

For run the application easy, we need do the follow configuration:

You still can use the command line to run your GAE application. But we are now going to configure Eclipse to allow you to run your application directly from Eclipse.

  1. Right click on "controller.py", select Run As -> Run Configuration. Under Main Module maintain the path to dev\_appserver.py

> 2. On the "Arguments" Tab, "Program arguments" write the follow : "${project\_loc}"

**Important notes**

The default login / password for admin is :
user: admin
password: 1234

### Other information ###

At this URL you will find all you need: http://www.vogella.de/articles/GoogleAppEngine/article.html