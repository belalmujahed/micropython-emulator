
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'micropython-emulator'
AUTHOR = 'Belal Mujahed'
AUTHOR_EMAIL = 'belal.mujahed@gmail.ccom'
URL = 'https://github.com/belalmujahed/micropython-emulator'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'A package to enable test driven development for micropython'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = []

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      py_modules=['network', 'esp'],
      setup_requires=[
            "flake8",
            "black"
      ]
      )