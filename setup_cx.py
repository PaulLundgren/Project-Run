import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pygame", "GameFiles"], "excludes": ["tkinter"]}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name='ProjectRun',
    version='1.0.0',
    description='2D side scroller written in python with pygame',
    author='Paul Lundgren, Conner Gallimore, Martin Lasprilla',
    url='https://github.com/PaulLundgren/Project-Run',
    options={"build_exe": build_exe_options},
    executables=[Executable("GameFiles/ProjectRun.py",
                            base=base,
                            targetName="ProjectRun.exe",
                            shortcutName="ProjectRun",
                            shortcutDir="DesktopFolder",
                            icon="GameFiles/Images/icon.ico")]
)