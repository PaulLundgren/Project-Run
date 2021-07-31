import sys
from cx_Freeze import setup, Executable

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
base = None
if sys.platform == "win32":
    base = "Win32GUI"
if sys.platform == "win64":
    base = "Win64GUI"

setup(
    name='ProjectRun',
    version='0.5.0',
    description='2D side scroller written in python with pygame',
    author='Paul Lundgren, Conner Gallimore, Martin Lasprilla, Lunafreya Nguyen',
    url='https://github.com/PaulLundgren/Project-Run',
    packages=['GameFiles'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'start_ProjectRun=GameFiles.ProjectRun:main',
        ],
    },
    install_requires=[
        'pygame~=2.0.1',
        'cx-Freeze~=6.7',
    ],
    include_package_data=True,
    executables=[Executable("GameFiles/ProjectRun.py",
                            base=base,
                            targetName="ProjectRun.exe",
                            shortcutName="ProjectRun",
                            shortcutDir="DesktopFolder",
                            icon="GameFiles/Images/icon.ico")]
)