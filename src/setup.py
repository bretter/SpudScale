from distutils.core import setup
import py2exe


options = {
           'py2exe': {
             'compressed': 0,
             'dist_dir': '../dist'
           }}

prog1 = dict(script="CLI.py",
             author="Brett Nelson",
             author_email="brett@brettnelson.org",
             version="1.0.0")

prog2 = dict(script="GUI.py",
             icon_resources=[(1, "../resources/potato.ico")],
             author="Brett Nelson",
             author_email="brett@brettnelson.org",
             version="1.0.0")

setup(console=[prog1],
      windows=[prog2],
      options=options)
