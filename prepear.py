import os
import shutil
def main():
    with open("/home/daniel/.config/hypr/hyprland.conf", "a") as f:
        shutil.move("/home/Owhat/)
        f.write("exec=/bin/python3 /home/daniel/.config/hypr/save.py")