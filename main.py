"""Module pour encoder une chaîne de caractères en liste de tuples (caractère, occurrences)."""


def artcode_i(s):
    """Retourne la liste de tuples encodant une chaîne de caractères passée en argument
       selon un algorithme itératif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: La liste des tuples (caractère, nombre d'occurrences).
    """
    if not s:
        return []
    
    tab = []
    letter = s[0]
    compt = 1

    for i in s[1:]:
        if i == letter:
            compt += 1
        else:
            tab.append((letter, compt))
            letter = i
            compt = 1
    tab.append((letter, compt)) 
    return tab

def artcode_r(s):
    """Retourne la liste de tuples encodant une chaîne de caractères passée en argument
       selon un algorithme récursif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: La liste des tuples (caractère, nombre d'occurrences).
    """
    if not s:
        return []
    
    def recursive_helper(sub_s, current_char, count):
        if not sub_s:
            return [(current_char, count)]
        if sub_s[0] == current_char:
            return recursive_helper(sub_s[1:], current_char, count + 1)
        return [(current_char, count)] + recursive_helper(sub_s[1:], sub_s[0], 1)
    
    return recursive_helper(s[1:], s[0], 1)


def main():
    """Fonction principale pour tester les fonctions itérative et récursive."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
