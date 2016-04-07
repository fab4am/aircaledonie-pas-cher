# Aircaledonie-pas-cher
Trouve les meilleurs tarifs Air Calédonie pour un séjour dans les îles ou le nord calédonien

Script python3, options à éditer en début de fichier :

```python
delaidepart = 15 # en jours, dans combien de jours souhaitez-vous partir au plus tôt
departauplustard = 40 # en jours,  dans combien de jours souhaitez-vous partir au plus tard
dureesejourmin = 3 # durée minimale du séjour en jours (exemple 3 = 2 jours, 2 nuits)
dureesejourmax = 7 # surée maximale du séjour en jours
prixmax = 16000 # prix maximum pour 1 personne aller-retour
destination = "LIF" # code destination, liste ci-dessous
```

puis lancer le script : 
```
python3 aircaledonie-pas-cher.py
```

Exemple d'exécution :
```
15700 F : Séjour de 3 jours du 2016-04-22 au 2016-04-25 (7850 F + 7850 F)
15700 F : Séjour de 4 jours du 2016-04-22 au 2016-04-26 (7850 F + 7850 F)
15700 F : Séjour de 3 jours du 2016-04-26 au 2016-04-29 (7850 F + 7850 F)
15700 F : Séjour de 4 jours du 2016-04-26 au 2016-04-30 (7850 F + 7850 F)
15700 F : Séjour de 3 jours du 2016-04-28 au 2016-05-01 (7850 F + 7850 F)
15700 F : Séjour de 4 jours du 2016-04-28 au 2016-05-02 (7850 F + 7850 F)
15700 F : Séjour de 3 jours du 2016-04-29 au 2016-05-02 (7850 F + 7850 F)
15700 F : Séjour de 4 jours du 2016-04-29 au 2016-05-03 (7850 F + 7850 F)

```
