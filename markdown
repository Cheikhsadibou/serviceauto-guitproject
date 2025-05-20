# Gestion des Timezones - Configuration Spéciale

## Contexte
Pour résoudre l'erreur `database connection isn't set to UTC` malgré une configuration correcte, nous avons implémenté:

## Solution Technique
1. **Backend Personnalisé** :
   - Location: `your_app/db_backends/postgresql.py`
   - Surcharge la méthode `get_connection` pour désactiver la vérification stricte
   - Garantit que toutes les connexions utilisent UTC

2. **Dépendances** :
   - Nécessite psycopg2-binary >= 2.9.0
   - Compatible Django 3.0+

## Procédure de Mise à Jour
1. Avant déploiement :
   ```bash
   python manage.py check_timezone


   
**Emplacements recommandés** :
1. Fichier `docs/TIMEZONE_README.md` dans le dépôt
2. Page Confluence/Notion dédiée
3. Commentaire détaillé dans le fichier de backend personnalisé

---

### 4. Intégration dans les procédures de déploiement

**Checklist de déploiement** :

```markdown
## Pré-Déploiement
- [ ] Vérifier la timezone du serveur (`timedatectl status`)
- [ ] Confirmer que PostgreSQL est en UTC (`SHOW TIMEZONE`)
- [ ] Exécuter les tests timezone (`python manage.py check_timezone`)

## Post-Déploiement
- [ ] Monitorer les logs timezone pendant 24h
- [ ] Vérifier que les nouvelles données sont enregistrées en UTC