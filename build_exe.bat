call .\venv\Scripts\activate.bat
pyinstaller --noconfirm --onedir --windowed --add-data "./MediaAutomationScripts;MediaAutomationScripts/" --add-data "./venv/Lib/site-packages/customtkinter;customtkinter/" --name VerifyVideoGUI main.py
copy .\etc\readme.txt .\dist\VerifyVideoGUI