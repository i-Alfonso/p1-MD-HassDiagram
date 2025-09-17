# EJEMPLO 2: Palabras ordenadas lexicográficamente
from graficos.mostrar import mostrar_analisis_completo

print("\n" + "="*60)
print("EJEMPLO 2: Palabras con orden lexicográfico")
print("="*60)

conjunto2 = {"a", "ab", "abc", "ac", "b", "bc"}

# Orden lexicográfico (como en el diccionario)
relacion2 = {
    # Reflexiva
    ("a", "a"), ("ab", "ab"), ("abc", "abc"), ("ac", "ac"), ("b", "b"), ("bc", "bc"),

    # Orden lexicográfico
    ("a", "ab"), ("a", "abc"), ("a", "ac"), ("a", "b"), ("a", "bc"),
    ("ab", "abc"), ("ab", "ac"), ("ab", "b"), ("ab", "bc"),
    ("abc", "ac"), ("abc", "b"), ("abc", "bc"),
    ("ac", "b"), ("ac", "bc"),
    ("b", "bc")
}

print("A = {a, ab, abc, ac, b, bc}")
print("Relación: orden lexicográfico (≤)")
mostrar_analisis_completo(conjunto2, relacion2)
