import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ProjectRun',
    version='0.5.0',
    description='2D side scroller written in python with pygame',
    author='Paul Lundgren, Conner Gallimore, Martin Lasprilla, Lunafreya Nguyen',
    url='https://github.com/PaulLundgren/Project-Run',
    packages=['GameFiles',],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'start_ProjectRun=GameFiles.ProjectRun:main',
        ],
    },
    install_requires=[
        'pygame~=2.0.1'
    ],
    include_package_data=True
)
