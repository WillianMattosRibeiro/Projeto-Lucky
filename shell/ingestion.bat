::- Executa um script python com argumentos -::
@echo off
color 0a
mode 60,15

python "C:\Users\BlueShift 017\Documents\Projeto-Lucky\source\ingestion.py" %*

color 07
mode 100,25
@echo on