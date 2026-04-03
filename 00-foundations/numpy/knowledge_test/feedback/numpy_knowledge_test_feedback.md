# Correction du test de connaissance NumPy

## Retour de l'AI

- `Juste` = bonne reponse
- `Faux` = reponse incorrecte
- `A revoir` = idee correcte mais reponse incomplete ou pas assez precise

## Consignes

- Durée conseillée : 45 à 60 minutes
- Répondre directement sous chaque question ou dans un fichier Python séparé
- Utiliser uniquement les notions présentes dans `numpy_journal.py`
- Barème total : 20 points

---

## Partie 1 - Bases des tableaux NumPy (4 points)

### Exercice 1 - Vocabulaire et observation (2 points)

On considère le tableau suivant :

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
```

1. Donner la valeur de `a.shape`
a.shape = 2, 3
**AI : Juste.** La forme attendue est `(2, 3)`.

2. Donner la valeur de `a.ndim`
a.ndim = 2
**AI : Juste.**

3. Donner la valeur de `a.size`
a.size = 6
**AI : Juste.**

4. Expliquer en une phrase la différence entre `shape` et `size`
la shape c'est la forme du tableau donc la nombre de ligne suivie du nombre de col.
la size c'est le nombre de valeur présent dans le tableau.
**AI : Juste.** L'idee est bonne.

### Exercice 2 - Copie (2 points)

On exécute le code suivant :

```python
original = np.array([[1, 2], [3, 4]])
copie = np.copy(original)
copie[0, 0] = 99
```

1. Quelle est la valeur de `copie[0, 0]` ?
~~copie[0, 0] = [[99 2],
              [3, 4]]~~
**AI : Faux.** On demandait la valeur a l'index `[0, 0]`, donc la bonne reponse est `99`.

2. Quelle est la valeur de `original[0, 0]` ?
~~original[0, 0] = [[1 2],
                 [3, 4]]~~
**AI : Faux.** On demandait la valeur a l'index `[0, 0]`, donc la bonne reponse est `1`.

3. Pourquoi `np.copy()` est-il utile ici ?
np.copy sert a ne pas modifier le tableau original si on le fait pas on vas le modifer
**AI : Juste.**

---

## Partie 2 - Création et transformation de tableaux (6 points)

### Exercice 3 - Création de tableaux (2 points)

Écrire une ligne NumPy pour créer :

1. Un tableau contenant les entiers de `0` à `11`
arr = np.arange(0, 12)
**AI : Juste.**

2. Un tableau de 6 valeurs régulièrement espacées entre `10` et `100`
~~arr = np.linespace(10, 100, num=6)~~
**AI : A revoir.** Bonne idee, c'est surtout une etourderie de syntaxe. La bonne fonction est `np.linspace(10, 100, num=6)`.

3. Un tableau de trois `1` avec le type `int64`
~~arr = np.ones(3, dtype=int64)~~
**AI : A revoir.** La reponse est bonne dans l'idee, il manque juste le prefixe `np.` : `np.ones(3, dtype=np.int64)`.

### Exercice 4 - Reshape et axes (2 points)

On considère :

```python
b = np.array([[1, 2, 3], [4, 5, 6]])
```

1. Transformer `b` en un tableau de forme `(3, 2)`
c = np.reshape(b ,(3, 2)) je suis pas obliger de le save dans une var mais je le fais pas simple automatisme
mais ici on reshape pas vraimment b il on peut faire b.reshape(3,2)
**AI : Juste.** `np.reshape(b, (3, 2))` ou `b.reshape(3, 2)` conviennent.

2. Expliquer pourquoi cette transformation est possible
~~Cette transfomation est possible car si on divise le nombre de ligne que le veut que le tableau est donc 3 / 3 = 1 donc on peux effectivement rajouté une ligne.
Exemple pour 4 ligne 3 / 4 = 0.75 pas un nombre entier on peux donc pas crée de ligne sumplémentaire.~~
**AI : Faux.** La vraie raison est qu'on garde le meme nombre total d'elements : `2 x 3 = 6` et `3 x 2 = 6`.

3. À partir de `t = np.array([1, 2, 3, 4])`, créer :
   - une version ligne de forme `(1, 4)`
   `t.reshape(1, 4)`
   **AI : Juste.**

   - une version colonne de forme `(4, 1)`
   `t.reshape(4, 1)`
   **AI : Juste.**

### Exercice 5 - Flatten et ravel (2 points)

Répondre aux questions suivantes :

1. Quelle différence de comportement observe-t-on entre `flatten()` et `ravel()` ?
Flatten n'affecte pas la tableau d'origin si on le modifi alors que Ravel lui vas modifier le tableau d'origin
**AI : Juste.** Bonne idee generale.

2. Lequel retourne une copie ?
Flatten car il modifi pas le tableau original
**AI : Juste.**

3. Lequel peut modifier le tableau d’origine si on modifie le résultat ?
Ravel
**AI : Juste.**

---

## Partie 3 - Indexation, slicing et masques (4 points)

### Exercice 6 - Lecture de valeurs (2 points)

On considère :

```python
c = np.array([[1, 2, 3, 4],
             [10, 20, 30, 40]])
```

Donner le résultat de :

1. `c[1, 2]`
c[1, 2] = 30
**AI : Juste.**

2. `c[0]`
c[0] = [1, 2, 3, 4]
**AI : Juste.**

3. `c[1:2]`
c[1:2] = [[10 20 30 40]]
**AI : Juste.**

4. `c[:, 1]`
c[:, 1] = [2 20]
**AI : Juste.**

### Exercice 7 - Masques booléens (2 points)

On considère :

```python
d = np.array([[1, 8, 3], [4, 11, 6]])
```

1. Écrire une expression qui sélectionne les valeurs supérieures ou égales à `5`
~~d = [d >= 5]~~
**AI : A revoir.** Tu avais la bonne condition, mais la syntaxe de selection attendue etait `d[d >= 5]`.

2. Écrire une expression qui sélectionne les valeurs paires
~~d = [d % 2 == 0]~~
**AI : A revoir.** La condition est bonne, mais la syntaxe attendue etait `d[d % 2 == 0]`.

3. À quoi sert `np.nonzero(d == 11)` ?
Je sais pas
**AI : Faux.** Cette expression sert a trouver la position de la valeur `11` dans le tableau.

---

## Partie 4 - Assemblage, séparation et opérations (6 points)

### Exercice 8 - Stacking et splitting (2 points)

On considère :

```python
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
z = np.arange(1, 29).reshape(4, 7)
```

1. Quelle est la différence entre `np.vstack((x, y))` et `np.hstack((x, y))` ?
np.vstack comme son nom l'indic il stack verticalement le tableau et np Hstack satck horizontalement
**AI : Juste.**

2. Que fait `np.hsplit(z, (2, 4))` ?
il slipt la tableau en 3 array 2, 4
**AI : A revoir.** L'idee est bonne, mais il faut dire que le tableau est decoupe selon les colonnes aux positions `2` et `4`.

3. Combien de sous-tableaux sont produits par cette opération ?
3
**AI : Juste.**

### Exercice 9 - Calculs et opérations utiles (2 points)

On considère :

```python
e = np.arange(1, 11)
f = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
m = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
```

1. Que fait l’expression `f // e` ?
il vas divisé le tableau f avec e
**AI : A revoir.** Oui, mais plus precisement c'est une division entiere element par element.

2. Que renvoie `m.sum(axis=0)` ?
la some des ligne de m
**AI : A revoir.** Tu as bien identifie l'idee de la somme, mais tu as inverse `axis=0` et `axis=1`. Ici `axis=0` donne la somme des colonnes : `array([9., 12.])`.

3. Que renvoie `m.sum(axis=1)` ?
la some de col de m
**AI : A revoir.** Meme inversion ici. `axis=1` donne la somme des lignes : `array([3., 7., 11.])`.

4. À quoi sert `.T` sur une matrice ?
**AI : Faux.** Non repondu. `.T` sert a transposer la matrice.

### Exercice 10 - Uniques, inversion et mini-code (2 points)

1. À quoi sert `np.unique(tab, return_index=True)` ?
c'est pour return l'index du tableau(tab)
**AI : A revoir.** Pas seulement. Cette fonction renvoie les valeurs uniques et leur premiere position.

2. À quoi sert `np.flip(tab, axis=1)` ?
c'est pour flip l'axis des collone
**AI : A revoir.** Oui, plus precisement cela inverse l'ordre des colonnes.

3. Écrire un court code NumPy qui :
   - crée un tableau de 24 entiers
   ~~a = np.arange(25)~~
   **AI : Faux.** `np.arange(25)` cree 25 valeurs. Il fallait 24 valeurs, par exemple `np.arange(1, 25)`.

   - le transforme en matrice de 6 lignes et 4 colonnes
   `a = a.reshape(6, 4)`
   **AI : A revoir.** Cette ligne est correcte seulement si `a` contient bien 24 valeurs.

   - inverse l’ordre des colonnes
   `a = np.flip(a, axis=1)`
   **AI : Juste.**

---

## Critères de réussite

- Utiliser correctement `shape`, `ndim`, `size`
- Savoir créer et transformer des tableaux
- Maîtriser l’indexation et les masques
- Comprendre `vstack`, `hstack`, `hsplit`
- Savoir utiliser les opérations courantes de NumPy
- Bien distinguer `flatten()` et `ravel()`

---

## Résultat final

- Exercice 1 : `2 / 2`
- Exercice 2 : `1 / 2`
- Exercice 3 : `2 / 2`
- Exercice 4 : `1.5 / 2`
- Exercice 5 : `2 / 2`
- Exercice 6 : `2 / 2`
- Exercice 7 : `0.5 / 2`
- Exercice 8 : `1.5 / 2`
- Exercice 9 : `1.5 / 2`
- Exercice 10 : `1 / 2`

**Note finale : 15 / 20**

Commentaire de l'AI :
Bonne copie dans l'ensemble. Les bases sont comprises, surtout l'indexation, `reshape`, `flatten` et `ravel`. J'ai allege la correction sur les etourderies de syntaxe et l'inversion de `axis`, car l'idee generale etait souvent bonne. Il faut quand meme continuer a securiser la syntaxe exacte des fonctions et des masques booleens.
