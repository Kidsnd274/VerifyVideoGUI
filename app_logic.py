# from MediaAutomationScripts import VerifyVideo

def call_verifier(file_path):
    import subprocess
    python_interpreter = 'python'
    script_path = './MediaAutomationScripts/VerifyVideo.py'
    creation_flag = subprocess.CREATE_NEW_CONSOLE
    subprocess.run([python_interpreter, script_path, '-f', file_path], creationflags=creation_flag)

def check_for_ffmpeg_binaries():
    pass