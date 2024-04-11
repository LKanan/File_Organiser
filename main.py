from pathlib import Path
import os
import popup_gui
from PyQt5.QtWidgets import QMessageBox
import time

"""
 On crée un objet path qui représente le chemin du dossier courant(Le chemin du dossier où se trouve notre fichier du 
 programme et dans lequel il est executé) et maintenant.
 La methode cwd() permet de recuperer le chemin du repertoire courant et la methode resolve() appliquée à l'objet path
 permet de recuperer la chaine de caractère du chemin courant que représente l'objet.
"""

path = Path.cwd()
# path = Path("/home/l_kanan/Bureau")
start_time = time.time()
attention_popup = popup_gui.attention_popup(path.name)
numer_of_files = 0
number_of_folders = 0

file_extensions = {
    "Text files": [".txt", ".rtf", ".doc", ".docx", ".odt", ".md", ".pages"],
    "Image files": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".svg", ".ico", ".heic"],
    "Audio files": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".aiff", ".m4a", ".wma", ".opus", ".aiff", ".alac"],
    "Video files": [".mp4", ".mov", ".avi", ".wmv", ".flv", ".mkv", ".mpeg", ".webm", ".3gp", ".mpg", ".m4v"],
    "Zipped files": [".zip", ".rar", ".7z", ".gz", ".tar"],
    "Executable files": [".exe", ".bat", ".com", ".sh"],
    "Web files": [".html", ".htm", ".css"],
    "Data files": [".csv", ".tsv", ".json", ".xml", ".db"],
    "Presentation files": [".ppt", ".pptx", ".pps", ".odp"],
    "Spreadsheet files": [".xls", ".xlsx", ".ods"],
    "Document files": [".pdf"],
    "Source code files": [".py", ".java", ".js", ".c", ".cpp", ".js", ".php"],
    "Adobe Photoshop files": [".psd"],
    "Adobe Illustrator files": [".ai"],
    "Adobe InDesign files": [".indd"],
    "Numérics books": [".epub"],
    "Kindle files": [".mobi"],
    "torrent files": [".torrent"],
    "ISO files": [".iso"],
    "Initialisation files": [".ini"],
    "Vcard files": [".vcf"],
    "Binary files": [".dat"],
    "ICalendar files": [".ics"],
    "E-mail files": [".eml"],
    "Excel Macro": [".xlsm"],
}

"""
Cette boucle représente le coeur meme de ce programme, on fait une iteration sur le dossier représenté par le chemin 
absolu dans la variable path 
La methode iterdir() permet de faire une iteration sur les fichiers contenus dans un dossier représenté par le chemin 
dans l'objet path
"""

if attention_popup == QMessageBox.Ok:
    start_time = time.time()
    for file in path.iterdir():
        """
        La methode items() appliquée sur un dictonnaire permet de faire une iteration double, dans ce cas on recupere la
        clé et la valeur au meme moment d'une iteration
        """
        for file_type, extensions in file_extensions.items():
            for extension in extensions:
                """
                La methode suffix() sur un objet Path permet de recuperer l'extension du fichier représenter dans le
                chemin contenu dans l'objet Path
                """
                if file.suffix.lower() == extension:
                    numer_of_files += 1
                    # print(file_type)
                    """
                    Création d'un dossier, on definit le nouveau dossier par son chemin complet en combinant un chemin
                    dans un objet Path et le nouveau nom du dossier et pour ce cas le nom de dossier c'est la cle
                    file_type
                    """
                    directory = path / file_type
                    """
                    La methode mkdir() permet de creer un dossier, son attribut exist_ok permet d'eviter ou non de generer
                    une erreur lorsque l'on veut creer un dossier qui existe deja et il prend une valeur booleenne par
                    defaut il a la valeur False si on ne le precise pas et si on lui donne la valeur True on ne va plus
                    generer une erreur mais on ne va simplement pas creer un dossier qui existe deja et s'il n'existe pas
                    on va le creer
                    """
                    if not directory.exists():
                        number_of_folders += 1
                    directory.mkdir(exist_ok=True)
                    """
                    La variable d'instance name appliquée sur l'objet Path renvoi une chaine de caractere correspondant au
                    nom+l'extension du fichier
                    """
                    if (directory / file.name).exists():
                        replacement_popup = popup_gui.replacement_popup(file.name, directory.name)
                        if replacement_popup == QMessageBox.Yes:
                            os.replace((path / file).resolve(), (directory / file.name).resolve())
                        elif replacement_popup == QMessageBox.No:
                            numer_of_files -= 1
                            continue
                    else:
                        file.rename(directory / file.name)
                    break
    end_time = time.time()
    popup_gui.rapport_popup(round((end_time - start_time), 3), number_of_folders, numer_of_files)
elif attention_popup == QMessageBox.Cancel:
    popup_gui.contact_popup()
# create_files()
# for content in path.iterdir():
#     print(content.suffix)

# Recuperation du chemin du contenu de l'objet sous forme d'une chaine de cractere
# print(str(path.resolve()))


# fichier = path / 'exemplaire.txt'

# La methode touch() permet de créer un fichier, on l'execute sur une variable contenant l'objet path suivi du nom du
# fichier a créer
# fichier.touch()
# On peut afficher le chemin du dossier courant
# print(Path.cwd().resolve())
# extension = input("entrez une extension ")
# for k, v in extensions.items():
#     for i in v:
# La methode suffix() sur un objet Path permet de recuperer l'extension du fichier représenter dans le chemin contenu
# dans l'objet Path
#         if i == path.suffix:
#             print(f"Type: {k}")
#             break

# Creation d'un dossier
# Pour creer un dossier il faut d'abord creer un objet Path qui contient le chemin absolu du nouveau dossier àcreer
# path = Path("/home/l_kanan/Bureau/exemplaire")
# La methode mkdir() permet de creer un dossier, son attribut exist_ok permet 'eviter ou non de generer une erreur
# lorsque l'on veut creer un dossier qui existe deja et il prend une valeur booleenne par defaut il a la valeur False
# si on ne le precise pas et si on lui donne la valeur True on ne va plus generer une erreur mais on ne va simplement
# pas creer un dossier qui existe deja et s'il n'existe pas on va le creer
# path.mkdir(exist_ok=True)

# Couper un fichier
# destination_folder = Path("/home/l_kanan/Bureau")
# La variable dùinstance name appliquée sur l'objet Path renvoi une chaine de caractere correspondant au nom+l'extension
# du fichier
# new_path = destination_folder / path.name
# path.rename(new_path)
# print(list(extensions.values()))
# for l in list(extensions.values()):
#     print(l)
