import json
# Ouvrir le fichier JSON en mode lecture
with open('/content/Untitled Folder/sampleJson (1).json', 'r') as fichier:
    # Lire le contenu du fichier et le charge en tant qu'objet Python
    r_fichier = json.load(fichier)
# Afficher le contenu du fichier JSON
print(r_fichier)
