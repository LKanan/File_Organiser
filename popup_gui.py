from PyQt5.QtWidgets import QApplication, QMessageBox

# Création d'une instance d'application PyQt
app = QApplication([])
message_box_attention = QMessageBox()
message_box_rapport = QMessageBox()
message_box_Contact = QMessageBox()
message_box_replacement = QMessageBox()


def attention_popup(folder_name):
    message_box_attention.setWindowTitle("Attention")
    message_box_attention.setText(f"""Vous êtes sur le point de réorganiser les fichiers se trouvant dans "{folder_name}".
Cette action est irreversible. 
Voulez-vous continuer ?

Contact: lucienkanani@gmail.com""")
    message_box_attention.setIcon(QMessageBox.Warning)
    message_box_attention.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
    # On affiche la fenetre du popup
    return message_box_attention.exec_()


def rapport_popup(time, numbers_of_folders, number_of_files):
    message_box_rapport.setWindowTitle("Rapport")
    message_box_rapport.setText(
        f"Réorganisation des fichiers réussie avec succès.\n{numbers_of_folders} dossier(s) créé(s), {number_of_files} fichier(s) organisé(s)\nDurée: {time} sec.\n\nContact: lucienkanani@gmail.com")
    message_box_rapport.setIcon(QMessageBox.Information)
    # On affiche la fenetre du popup
    return message_box_rapport.exec_()


def contact_popup(time=0):
    message_box_Contact.setWindowTitle("Contact")
    message_box_Contact.setText(f"""Email: lucienkanani@gmail.com
LinkedIn: Lucien Kanani
Github: LKanan""")
    message_box_Contact.setIcon(QMessageBox.Information)
    # On affiche la fenetre du popup
    return message_box_Contact.exec_()


def replacement_popup(file_name, folder_name):
    message_box_replacement.setWindowTitle("Attention")
    message_box_replacement.setText(
        f"""Le fichier "{file_name}" existe déjà dans le dossier "{folder_name}".\nVoulez-vous le remplacer ?""")
    message_box_replacement.setIcon(QMessageBox.Warning)
    message_box_replacement.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    # On affiche la fenetre du popup
    return message_box_replacement.exec_()
# attention_popup("Bureau")
