# Practice exercises for PyGame

## Repository
https://github.com/StefMcCuistion/PyGame-Practice-Exercises.git

## Description
This is where I'll be keeping all my practice projects for learning PyGame! I'm starting on 12/27/2024 with the ClearCode 'Ultimate Introduction to Pygame' tutorial. 

## Resources
### Tutorials used:
https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=2038s
https://www.youtube.com/watch?v=8OMghdHP-zs&pp=ygUQY2xlYXJjb2RlIHB5Z2FtZQ%3D%3D

## Notes
### Virtual Environments
Virtual Environments will keep you from installing dependencies and packages globally.
There are many tools you can use like ``pipx`` and ``poetry`` to assist with this, but for an out-of-the-box solution ``venv`` comes with Python.
The command ``python -m venv .venv`` will create a virtual environment in the ``.venv`` folder. (Do this at the root)
Then the command ``source ./venv/Scripts/Activate`` will activate the environment, and any console commands you enter afterwards will affect the virtual environment.
Such as the command to install requirements from a ``requirements.txt`` file: ``pip install -r requirements.txt``
As a temporary workaround, I'll have '.venv/pyvenv.cfg' read this on my laptop:
```
home = C:\Users\Stef McCuistion\AppData\Local\Programs\Python\Python312
include-system-site-packages = false
version = 3.12.5
executable = C:\Users\Stef McCuistion\AppData\Local\Programs\Python\Python312\python.exe
command = C:\Users\Stef McCuistion\AppData\Local\Programs\Python\Python312\python.exe -m venv C:\Users\Stef McCuistion\Desktop\Gamedev\PyGame-Practice-Exercises\.venv
```
...but this on my PC:
```
home = C:\Users\Stef\AppData\Local\Programs\Python\Python312
include-system-site-packages = false
version = 3.12.0
executable = C:\Users\Stef McCuistion\AppData\Local\Programs\Python\Python312\python.exe
command = C:\Users\Stef McCuistion\AppData\Local\Programs\Python\Python312\python.exe -m venv C:\Users\Stef McCuistion\Desktop\Gamedev\PyGame-Practice-Exercises\.venv
```