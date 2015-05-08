from distutils.core import setup
import py2exe

py2exe = dict(compressed=1)

options = dict(py2exe=py2exe)

prog1 = dict(script="CLI.py",
             # icon_resources=[(1,"tater.png")],
             author="Brett Nelson",
             author_email="brett@brettnelson.org",
             version="1.0.0")

prog2 = dict(script="GUI.py",
             # icon_resources=[(1,"potato.png")],
             author="Brett Nelson",
             author_email="brett@brettnelson.org",
             version="1.0.0")

setup(console=[prog1],
      windows=[prog2],
      options=options)
