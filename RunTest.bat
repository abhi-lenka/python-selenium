set PYTHONPATH=%PYTHONPATH%;%cd%;
cd drivers
set PATH=%PATH%;%cd%;
cd ..
call python --version
call pip install -r requirements.txt
call allure generate --clean allure-result
call pytest