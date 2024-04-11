# from MediaAutomationScripts import VerifyVideo

def call_verifier(file_path):
    print("HELLO")
    print(file_path)
    import subprocess
    python_interpreter = 'python'
    script_path = './MediaAutomationScripts/VerifyVideo.py'
    subprocess.run([python_interpreter, script_path, '-f', file_path])

def check_for_ffmpeg_binaries():
    pass