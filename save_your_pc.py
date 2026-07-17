import os
import time 
import shutil

username = os.getenv("USERNAME")

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.theme import Theme

themes = Theme({"error": "red bold", "success": "green", "warning": "yellow bold"})

console = Console(theme=themes)

obs_path = f"C:/Users/{username}/AppData/Roaming/obs-studio/basic"
mc_path = f"C:/Users/{username}/AppData/Roaming/.minecraft"

doc_path = f"C:/Users/{username}/Documents"
pic_path = f"C:/Users/{username}/Pictures"
video_path = f"C:/Users/{username}/Videos"


def save_pc(disk):
    os.system('cls')
    final_path = f"{disk}/PC SAVED"

    if os.path.exists(f"{disk}/PC SAVED"):
        console.print("[warning][!][/warning] The backup destination folder already exists!")
        confirmation = Confirm.ask("[yellow][?][/yellow] Continue?")

        if confirmation:
            console.print("[warning][!][/warning] Deleting existing backup folder...")
            shutil.rmtree(f"{disk}/PC SAVED")
            os.makedirs(f"{disk}/PC SAVED")

            backup(
                obs_path,
                final_path,
                "Obs Studio"
            )
            backup(
                mc_path,
                final_path,
                f"Minecraft"
            )
            save_download(final_path)
            backup(
                doc_path,
                final_path,
                f"Documents"
            )
            backup(
                pic_path,
                final_path,
                f"Pictures"
            )
            backup(
                video_path,
                final_path,
                f"Videos"
            )

        else:
            console.print("[warning][!][/warning] Script aborted by the user!")
            time.sleep(3)
            return
    else:
        os.makedirs(f"{disk}/PC SAVED")
        console.print("[success][+][/success] Directory created successfully!")
        time.sleep(3)

        backup(
            obs_path,
            final_path,
            "Obs Studio"
        )
        backup(
            mc_path,
            final_path,
            f"Minecraft"
        )
        save_download(final_path)
        backup(
            doc_path,
            final_path,
            f"Documents"
        )
        backup(
            pic_path,
            final_path,
            f"Pictures"
        )
        backup(
            video_path,
            final_path,
            f"Videos"
        )

def backup(app_path, final_path, name):
    # save_path = diretorio do save
    # final_save = onde vai salvar
    # name = nome do que vai ser salvo
    console.print("")
    if not os.path.exists(app_path):
        console.print(f"[error][-][/error] The directory {app_path} does not exist or is not located in the default path!")
        time.sleep(3)
        return False
    else:
        console.print(f"[success][+][/success] Directory {app_path} found. Copying files...")

        try:
            shutil.copytree(app_path, f"{final_path}/{name}")
            console.print(f"[success][+][/success] The {name} backup was completed successfully!")
            time.sleep(3)
            return True
        except Exception as err:
            console.print(f"[error][-][/error] Failed to back up {name}: {err}")
            time.sleep(3)
            return False

def save_download(final_path):
    console.print("")
    # DOWNLOADS 
    download_path = f"C:/Users/{username}/Downloads"

    if not os.path.exists(download_path):
        console.print(f"[error][-][/error] The directory {download_path} does not exist or is not located in the default path!")
        time.sleep(3)
    else:
        console.print(f"[success][+][/success] Directory {download_path} found. Copying files...")
        confirm_backup = Confirm.ask(f"[yellow][?][/yellow] Do you want to copy the folder {download_path}?")

        if confirm_backup:
            try:
                shutil.copytree(download_path, f"{final_path}/Downloads")
                console.print("[success][+][/success] The Downloads backup was completed successfully!")
                time.sleep(3)
            except Exception as err:
                console.print(f"[error][-][/error] Failed to back up: {err}")
                time.sleep(5)


if __name__ == "__main__":
    while True:
        os.system('cls')
        disk = Prompt.ask("[yellow][?][/yellow] Enter the drive letter for the backup (e.g., D:/)")

        disk = disk.strip()

        if len(disk) == 1:
            disk += ":/"
        
        if disk.endswith(":"):
            disk += "/"

        if not os.path.exists(f"{disk}"):
            console.print("[error][-][/error] The drive you entered does not exist!")
            time.sleep(3)
            continue
        else:
            console.print(f"[success][+][/success] Drive: ( {disk} ) was found!")
            save_pc(disk)
            break
