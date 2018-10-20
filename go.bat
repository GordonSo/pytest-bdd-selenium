python -m venv venv
call .\venv\Scripts\activate.bat
pip install -r requirements.txt --disable-pip-version-check
pytest "tests"
pause