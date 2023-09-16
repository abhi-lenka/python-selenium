set PYTHONPATH=%PYTHONPATH%;%cd%;
call python --version
call pip install -r requirements.txt
call pytest