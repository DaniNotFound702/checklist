def main():
    with open("/home/owhat/.config/hypr/hyprland.conf", "a") as f:
        f.write("exec=/home/owhat/checklist/.venv/bin/python3 /home/owhat/checklist/save.py")