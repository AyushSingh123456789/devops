import subprocess

def paste_from_windows_clipboard():
    # Use PowerShell to read the Windows clipboard
    result = subprocess.run(
        ['powershell.exe', '-command', 'Get-Clipboard'],
        capture_output=True, text=True
    )
    # Strip trailing newline that Windows adds
    return result.stdout.rstrip('\r\n')

def copy_to_windows_clipboard(text):
    # Pipe text into clip.exe, which sets the Windows clipboard
    subprocess.run(['clip.exe'], input=text.encode('utf-8'), check=True)

text = paste_from_windows_clipboard()
alt_text = ''
make_uppercase = False
for character in text:
    if make_uppercase:
        alt_text += character.upper()
    else:
        alt_text += character.lower()
    make_uppercase = not make_uppercase

copy_to_windows_clipboard(alt_text)
print(alt_text)