# Sauvegardes de base de données Odoo

Ce dossier contient les sauvegardes de la base de données.

⚠️  **ATTENTION**: Les fichiers de sauvegarde peuvent être volumineux.

Pour restaurer une sauvegarde:
```bash
gunzip backups/odoo_YYYYMMDD_HHMMSS.sql.gz
psql -d odoo < backups/odoo_YYYYMMDD_HHMMSS.sql
```
