# Guide d'installation - University Scholar

## Problème : "No module found!"

Si vous voyez ce message, suivez ces étapes :

### 1. Vérifier que le module est au bon endroit
Le module doit être dans : `/home/kramharroubi/odoo18/addons/university_scholar/`

### 2. Redémarrer Odoo
Après avoir créé un nouveau module, Odoo doit être redémarré :
```bash
# Arrêtez Odoo (Ctrl+C ou kill)
# Puis redémarrez-le
./odoo-bin -c odoo.conf
```

### 3. Mettre à jour la liste des applications
Dans l'interface Odoo :
1. Allez dans **Apps** (Applications)
2. Cliquez sur **"Mettre à jour la liste des applications"** (Update Apps List)
3. Attendez que la mise à jour soit terminée

### 4. Activer le mode développeur (si nécessaire)
Si le module n'apparaît toujours pas :
1. Allez dans **Paramètres** > **Activer le mode développeur**
2. Retournez dans **Apps**
3. Cliquez sur **"Mettre à jour la liste des applications"** à nouveau
4. Recherchez "University Scholar" ou "university_scholar"

### 5. Vérifier les chemins d'addons
Si le problème persiste, vérifiez que le chemin des addons est correct dans votre fichier de configuration Odoo :
```ini
[options]
addons_path = /home/kramharroubi/odoo18/addons,/home/kramharroubi/odoo18/odoo/addons
```

### 6. Vérifier les logs
Consultez les logs Odoo pour voir s'il y a des erreurs :
```bash
tail -f /var/log/odoo/odoo.log
# ou selon votre configuration
```

## Installation du module

Une fois le module visible :
1. Recherchez "University Scholar" dans Apps
2. Cliquez sur **Installer**
3. Attendez la fin de l'installation

## Configuration

1. Allez dans **Paramètres** > **University Scholar**
2. Entrez votre clé API SerpAPI (obtenue sur https://serpapi.com/)
3. Sauvegardez

## Utilisation

1. Allez dans **Université** > **Enseignants**
2. Créez un nouvel enseignant
3. Renseignez le **Google Scholar ID**
4. Cliquez sur **"Synchroniser avec Google Scholar"**

