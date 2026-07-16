# SAVE YOUR PC 💻😎

A simple Python backup utility designed to quickly save important personal files and application data to an external drive or secondary storage location.

## ✨ Features

* Backup OBS Studio profiles, scenes, and settings
* Backup Minecraft worlds (`saves`) and screenshots
* Backup Documents folder
* Optional backup of Downloads folder
* Backup Pictures folder
* Backup Videos folder

* Interactive terminal interface using Rich
* Automatic validation of directories before copying
* Existing backup folder detection with overwrite confirmation

## What Gets Backed Up

### OBS Studio

```
%AppData%/obs-studio/basic
```

### Minecraft

```
%AppData%/.minecraft/saves
%AppData%/.minecraft/screenshots
```

### Windows User Folders

```
Documents
Downloads (optional)
Pictures
Videos
```

## 🚩 Requirements

* Python 3.8+
* Windows
* Rich 

Install dependencies:

```bash
pip install rich
```

## 🤔 How to use

Run the script:

```bash
python main.py
```

Or Run the Executable!

Enter the destination drive when prompted:

```text
D:/
```

or simply:

```text
D
```

The program will automatically create:

```text
D:/
└── PC SAVED/
    ├── obs studio/
    ├── minecraft/
    │   ├── saves/
    │   └── screenshots/
    ├── Documents/
    ├── Downloads/
    ├── Pictures/
    └── Videos/
```

## 🤔 How It Works

1. The script asks for a destination drive.
2. It verifies that the drive exists.
3. A folder named `PC SAVED` is created.
4. Important files and application data are copied.
5. If a previous backup exists, the user can choose whether to overwrite it.

## ❓ Why I Built This

After losing important Minecraft saves and getting tired of manually browsing through multiple folders every time I wanted to create a backup, I decided to automate the process.

This tool allows me to back up the files I care about most with just a few clicks.

## ‼️ Disclaimer

This project was created for personal use and currently supports standard Windows folder locations. If your folders or applications are installed in custom locations, modifications may be required.
