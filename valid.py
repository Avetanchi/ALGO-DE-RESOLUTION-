clause = input("entrer une fbf: ")
l = clause.split(" ")
i = 0
while i < len(l) - 1:
    if l[i] == "implique":
        l[i-1] = "-" + l[i-1]
        l[i] = "ou"
    if l[i] == "equ":
        A = l[i-1]
        B = l[i+1]

        l[i] = "ou"
        l[i+1] = "-" + B
        l.insert(i+2, "et")
        l.insert(i+3, B)
        l.insert(i+4, "ou")
        l.insert(i+5, "-" + A)
        i += 4
    i += 1
print(l)
for i in range(len(l)):
    if l[i] == "ou":
        l[i] = "et"
    elif l[i] == "et":
        l[i] = "ou"
    elif l[i][0] == "-":
        val = l[i]
        l[i] = val[1:]
    else:
        l[i] = "-" + l[i]

ensemble = []
stack = []
for i in l:
    if i != "et":
        stack.append(i)
    else:
        ensemble.append(stack)
        stack = []
ensemble.append(stack)

def negation(literal):
    if literal.startswith("-"):
        return literal[1:]
    return "-" + literal

print(ensemble)
for j in range(len(ensemble)):
    clause = ensemble[j]
    clause = [c for c in clause if c != "ou"]
    result = []
    for c in clause:
        if negation(c) not in clause:
            result.append(c)
            result.append("ou")
    ensemble[j] = result[:-1]
    
print(ensemble)

def existe_clause_vide(clauses):
    for cl in clauses:
        if cl == []:
            return True

def est_resolvable(clause1, clause2):
    for c in clause1:
        for d in clause2:
            if negation(c) == d:
                return True
def existe_paire_reductible(clauses):
    for clause1 in clauses:
        for clause2 in clauses:
            if clause1 != clause2 and est_resolvable(clause1, clause2):
                return True
    return False


def trouver_paire_resolvable(clauses):
    for clause1 in clauses:
        for clause2 in clauses:
            if clause1 != clause2 and est_resolvable(clause1, clause2):
                return clause1, clause2

def resoudre(clause1, clause2):
    clauses = [cl for cl in clause1 if cl != "ou"]
    for cl in clause2:
        if negation(cl) in clauses:
            clauses.remove(negation(cl))
        elif  cl != "ou":
            clauses.append(cl)
            
    result = []
    for cl in clauses:
        result.append(cl)
        result.append("ou")
    return result[:-1]

while not existe_clause_vide(ensemble) and existe_paire_reductible(ensemble):
   
    print("ensemble des clauses :", ensemble)

    clause1, clause2 = trouver_paire_resolvable(ensemble)
    print("Paire resolvable :", clause1, clause2)

    resolvante = resoudre(clause1, clause2)
    print("Resolvante :" ,resolvante)

    ensemble.remove(clause1)
    ensemble.remove(clause2)
    ensemble.append(resolvante)

print("ensemble final :", ensemble)
if existe_clause_vide(ensemble):
    print("fbf est valide")
else:
    print("fbf est non valide")
















