# NumPy - Points a revoir

## Priorite haute

- Syntaxe des masques booleens : `tab[condition]`
- Difference entre `axis=0` et `axis=1`
- Repondre exactement a la question quand on demande une valeur unique comme `a[0, 0]`

## Syntaxe a securiser

- `np.linspace(...)` et non `np.linespace(...)`
- `np.ones(3, dtype=np.int64)` avec le prefixe `np.`
- Verifier le nombre d'elements avant un `reshape`

## Notions a reviser

- `np.nonzero(...)` pour trouver une position
- `np.unique(tab, return_index=True)` pour recuperer les valeurs uniques et leur premiere position
- `np.flip(tab, axis=1)` pour inverser l'ordre des colonnes
- `.T` pour transposer une matrice
- `np.hsplit(...)` pour decouper selon les colonnes
