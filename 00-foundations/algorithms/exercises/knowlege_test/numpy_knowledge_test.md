# Test de connaissance NumPy

## Consignes

- Duree conseillee : 45 a 60 minutes
- Repondre directement sous chaque question ou dans un fichier Python separe
- Utiliser uniquement les notions presentes dans `numpy_journal.py`
- Bareme total : 20 points

---

## Partie 1 - Bases des tableaux NumPy (4 points)

### Exercice 1 - Vocabulaire et observation (2 points)

On considere le tableau suivant :

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
```

1. Donner la valeur de `a.shape`
2. Donner la valeur de `a.ndim`
3. Donner la valeur de `a.size`
4. Expliquer en une phrase la difference entre `shape` et `size`

### Exercice 2 - Copie (2 points)

On execute le code suivant :

```python
original = np.array([[1, 2], [3, 4]])
copie = np.copy(original)
copie[0, 0] = 99
```

1. Quelle est la valeur de `copie[0, 0]` ?
2. Quelle est la valeur de `original[0, 0]` ?
3. Pourquoi `np.copy()` est-il utile ici ?

---

## Partie 2 - Creation et transformation de tableaux (6 points)

### Exercice 3 - Creation de tableaux (2 points)

Ecrire une ligne NumPy pour creer :

1. Un tableau contenant les entiers de `0` a `11`
2. Un tableau de 6 valeurs regulierement espacees entre `10` et `100`
3. Un tableau de trois `1` avec le type `int64`

### Exercice 4 - Reshape et axes (2 points)

On considere :

```python
b = np.array([[1, 2, 3], [4, 5, 6]])
```

1. Transformer `b` en un tableau de forme `(3, 2)`
2. Expliquer pourquoi cette transformation est possible
3. A partir de `t = np.array([1, 2, 3, 4])`, creer :
   - une version ligne de forme `(1, 4)`
   - une version colonne de forme `(4, 1)`

### Exercice 5 - Flatten et ravel (2 points)

Repondre aux questions suivantes :

1. Quelle difference de comportement observe-t-on entre `flatten()` et `ravel()` ?
2. Lequel retourne une copie ?
3. Lequel peut modifier le tableau d'origine si on modifie le resultat ?

---

## Partie 3 - Indexation, slicing et masques (4 points)

### Exercice 6 - Lecture de valeurs (2 points)

On considere :

```python
c = np.array([[1, 2, 3, 4], [10, 20, 30, 40]])
```

Donner le resultat de :

1. `c[1, 2]`
2. `c[0]`
3. `c[1:2]`
4. `c[:, 1]`

### Exercice 7 - Masques booleens (2 points)

On considere :

```python
d = np.array([[1, 8, 3], [4, 11, 6]])
```

1. Ecrire une expression qui selectionne les valeurs superieures ou egales a `5`
2. Ecrire une expression qui selectionne les valeurs paires
3. A quoi sert `np.nonzero(d == 11)` ?

---

## Partie 4 - Assemblage, separation et operations (6 points)

### Exercice 8 - Stacking et splitting (2 points)

On considere :

```python
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
z = np.arange(1, 29).reshape(4, 7)
```

1. Quelle est la difference entre `np.vstack((x, y))` et `np.hstack((x, y))` ?
2. Que fait `np.hsplit(z, (2, 4))` ?
3. Combien de sous-tableaux sont produits par cette operation ?

### Exercice 9 - Calculs et operations utiles (2 points)

On considere :

```python
e = np.arange(1, 11)
f = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
m = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
```

1. Que fait l'expression `f // e` ?
2. Que renvoie `m.sum(axis=0)` ?
3. Que renvoie `m.sum(axis=1)` ?
4. A quoi sert `.T` sur une matrice ?

### Exercice 10 - Uniques, inversion et mini-code (2 points)

1. A quoi sert `np.unique(tab, return_index=True)` ?
2. A quoi sert `np.flip(tab, axis=1)` ?
3. Ecrire un court code NumPy qui :
   - cree un tableau de 24 entiers
   - le transforme en matrice de 6 lignes et 4 colonnes
   - inverse l'ordre des colonnes

---

## Bonus - Exercice pratique (2 points)

Ecrire un script NumPy qui realise toutes les etapes suivantes :

1. Creer un tableau 1D contenant les valeurs de `1` a `12`
2. Le transformer en matrice `3 x 4`
3. Afficher la deuxieme ligne
4. Afficher uniquement les valeurs paires
5. Empiler horizontalement cette matrice avec elle-meme
