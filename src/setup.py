from distutils.core import setup
import py2exe


options = {#'build': {'build_base': '.\src'},
           'py2exe': {
             'compressed': 0,
             #'bundle_files': 1,
             'dist_dir': 'dist'
             #'includes': 'src/ConfigReader'
           }}

prog1 = dict(script="CLI.py",
             # icon_resources=[(1,"tater.png")],
             author="Brett Nelson",
             author_email="brett@brettnelson.org",
             version="1.0.0")

prog2 = dict(script="GUI.py",
             icon_resources=[(1,"../resources/potato.ico")],
             author="Brett Nelson",
             author_email="brett@brettnelson.org",
             version="1.0.0")

setup(console=[prog1],
      windows=[prog2],
      options=options)
