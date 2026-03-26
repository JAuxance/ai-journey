# NumPy Journal - Liste d'exercices d'entraînement

## Objectif

Cette liste suit directement les notions de `numpy_journal.py` pour t'aider à pratiquer de façon progressive.

## Règles de travail

- Utiliser uniquement `import numpy as np` (et `math` si besoin).
- Faire un exo à la fois, puis vérifier les sorties.
- Écrire du code lisible avec des noms de variables clairs.
- Vérifier `shape`, `ndim` et `dtype` quand c'est pertinent.

---

## Niveau 1 - Fondamentaux

### Exercice 1 - Observer un tableau
Créer `a = np.array([[2, 4, 6], [1, 3, 5]])`, puis afficher :
- `a.shape`
- `a.ndim`
- `a.size`
- `a.dtype`

### Exercice 2 - Copie sécurisée
Créer un tableau `original`, faire une copie avec `np.copy`, modifier la copie et prouver que `original` ne change pas.

### Exercice 3 - Création rapide
Créer les tableaux suivants :
- `np.arange(15)`
- `np.linspace(0, 1, num=5)`
- `np.ones((2, 3), dtype=np.int64)`
- `np.empty(4)`

### Exercice 4 - Trier et concaténer
Avec `x = np.array([9, 2, 7, 2, 1])` :
- trier `x`
- concaténer `x` avec `np.array([100, 200])`

### Exercice 5 - Reshape valide
Partir de `b = np.arange(1, 13)` :
- transformer en `(3, 4)`
- transformer en `(2, 6)`
- expliquer pourquoi `(5, 3)` ne fonctionne pas

### Exercice 6 - Lignes, colonnes, axes
Avec `t = np.array([10, 20, 30, 40])` :
- créer une version ligne `(1, 4)` avec `np.newaxis`
- créer une version colonne `(4, 1)` avec `np.newaxis`
- refaire avec `np.expand_dims`

### Exercice 7 - Indexing et slicing
Avec `c = np.array([[1, 2, 3, 4], [10, 20, 30, 40]])`, afficher :
- élément `30`
- première ligne
- deuxième ligne via slicing
- deuxième colonne

### Exercice 8 - Masques booléens
Avec `d = np.array([[1, 8, 3], [4, 11, 6]])`, récupérer :
- valeurs `>= 5`
- valeurs paires
- position de `11` avec `np.nonzero`

---

## Niveau 2 - Intermédiaire

### Exercice 9 - Empilement vertical et horizontal
Créer deux matrices `2x2` et comparer le résultat de :
- `np.vstack((m1, m2))`
- `np.hstack((m1, m2))`
Puis donner les shapes obtenues.

### Exercice 10 - Découpage de matrute tout les truc uselsse au projet dans au gitiice
Créer `z = np.arange(1, 29).reshape(4, 7)` puis utiliser `np.hsplit(z, (2, 4))`.
Afficher chaque sous-tableau avec son index.

### Exercice 11 - Opérations par axe
Créer `m = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])` :
- calculer `m.sum(axis=0)`
- calculer `m.sum(axis=1)`
- expliquer en une phrase la différence entre `axis=0` et `axis=1`

### Exercice 12 - Transpose
Générer une matrice aléatoire `3x2` et afficher sa transposée avec `.T`.
Vérifier que les shapes sont inversées.

### Exercice 13 - Valeurs uniques
Avec `u = np.array([4, 4, 2, 9, 2, 1, 9, 9])` :
- récupérer les valeurs uniques
- récupérer les indices de première apparition (`return_index=True`)

### Exercice 14 - Inversion de colonnes
Créer une matrice `6x4` puis inverser l'ordre des colonnes avec `np.flip(..., axis=1)`.

---

## Niveau 3 - Mise en pratique

### Exercice 15 - Pipeline 1D vers 2D
Écrire un mini-script qui :
1. crée un tableau de `1` à `24`
2. le reshape en `6x4`
3. affiche la 3e ligne
4. affiche uniquement les valeurs paires
5. inverse l'ordre des colonnes

### Exercice 16 - Flatten vs ravel
Montrer sur un exemple que :
- `flatten()` retourne une copie
- `ravel()` peut partager la mémoire avec l'original

### Exercice 17 - Résumé automatique d'un tableau
Écrire une fonction `describe_array(arr)` qui affiche :
- `shape`, `ndim`, `size`, `dtype`
- minimum, maximum, moyenne

### Exercice 18 - Mini challenge final
À partir d'une matrice aléatoire `5x5` :
1. remplacer toutes les valeurs `< 30` par `0`
2. extraire les valeurs `>= 30`
3. afficher les positions des valeurs strictement supérieures à `80`

---

## Format de rendu recommandé (propre pour le repo)

1. Créer un fichier `numpy_journal_solutions.py`.
2. Faire une fonction par exercice : `exo_01()`, `exo_02()`, etc.
3. Ajouter un `main()` qui appelle seulement les exos terminés.
4. Ajouter en commentaire en haut du fichier :
   - date
   - progression (`Niveau 1`, `Niveau 2`, `Niveau 3`)
5. Faire un commit avec un message clair, par exemple :
   - `add numpy journal training exercises solutions (level 1)`

## Critères de validation

- Tous les exos du Niveau 1 exécutés sans erreur.
- Au moins 4 exos du Niveau 2 terminés.
- 1 mini challenge du Niveau 3 terminé.
- Code poussé sur le repo avec un commit propre.
