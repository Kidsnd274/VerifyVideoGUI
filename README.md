## Development
To clone the repo, run the following command as this repo uses git submodules
```
`git clone --recurse-submodules https://github.com/Kidsnd274/VerifyVideoGUI`
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