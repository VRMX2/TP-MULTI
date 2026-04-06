import cv2
import numpy as np

def Encode(nom_image, fichier_txt):
    img = cv2.imread(nom_image, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Erreur : {nom_image} introuvable.")
        return None, 0, 0
    
    _, binary_img = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
    height, width = binary_img.shape
    fimage = binary_img.flatten() 
    
    malist = []
    if len(fimage) > 0:
        val_actuelle = fimage[0]
        compteur = 1
        for i in range(1, len(fimage)):
            if fimage[i] == val_actuelle and compteur < 127:
                compteur += 1
            else:
                malist.append((compteur, val_actuelle))
                val_actuelle = fimage[i]
                compteur = 1
        malist.append((compteur, val_actuelle))

    print(f"\n{'='*70}")
    print(f" ANALYSE : {nom_image}")
    print(f"{'='*70}")
    
    header = f"{'Séquence':<18} | {'Règle appliquée':<20} | {'Code Binaire'}"
    print(header)
    print("-" * len(header))

    chaine_codee = ""
    for i, (nb, val) in enumerate(malist):
        couleur = "blanc" if val == 1 else "noir"
        seq_text = f"{nb} {couleur}"
        
        if nb >= 3:
            octet_ctrl = format(128 + nb, '08b') 
            donnee = str(int(val))
            regle = "Répétition (MSB=1)"
        else:
            octet_ctrl = format(nb, '08b') 
            donnee = str(int(val)) * nb
            regle = "Suite (MSB=0)"
        
        chaine_codee += octet_ctrl + donnee
        
  
        if i < 15:
            print(f"{seq_text:<18} | {regle:<20} | {octet_ctrl} + {donnee}")

    with open(fichier_txt, "w") as file:
        file.write(chaine_codee)


    taux = (len(chaine_codee) / len(fimage)) * 100
    print("-" * len(header))
    print(f"Taux de compression : {taux:.2f}%")
    
    return chaine_codee, height, width
def Decode(fichier_txt, height, width, nom_sortie):
    with open(fichier_txt, "r") as file:
        txt = file.read() 

    resultat = [] 
    idx = 0

    while idx < len(txt):
        octet_ctrl = txt[idx:idx+8]
        val_ctrl = int(octet_ctrl, 2)
        idx += 8
        
        if val_ctrl >= 128:
        
            nb = val_ctrl - 128
            val_pixel = int(txt[idx])
            resultat.extend([val_pixel] * nb)
            idx += 1
        else:
            
            nb = val_ctrl
            for _ in range(nb):
                resultat.append(int(txt[idx]))
                idx += 1
    
   
    decoded_image = np.array(resultat).reshape((height, width)).astype(np.uint8)
    cv2.imwrite(nom_sortie, decoded_image * 255)
    print(f"Image décodée : {nom_sortie}")

for img_name in ['image.bmp','cablecar.BMP']:
    try:
        data_bin, h, w = Encode(img_name, f"compression_{img_name}.txt")
        if data_bin:
            Decode(f"compression_{img_name}.txt", h, w, f"decompression_{img_name}")
    except Exception as e:
        print(f"Erreur lors du traitement de {img_name} : {e}")