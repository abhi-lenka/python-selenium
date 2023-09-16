set PYTHONPATH=%PYTHONPATH%;%cd%;
cd drivers
set PATH=%PATH%;%cd%;
cd ..
call python --version
call pip install -r requirements.txt
call pytest