# 💾 Guide de sauvegarde de la base de données Odoo

## 🚀 Méthodes de sauvegarde

### Méthode 1 : Script automatique (Recommandé)

```bash
cd /home/kramharroubi/odoo18

# Sauvegarde avec compression (format custom PostgreSQL)
./backup_db.sh odoo

# Ou spécifier un autre dossier
./backup_db.sh odoo /chemin/vers/backups
```

**Avantages** :
- Format optimisé PostgreSQL (plus rapide)
- Compression automatique
- Horodatage automatique
- Facile à restaurer

### Méthode 2 : Script simple (format SQL)

```bash
cd /home/kramharroubi/odoo18

# Sauvegarde en format SQL texte
./backup_db_simple.sh odoo
```

**Avantages** :
- Format SQL lisible
- Peut être restauré sur n'importe quelle base PostgreSQL
- Compression automatique

### Méthode 3 : Commande pg_dump directe

```bash
# Sauvegarde format custom (recommandé)
pg_dump -Fc -f backup_odoo_$(date +%Y%m%d).dump odoo

# Sauvegarde format SQL
pg_dump odoo > backup_odoo_$(date +%Y%m%d).sql

# Avec compression
pg_dump odoo | gzip > backup_odoo_$(date +%Y%m%d).sql.gz
```

### Méthode 4 : Via l'interface Odoo

1. Allez dans **Paramètres** → **Technique** → **Base de données** → **Sauvegardes**
2. Cliquez sur **"Sauvegarder"**
3. Entrez un nom pour la sauvegarde
4. Cliquez sur **"Sauvegarder"**

## 📁 Emplacement des sauvegardes

Par défaut, les scripts sauvegardent dans :
- `./backups/` (dans le répertoire Odoo)

Vous pouvez créer un dossier dédié :
```bash
mkdir -p /home/kramharroubi/backups_odoo
./backup_db.sh odoo /home/kramharroubi/backups_odoo
```

## 🔄 Restaurer une sauvegarde

### Restaurer depuis format custom (.dump)

```bash
# Créer une nouvelle base de données (optionnel)
createdb nouvelle_base

# Restaurer
pg_restore -d nouvelle_base -c backup_odoo_20231203.dump
```

### Restaurer depuis format SQL

```bash
# Si compressé, décompresser d'abord
gunzip backup_odoo_20231203.sql.gz

# Restaurer
psql -d nouvelle_base < backup_odoo_20231203.sql
```

## ⏰ Sauvegarde automatique (Cron)

Pour créer des sauvegardes automatiques quotidiennes :

```bash
# Éditer le crontab
crontab -e

# Ajouter cette ligne (sauvegarde tous les jours à 2h du matin)
0 2 * * * /home/kramharroubi/odoo18/backup_db.sh odoo /home/kramharroubi/backups_odoo >> /var/log/odoo_backup.log 2>&1
```

## 🗑️ Nettoyer les anciennes sauvegardes

Pour garder seulement les 7 dernières sauvegardes :

```bash
# Garder seulement les 7 dernières
cd /home/kramharroubi/backups_odoo
ls -t *.dump | tail -n +8 | xargs rm -f
```

## ✅ Bonnes pratiques

1. **Sauvegarder régulièrement** : Au moins une fois par jour
2. **Sauvegarder avant les mises à jour** : Toujours avant d'installer/mettre à jour des modules
3. **Tester les restaurations** : Vérifiez que vos sauvegardes fonctionnent
4. **Stockage externe** : Copiez les sauvegardes sur un autre serveur/disque
5. **Conserver plusieurs versions** : Gardez au moins 7-30 jours de sauvegardes

## 📊 Vérifier une sauvegarde

```bash
# Vérifier le contenu d'une sauvegarde custom
pg_restore --list backup_odoo_20231203.dump | head -20

# Vérifier la taille
ls -lh backup_odoo_*.dump
```

## 🔐 Sécurité

- **Protégez vos sauvegardes** : Elles contiennent toutes vos données
- **Chiffrement** : Pour les sauvegardes sensibles, utilisez le chiffrement
- **Permissions** : Limitez l'accès aux fichiers de sauvegarde

---

**Scripts créés** :
- `backup_db.sh` - Sauvegarde format custom (recommandé)
- `backup_db_simple.sh` - Sauvegarde format SQL

