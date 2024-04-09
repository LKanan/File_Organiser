from PyQt5.QtWidgets import QApplication, QMessageBox

# Création d'une instance d'application PyQt
app = QApplication([])
message_box = QMessageBox()


def create_popup(time=0):
    message_box.setWindowTitle("Rapport")
    message_box.setText(f"Réorganisation des fichiers réussie avec succès.\n {time} sec.")
    message_box.setIcon(QMessageBox.Information)
    # On affiche la fenetre du popup
    message_box.exec_()

create_popup()