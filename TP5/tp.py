import numpy as np
from PIL import Image
import os

def lzw_compress(data_str):
    # Créer un dictionnaire initial dictionary de taille 256
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    
    if not data_str:
        return []
        
    result = []
    
    # W <- lire un caractère
    w = data_str[0]
    
    # Tant qu’il reste des caractères à lire faire
    for a in data_str[1:]:
        # a est le nouveau caractère lu (via la boucle for)
        
        # si ( w + a est dans D ) alors
        wa = w + a
        if wa in dictionary:
            # w <- w + a
            w = wa
        else:
            # écrire le code de w
            result.append(dictionary[w])
            
            # ajouter w + a dans D
            dictionary[wa] = dict_size
            dict_size += 1
            
            # w <- a
            w = a
            
    # écrire le code de w (fin de la boucle)
    if w:
        result.append(dictionary[w])
        
    return result

def lzw_decompress(compressed):
    # Initialiser le dictionnaire de base pour la décompression
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    
    if not compressed:
        return ""
        
    result = []
    w = chr(compressed[0])
    result.append(w)
    
    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            # Cas spécial dans LZW : ex quand on encode ABABA et le code de ABA est juste ajouté
            entry = w + w[0]
        else:
            raise ValueError('Mauvais code compressé : %s' % k)
            
        result.append(entry)
        
        # ajouter w + le premier caractère de la nouvelle entrée dans D
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        
        w = entry
        
    return "".join(result)

def test_sequence_lzw():
    sequence = "ABABABA"
    print(f"--- Test de la compression sur la séquence : '{sequence}' ---")
    
    # Générer le code
    code = lzw_compress(sequence)
    print(f"1. Code associé à la séquence : {code}")
    
    # Calculer le taux de compression
    taille_initiale = len(sequence)
    taille_compressee = len(code)
    
    print(f"2. Longueur initiale : {taille_initiale}")
    print(f"   Longueur compressée (en codes) : {taille_compressee}")
    
    # Taux de compression de base (longueur init / longueur comp)
    ratio = taille_initiale / taille_compressee
    gain = (1 - (taille_compressee / taille_initiale)) * 100
    
    print(f"   Taux de compression (Ratio) : {ratio:.2f}")
    print(f"   Gain d'espace : {gain:.2f}%\n")
    
    # Optionnel: Décompression
    decompressed = lzw_decompress(code)
    print(f"   [Optionnel] Décompression : {decompressed}")
    print(f"   Vérification : {'Valide' if sequence == decompressed else 'Erreur'}\n")

def test_image_lzw():
    print("--- Test de la compression sur une image ---")
    
    # Recherche d'une image dans le dossier, ou création d'une image de test
    image_paths = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    
    if image_paths:
        image_path = image_paths[0]
        print(f"Image trouvée : {image_path}")
        # Lire en niveau de gris ('L')
        img = Image.open(image_path).convert('L')
    else:
        print("Aucune image trouvée. Création d'une image de test locale (50x50)...")
        img_array = np.zeros((50, 50), dtype=np.uint8)
        # Création de zones uniformes pour faciliter la compression
        img_array[:, :25] = 100
        img_array[:, 25:] = 200
        img = Image.fromarray(img_array)
        img.save("test_lzw.png")
        img = Image.open("test_lzw.png").convert('L')
        print("Image synthétique 'test_lzw.png' générée.")
        
    # Transformation de l'image en vecteur puis en suite de caractères
    data = np.array(img).flatten()
    data_str = ''.join([chr(p) for p in data])
    
    print(f"Image transformée en suite de {len(data_str)} caractères.")
    
    # Appliquer la compression LZW
    compressed_img = lzw_compress(data_str)
    print(f"Nombre de codes après compression : {len(compressed_img)}")
    
    gain_img = (1 - (len(compressed_img) / len(data_str))) * 100
    print(f"Gain de compression sur l'image : {gain_img:.2f}%")
    
    # Vérification optionnelle
    print("\nVérification avec décompression de l'image...")
    decompressed_str = lzw_decompress(compressed_img)
    if decompressed_str == data_str:
        print("Super ! La décompression restitue exactement les pixels de départ.")
    else:
        print("Erreur : la décompression ne correspond pas à l'original.")
        

if __name__ == "__main__":
    test_sequence_lzw()
    test_image_lzw()
