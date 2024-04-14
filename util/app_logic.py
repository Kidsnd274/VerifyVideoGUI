from util.verify_options_object import VerifyOptionsObject

def call_verifier(optionsObject):
    file_path = optionsObject.folder_path
    skip_ffmpeg = optionsObject.skip_ffmpeg
    filter_suffix = optionsObject.filter_staxrip_suffix
    
    import subprocess
    python_interpreter = 'python'
    script_path = './MediaAutomationScripts/VerifyVideo.py'
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

def check_for_ffmpeg_binaries():
    pass