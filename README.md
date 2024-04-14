![image](https://github.com/Kidsnd274/VerifyVideoGUI/assets/1343896/e743a1b1-e1ce-4168-abf5-d05a65cf9ec9)

Make sure you have ffmpeg in PATH or the MediaAutomationScripts folder
## Development
To clone the repo, run the following command as this repo uses git submodules
```
git clone --recurse-submodules https://github.com/Kidsnd274/VerifyVideoGUI
```
or if you have already cloned the repo, run the following commands in the repo directory
```
git submodule init 
git submodule update
```
To create the Python virtual environment, run the following command:
```
python -m venv venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
```
Once you're in the virtual environment, to run the program just use this command:
```
python main.py
```
