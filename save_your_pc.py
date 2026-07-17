import os
import time 
import shutil

username = os.getenv("USERNAME")

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.theme import Theme

themes = Theme({"error": "red bold", "success": "green", "warning": "yellow bold"})

console = Console(theme=themes)

def save_pc(disk):
    os.system('cls')
    final_path = f"{disk}/PC SAVED"

    if os.path.exists(f"{disk}/PC SAVED"):
        console.print("[warning][!][/warning] A pasta de backups final ja existe!")
        confirmation = Confirm.ask("[yellow][?][/yellow] Deseja continuar?")

        if confirmation:
            console.print("[warning][!][/warning] Pasta antiga sendo deletada")
            shutil.rmtree(f"{disk}/PC SAVED")
            os.makedirs(f"{disk}/PC SAVED")

            save_obs(final_path)
            save_mc(final_path)
            save_files(final_path)

        else:
            console.print("[warning][!][/warning] Script foi abortado pelo usuario!")
            time.sleep(3)
            return
    else:
        os.makedirs(f"{disk}/PC SAVED")
        console.print("[success][+][/success] Diretorio criado com sucesso")
        time.sleep(3)

        save_obs(final_path)
        save_mc(final_path)
        save_files(final_path)

def save_obs(final_path):
    # OBS THEMES, PROFILES
    console.print("")
    obs_path = f"C:/Users/{username}/AppData/Roaming/obs-studio/basic"

    if not os.path.exists(obs_path):
        console.print(f"[error][-][/error] O diretorio {obs_path} nao existe ou nao esta na pasta padrao!")
        time.sleep(3)
        return
    else:
        console.print(f"[success][+][/success] Diretorio {obs_path} foi encontrado. Copiando arquivos")
        time.sleep(3)

        try:
            shutil.copytree(obs_path, f"{final_path}/obs studio")
            console.print("[success][+][/success] O backup do OBS foi realizado com sucesso!")
            time.sleep(5)

        except Exception as e:
            console.print(f"[error][-][/error] Ocorreu um erro ao realizar o backup: {e}")
            time.sleep(5)

def save_mc(final_path):
    # MC FILES
    console.print("")
    mc_path = f"C:/Users/{username}/AppData/Roaming/.minecraft"

    if not os.path.exists(mc_path):
        console.print("[error][-][/error] O diretorio de saves/screenshots nao existe!")
        time.sleep(3)
        return
    else:
        console.print(f"[success][+][/success] Diretorio {mc_path} foi encontrado. Copiando arquivos")
        time.sleep(3)

        try:
            shutil.copytree(f"{mc_path}/saves", f"{final_path}/minecraft/saves")
            shutil.copytree(f"{mc_path}/screenshots", f"{final_path}/minecraft/screenshots")
            
            console.print("[success][+][/success] O backup dos SAVES e SCREENSHOTS de MINECRAFT foi realizado com sucesso!")
            time.sleep(5)

        except Exception as err:
            console.print(f"[error][-][/error] Ocorreu um erro ao realizar o backup: {err}")
            time.sleep(5)

def save_files(final_path):
    # DOCUMENTS
    console.print("")
    doc_path = f"C:/Users/{username}/Documents"

    if not os.path.exists(doc_path):
        console.print(f"[error][-][/error] O diretorio {doc_path} nao existe ou nao esta na pasta padrao!")
        time.sleep(3)
    else:
        console.print(f"[success][+][/success] Diretorio {doc_path} foi encontrado. Copiando arquivos")
        time.sleep(3)

        try:
            shutil.copytree(doc_path, f"{final_path}/Documents")
            console.print("[success][+][/success] O backup de documentos foi realizado com sucesso!")
            time.sleep(3)

        except Exception as err:
            console.print(f"[error][-][/error] Ocorreu um erro ao realizar o backup: {err}")
            time.sleep(5)

    # DOWNLOADS 
    download_path = f"C:/Users/{username}/Downloads"

    if not os.path.exists(download_path):
        console.print(f"[error][-][/error] O diretorio {download_path} nao existe ou nao esta na pasta padrao!")
        time.sleep(3)
    else:
        console.print(f"[success][+][/success] Diretorio {download_path} foi encontrado.")
        confirm_backup = Confirm.ask(f"[yellow][?][/yellow] Deseja copiar a pasta {download_path}?")

        if confirm_backup:
            try:
                shutil.copytree(download_path, f"{final_path}/Downloads")
                console.print("[success][+][/success] O backup de Downloads foi realizado com sucesso!")
                time.sleep(3)
            except Exception as err:
                console.print(f"[error][-][/error] Ocorreu um erro ao realizar o backup: {err}")
                time.sleep(5)

    # PICTUES 
    pic_path = f"C:/Users/{username}/Pictures"

    if not os.path.exists(pic_path):
        console.print(f"[error][-][/error] O diretorio {pic_path} nao existe!")
        time.sleep(5)
    else:
        console.print(f"[success][+][/success] O Diretorio {pic_path} foi encontrado. Iniciando backup!")

        try:
            shutil.copytree(pic_path, f"{final_path}/Pictures")
            console.print("[success][+][/success] O backup de Pictures foi realizado com sucesso!")
            time.sleep(3)
        except Exception as err:
            console.print(f"[error][-][/error] Ocorreu um erro ao realizar o backup: {err}")    
            time.sleep(5)

    # VIDEOS
    video_path = f"C:/Users/{username}/Videos"

    if not os.path.exists(video_path):
        console.print(f"[error][-][/error] O diretorio {video_path} nao existe!")
        time.sleep(5)
    else:
        console.print(f"[success][+][/success] O Diretorio {video_path} foi encontrado. Iniciando backup!")

        try:
            shutil.copytree(video_path, f"{final_path}/Videos")
            console.print("[success][+][/success] O backup de Videos foi realizado com sucesso!")
            time.sleep(3)
        except Exception as err:
            console.print(f"[error][-][/error] Ocorreu um erro ao realizar o backup: {err}")    
            time.sleep(5)


if __name__ == "__main__":
    while True:
        os.system('cls')
        disk = Prompt.ask("[yellow][?][/yellow] Digite o nome do disco para backup EX: D:/")

        disk = disk.strip()

        if len(disk) == 1:
            disk += ":/"
        
        if disk.endswith(":"):
            disk += "/"

        if not os.path.exists(f"{disk}"):
            console.print("[error][-][/error] O disco digitado nao existe!")
            time.sleep(3)
            continue
        else:
            console.print(f"[success][+][/success] Disco {disk} foi encontrado!")
            save_pc(disk)
            break
