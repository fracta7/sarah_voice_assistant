import py2exe
from distutils.core import setup

setup(
    windows=[
        {
            "script": "sarah.py",
            "icon_resources": [(1, "ico.ico")]
        }
    ],
)
