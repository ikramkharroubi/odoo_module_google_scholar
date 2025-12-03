# 🗄️ Guide : Travailler avec la base de données Odoo

## 📋 Table des matières
1. [Restaurer une sauvegarde](#restaurer)
2. [Commandes SQL utiles](#sql)
3. [Gérer les modules via SQL](#modules)
4. [Gérer les utilisateurs](#utilisateurs)
5. [Vérifier l'état de la base](#verifier)
6. [Nettoyer la base](#nettoyer)

---

## 🔄 Restaurer une sauvegarde {#restaurer}

### Restaurer sur la même base

```bash
# 1. Arrêter Odoo
# Ctrl+C dans le terminal où Odoo tourne

# 2. Restaurer la sauvegarde
cd /home/kramharroubi/odoo18

# Si format SQL compressé
gunzip backups/odoo_20251203_205208.sql.gz
psql -d odoo < backups/odoo_20251203_205208.sql

# Si format SQL non compressé
psql -d odoo < backups/odoo_20251203_205208.sql
```

### Restaurer sur une nouvelle base

```bash
# 1. Créer une nouvelle base de données
createdb odoo_test

# 2. Restaurer
gunzip backups/odoo_20251203_205208.sql.gz
psql -d odoo_test < backups/odoo_20251203_205208.sql

# 3. Modifier odoo.conf pour pointer vers odoo_test
# db_name = odoo_test
```

---

## 🔍 Commandes SQL utiles {#sql}

### Se connecter à la base de données

```bash
psql -d odoo
```

### Commandes SQL de base

```sql
-- Lister toutes les tables
\dt

-- Lister toutes les bases de données
\l

-- Quitter psql
\q

-- Afficher la structure d'une table
\d university_teacher

-- Compter les enregistrements
SELECT COUNT(*) FROM university_teacher;
SELECT COUNT(*) FROM university_article;
```

### Requêtes utiles pour Odoo

```sql
-- Voir tous les modules installés
SELECT name, state, latest_version 
FROM ir_module_module 
WHERE state = 'installed'
ORDER BY name;

-- Voir les modules désinstallés
SELECT name, state 
FROM ir_module_module 
WHERE state = 'uninstalled';

-- Voir les utilisateurs
SELECT login, name, active 
FROM res_users 
ORDER BY login;

-- Voir les enseignants
SELECT id, name, scholar_id, article_count 
FROM university_teacher;

-- Voir les articles
SELECT id, name, year, citations, teacher_id 
FROM university_article 
ORDER BY citations DESC 
LIMIT 10;
```

---

## 📦 Gérer les modules via SQL {#modules}

### Désinstaller un module

```sql
-- Mettre le module en état 'uninstalled'
UPDATE ir_module_module 
SET state = 'uninstalled' 
WHERE name = 'nom_du_module';

-- Supprimer complètement un module
DELETE FROM ir_module_module WHERE name = 'nom_du_module';
DELETE FROM ir_model_data WHERE module = 'nom_du_module';
```

### Réinstaller un module

```sql
-- Remettre le module en état 'to install'
UPDATE ir_module_module 
SET state = 'to install' 
WHERE name = 'nom_du_module';
```

### Vérifier les dépendances

```sql
-- Voir les dépendances d'un module
SELECT name, dependencies_id 
FROM ir_module_module 
WHERE name = 'university_scholar';
```

---

## 👥 Gérer les utilisateurs {#utilisateurs}

### Créer un utilisateur administrateur

```sql
-- Créer un nouvel utilisateur admin
INSERT INTO res_users (login, password, name, active, company_id)
VALUES (
    'admin2',
    'pbkdf2_sha256$...',  -- Hash du mot de passe
    'Administrateur 2',
    true,
    1
);

-- Lui donner les droits admin
INSERT INTO res_groups_users_rel (gid, uid)
SELECT id, (SELECT id FROM res_users WHERE login = 'admin2')
FROM res_groups
WHERE full_name = 'Administration / Settings';
```

### Réinitialiser le mot de passe admin

```sql
-- Mot de passe: admin (en production, utilisez un hash sécurisé)
UPDATE res_users 
SET password = 'pbkdf2_sha256$600000$...' 
WHERE login = 'admin';
```

### Désactiver un utilisateur

```sql
UPDATE res_users 
SET active = false 
WHERE login = 'nom_utilisateur';
```

---

## ✅ Vérifier l'état de la base {#verifier}

### Vérifier l'intégrité

```sql
-- Vérifier les contraintes
SELECT conname, conrelid::regclass, confrelid::regclass
FROM pg_constraint
WHERE contype = 'f';

-- Vérifier les index
SELECT tablename, indexname 
FROM pg_indexes 
WHERE schemaname = 'public'
ORDER BY tablename;
```

### Statistiques de la base

```sql
-- Taille de la base de données
SELECT pg_size_pretty(pg_database_size('odoo'));

-- Taille des tables
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
LIMIT 20;
```

---

## 🧹 Nettoyer la base {#nettoyer}

### Supprimer les données de test

```sql
-- Supprimer tous les enseignants et leurs articles
DELETE FROM university_article;
DELETE FROM university_teacher;

-- Réinitialiser les séquences
ALTER SEQUENCE university_teacher_id_seq RESTART WITH 1;
ALTER SEQUENCE university_article_id_seq RESTART WITH 1;
```

### Nettoyer les modules désinstallés

```sql
-- Supprimer les modules en état 'uninstalled'
DELETE FROM ir_module_module WHERE state = 'uninstalled';
```

### Vider les logs

```sql
-- Supprimer les anciens logs (attention!)
DELETE FROM ir_logging WHERE create_date < NOW() - INTERVAL '30 days';
```

---

## 🔧 Scripts pratiques

### Script : Lister tous les enseignants et leurs articles

```bash
psql -d odoo -c "
SELECT 
    t.id,
    t.name AS enseignant,
    t.scholar_id,
    COUNT(a.id) AS nb_articles,
    COALESCE(SUM(a.citations), 0) AS total_citations
FROM university_teacher t
LEFT JOIN university_article a ON a.teacher_id = t.id
GROUP BY t.id, t.name, t.scholar_id
ORDER BY total_citations DESC;
"
```

### Script : Exporter les données en CSV

```bash
psql -d odoo -c "
COPY (
    SELECT t.name, a.name AS article, a.year, a.citations
    FROM university_teacher t
    JOIN university_article a ON a.teacher_id = t.id
) TO '/tmp/articles_export.csv' WITH CSV HEADER;
"
```

---

## ⚠️ Précautions importantes

1. **Toujours faire une sauvegarde avant** de modifier la base directement
2. **Tester sur une copie** avant d'appliquer sur la production
3. **Ne pas modifier directement** les tables système d'Odoo si possible
4. **Utiliser l'interface Odoo** quand c'est possible plutôt que SQL direct

---

## 📚 Ressources

- Documentation PostgreSQL : https://www.postgresql.org/docs/
- Documentation Odoo ORM : https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html

