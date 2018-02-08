from setuptools import setup

setup(
    name="terminal_velocity",
    version="0.3.01",
    author="Sean Hammond, Vincent Perricone",
    packages=["terminal_velocity"],
    scripts=["bin/terminal_velocity"],
    url="http://vhp.github.com/terminal_velocity/",
    license="GNU General Public License, Version 3",
    description="A fast note-taking app for the UNIX terminal",
    long_description=open("README.md").read(),
    install_requires=[
        "urwid",
        "chardet",
        ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        ],
)
