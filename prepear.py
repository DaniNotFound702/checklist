def main():
    with open("/home/owhat/.config/hypr/hyprland.conf", "a") as f:
        f.write("exec=/bin/bash /home/owhat/checklist/start.sh")