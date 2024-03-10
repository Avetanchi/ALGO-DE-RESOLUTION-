# ALGO-DE-RESOLUTION-
ALGORITHME DE RESOLUTION POUR TESTER LA VALIDITE D UNE FORMULE BIEN FORMEE


equivalent -> "equ"

implique -> "implique"

et -> "et"

ou  -> "ou"

negation de A -> -A

exmple de input : a eq b et c implique -a

*Algorithme de résolution*

Début
Ecrire la négation de F ;

Mettre F sous forme d'un ensemble de clauses ;

Tant que

la clause vide n'est pas rencontrée et qu'il
existe des paires réductibles faire

Début
Chercher des clauses résolvantes ;

Ajouter ce résultat à la liste des clauses ;

Fintantque

Si

on trouve la clause vide alors F est valide

sinon

F est invalide

Finsi

Fin ;

