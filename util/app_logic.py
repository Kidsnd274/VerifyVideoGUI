import threading
import os
import sys
import subprocess

def call_verifier(optionsObject, callbackFunction):
    thread = threading.Thread(target=start_subprocess, args=(optionsObject, callbackFunction, ), daemon=True)
    thread.start()
    
def start_subprocess(optionsObject, callbackFunction):
    file_path = optionsObject.folder_path
    skip_ffmpeg = optionsObject.skip_ffmpeg
    filter_suffix = optionsObject.filter_staxrip_suffix
    
    # Check if we are running as a bundled application
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    else:
        # Otherwise, we are running in a normal Python environment
        application_path = '.'

    # Adjust the script path according to the environment
    script_path = os.path.join(application_path, 'MediaAutomationScripts', 'VerifyVideo.py')
    
    python_interpreter = 'python'
    creation_flag = subprocess.CREATE_NEW_CONSOLE
    args = [
        python_interpreter,
        script_path,
        '-f',
        file_path
    ]
    if skip_ffmpeg:
        args.append('-if')
    if filter_suffix:
        args.append('-s')

    subprocess.run(args, creationflags=creation_flag)
    callbackFunction()

def check_for_ffmpeg_binaries():
    pass