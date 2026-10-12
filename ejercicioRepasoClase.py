cursoMasRapido = 1.5
cursoMasRapidoPromedio = 2.5
cursoPromedio = 4
crudoCursoPromedio = 5
crudoEsteCurso= 3.5 
cursoMaximo = 7

diferenciaMasRapido = (cursoMasRapidoPromedio / cursoMasRapido)*100
print(diferenciaMasRapido)

diferenciaMasLento = (cursoMaximo/cursoMasRapido)*100
print("\n")
print(diferenciaMasLento)

promedioCursos = (cursoMasRapido + cursoPromedio + cursoMaximo + cursoMasRapidoPromedio)/4
print(promedioCursos)

porcentajeReducible = crudoCursoPromedio-promedioCursos
print(porcentajeReducible)

porcentajeReducible2 = crudoEsteCurso-cursoMasRapido
print(porcentajeReducible2)

cuantoVeces = cursoMasRapido*10
vistasMaximo = cuantoVeces/cursoMaximo
vistasPromedio = cuantoVeces/cursoPromedio
vistasMinimas = cuantoVeces/cursoMasRapidoPromedio

print("\n")
print(vistasMaximo)
print(vistasPromedio)
print(vistasMinimas)


