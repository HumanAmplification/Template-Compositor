import sys, os, urllib2, shutil, string

# To guarantee that we have setuptools
# This approach was appropriated from ez_setup.py:
# http://peak.telecommunity.com/dist/ez_setup.py
version = "0.6c11"
download_base = "http://pypi.python.org/packages/%s/s/setuptools/" % sys.version[:3]
egg_name = "setuptools-%s-py%s.egg" % (version,sys.version[:3])
url = download_base + egg_name
saveto = os.path.join(os.curdir, egg_name)
if os.path.exists(saveto):
    # Remove existing
    os.remove(saveto)
src = urllib2.urlopen(url)
if src:
    dst = open(saveto,"wb")
    egg = None
    if dst:
        data = src.read()
        dst.write(data)
        dst.close()
        egg = os.path.realpath(saveto)
        sys.path.insert(0, egg)
    else:
        print "Unable to open egg file %s" % saveto
    src.close()
    # Bootstrap setuptools
    if egg is not None:
        import setuptools
        setuptools.bootstrap_install_from = egg
    else:
        print "Unable to retrieve egg."
else:
    print "Unable to open URL %s" % url
        
    

from setuptools import setup

PROJECT_NAME = "Compositor"
VERSION = "0.2"

setup(
      name=PROJECT_NAME,
      version=VERSION,
      description="Template renderer!",
      url="https://github.com/HumanAmplification/Template-Compositor",
      packages=[
                "compositor",
                "compositor.app"
                ],
      entry_points = {
          'console_scripts' : [
                'compositor = compositor.app.compositor_app:main'
           ]
      },
      package_data = {
      },
      zip_safe=True,
      install_requires=[
                        "Jinja2"
                        ],
      # Authorship metadata
      author="Mark A Christensen",
      license="CC Attribution 3.0",
      keywords="templating jinja jinja2 christensen"
      
)

# Remove crap from sudo install command
# because no one wants compiler droppings everywhere.
egg_filename = string.replace(string.replace(egg_name,"'","_")," ","_")
if os.path.exists(egg_filename):
    os.remove(egg_filename)
if os.path.exists("dist"):
    shutil.rmtree("dist")
project_filename = string.replace(string.replace(PROJECT_NAME,"'","_")," ","_")
if os.path.exists("%s.egg-info" % project_filename):
    shutil.rmtree("%s.egg-info" % project_filename)
if os.path.exists("build"):
    shutil.rmtree("build")    
    
