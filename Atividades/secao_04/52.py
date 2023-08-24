inv1 = float(input('Quanto o apostador 1 investiu na aposta?'))
inv2 = float(input('Quanto o apostador 2 investiu na aposta?'))
inv3 = float(input('Quanto o apostador 3 investiu na aposta?'))
premio = float(input('Valor do prémio:'))

invTotal = inv1 + inv2 + inv3

val1 = (inv1 * premio) / invTotal
val2 = (inv2 * premio) / invTotal
val3 = (inv3 * premio) / invTotal

print(f"O premio do apostador 1 é: {round(val1, 2)}")
print(f"O premio do apostador 2 é: {round(val2, 2)}")
print(f"O premio do apostador 3 é: {round(val3, 2)}")
