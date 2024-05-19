<h2>Exercícios</h2>

??? question "Como adaptar a [curva de Koch](https://pt.wikipedia.org/wiki/Curva_de_Koch) para um quadrado?"

    ``` python title="Quadrado de Koch"
    def quadrado_de_koch(comprimento):
	    if comprimento < 8:
	        linha(comprimento)          # ________
	    else:
	        comprimento /= 4

	        curva_de_koch(comprimento)  # __

	        gira(90)
	        curva_de_koch(comprimento)  # __|

	        gira(-90)                   #    __
	        curva_de_koch(comprimento)  # __|

	        gira(-90)                   #    __
	        curva_de_koch(comprimento)  # __|  |

	        gira(90)                    #    __
	        curva_de_koch(comprimento)  # __|  |__
