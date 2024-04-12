# File_Workbook

Ceci est un petit script pour classer ou organiser automatiquement les fichiers dans des dossiers avec des noms selon
leurs extensions avec le langage Python.
Ce script doit etre executé dans n'importe quel repertoire sur l'ordinateurgit  ayant des fichiers à organiser.
Avec path = Path.cwd() on recupère directement le chemin vers le repertoire courant, mais vous pouvez changer en
personnalisant le chemin avec la syntaxe custom_path = Path("/chemin/vers/repertoire")

- Pour créer des fichiers test sur le bureau vous pouvez utiliser ce scrip:

```
from pathlib import Path

custom_path = Path("/home/l_kanan/Bureau")

# Fonction pour creer des fichiers aleatoires
def create_files(path):

    # l'argument de Path represente le chemin du dossier dans lequel on va creer les fichiers
    files_name = ["CV.docx",
                  "Rapport_stage.pdf",
                  "Compte_rendu_reunion.odt",
                  "Facture_2023-11-15.pdf",
                  "Contrat_de_travail.docx",
                  "Lettre_de_motivation.pdf",
                  "Cours_histoire.odt",
                  "Recette_gateau_au_chocolat.txt",
                  "Liste_de_courses.txt",
                  "Plan_de_vacances.xlsx",
                  "Photo_vacances_2023.jpg",
                  "Anniversaire_amis.jpeg",
                  "Paysage_montagne.png",
                  "Chat_mignon.gif",
                  "Selfie.bmp",
                  "Repas_delicieux.jpg",
                  "Fleur_exotique.tif",
                  "Aurore_boreale.svg",
                  "Logo_entreprise.ico",
                  "Capture_ecran.png",
                  "Chanson_preferee.mp3",
                  "Playlist_ete.m4a",
                  "Album_de_l_annee.flac",
                  "Musique_relaxante.wav",
                  "Sonnerie_telephone.ogg",
                  "Concert_live.mp3",
                  "Bruit_de_la_nature.aiff",
                  "Podcast_interessant.mp3",
                  "Audio_livre.mp3",
                  "Cours_langue_etrangere.mp3",
                  "Film_prefere.mp4",
                  "Vacances_en_famille.mov",
                  "Tutoriel_informatique.avi",
                  "Serie_televisee.wmv",
                  "Court_metrage.flv",
                  "Video_drole.mkv",
                  "Mariage_amis.mpeg",
                  "Presentation_projet.mp4",
                  "Reunion_travail.webm",
                  "Game_play.mp4",
                  "Telechargement.zip",
                  "CV_anglais.docx",
                  "Budget_mensuel.xlsx",
                  "Logo_entreprise.ai",
                  "Modele_lettre.doc",
                  "Script_python.py",
                  "Code_html.html",
                  "Presentation_PowerPoint.pptx",
                  "Dictionnaire_francais.pdf",
                  "Jeux_video.exe",
                  "CV_2023.docx",
                  "Rapport_stage.pdf",
                  "Lettre_motivation.odt",
                  "Cours_histoire.pptx",
                  "Compte_rendu_reunion.txt",
                  "Liste_courses.csv",
                  "Recette_gateau.rtf",
                  "Budget_mensuel.xlsx",
                  "Contrat_travail.pdf",
                  "Manuel_utilisateur.doc",
                  "Photo_vacances_2023.jpg",
                  "Capture_ecran.png",
                  "Paysage_montagne.jpeg",
                  "Chat_mignon.gif",
                  "Logo_entreprise.bmp",
                  "Diagramme_circulaire.svg",
                  "Tuto_maquillage.ico",
                  "Fond_ecran.tif",
                  "Photo_anniversaire.heic",
                  "Scanner_document.pdf",
                  "Chanson_prefere.mp3",
                  "Album_2022.wav",
                  "Musique_relaxante.flac",
                  "Sonnerie_telephone.ogg",
                  "Compilation_fete.m4a",
                  "Podcast_technologie.aac",
                  "Concert_live.mp3",
                  "Bruit_nature.wav",
                  "Cours_musique.aiff",
                  "Chanson_enfance.mp3",
                  "Film_prefere.mp4",
                  "Serie_tv.mkv",
                  "Tutoriel_informatique.avi",
                  "Vacances_ete.mov",
                  "Court_metrage.flv",
                  "Mariage_amis.wmv",
                  "Video_animaux.webm",
                  "Extrait_film.mpg",
                  "Conference_enregistrement.mp4",
                  "Vlog_voyage.m4v",
                  "Setup_logiciel.exe",
                  "Licence_logiciel.txt",
                  "Crack_logiciel.rar",
                  "Manuel_installation.pdf",
                  "Mise_a_jour_logiciel.zip",
                  "Plugin_logiciel.7z",
                  "Theme_logiciel.tar",
                  "Fichier_configuration.ini",
                  "Code_source.py",
                  "Script_python.js",
                  "Facture_achat.pdf",
                  "E-mail_important.eml",
                  "Piece_jointe.zip",
                  "Calendrier_evenements.ics",
                  "Liste_contacts.vcf",
                  "Favori_navigateur.html",
                  "Historique_navigateur.dat",
                  "Document_scanne.pdf",
                  "Archive_photos.rar",
                  ]
    for name in files_name:
    """Creation d'un fichier dans le dossier que représente le chemin contenu dans l'objet
Cette ligne signifie qu'on veut créer un fichier exemplaire.txt dans le dossier représenté par le chemin dans l'objet
Path"""
        file = path / name
        file.touch()

create_files(custom_path)
```