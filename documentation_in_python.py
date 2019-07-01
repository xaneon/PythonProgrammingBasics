""" Beschreibung des Moduls. """
def addiere(arg1, arg2):
    """*Addiert* ``arg1`` und ``arg2``."""
    return arg1 + arg2

# Kommentar eines Entwicklers
def multipliziere(arg1, arg2):
    """
        >>> multipliziere(3, 5)
        15
    """
    return arg1 * arg2

def potenziere(basis, exponent):
    """
    **Zusammenfassung** der Funktion.

    Parameters
    -----------
    basis: float
        Die Beschreibung zu ``basis``.
    exponent: int
        Die Beschreibung zu  ``exponent``.

    Returns
    --------
    int
        Das Ergebnis des Pontenzierens.
    """
    return basis ** exponent
