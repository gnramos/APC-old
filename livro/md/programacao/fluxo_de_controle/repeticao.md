# Repetição

<h2>Exercícios</h2>

??? question "Implemente o código que leia a quantidade máxima N de elefantes e apresente a letra da música até que N (≥1) elefantes incomodem muita gente. Por exemplo, para N = 4: **1 elefante incomoda muita gente... 2 elefantes incomodam, incomodam muito mais! 2 elefantes incomodam muita gente... 3 elefantes incomodam, incomodam, incomodam muito mais! 3 elefantes incomodam muita gente... 4 elefantes incomodam, incomodam, incomodam, incomodam muito mais!**"

    Uma possível solução é:
    ```python title="Elefantes"
    --8<-- "exercicios/programacao/fluxo_de_controle/repeticao/elefantes.py:14"
    ```

??? question "Considerando um comprimento *L*, implemente o código que desenha um quadrado de lado *L*."

    Uma possível solução é:
    ```python title="Quadrado"
    --8<-- "exercicios/programacao/fluxo_de_controle/repeticao/quadrado.py:10:15"
    ```



https://blockly.games/turtle?lang=pt-br


while Loops
The while loop is the second construct that can use and expressions to control a program’s execution flow. By using the and operator in the while statement header, you can test several conditions and repeat the loop’s code block for as long as all conditions are met.

Say you’re prototyping a control system for a manufacturer. The system has a critical mechanism that should work with a pressure of 500 psi or lower. If the pressure goes over 500 psi while staying under 700 psi, then the system has to run a given series of standard safety actions. For pressures greater than 700 psi, there are a whole new set of safety actions that the system must run.

To approach this problem, you can use a while loop with an and expression. Here’s a script that simulates a possible solution:

 1# pressure.py
 2
 3from time import sleep
 4from random import randint
 5
 6def control_pressure():
 7    pressure = measure_pressure()
 8    while True:
 9        if pressure <= 500:
10            break
11
12        while pressure > 500 and pressure <= 700:
13            run_standard_safeties()
14            pressure = measure_pressure()
15
16        while pressure > 700:
17            run_critical_safeties()
18            pressure = measure_pressure()
19
20    print("Wow! The system is safe...")
21
22def measure_pressure():
23    pressure = randint(490, 800)
24    print(f"psi={pressure}", end="; ")
25    return pressure
26
27def run_standard_safeties():
28    print("Running standard safeties...")
29    sleep(0.2)
30
31def run_critical_safeties():
32    print("Running critical safeties...")
33    sleep(0.7)
34
35if __name__ == "__main__":
36    control_pressure()
Inside control_pressure(), you create an infinite while loop on line 8. If the system is stable and the pressure is below 500 psi, the conditional statement breaks out of the loop and the program finishes.

On line 12, the first nested while loop runs the standard safety actions while the system pressure stays between 500 psi and 700 psi. In each iteration, the loop gets a new pressure measurement to test the condition again in the next iteration. If the pressure grows beyond 700 psi, then the second loop on line 16 runs the critical safety actions.

Note: The implementation of control_pressure() in the example above is intended to show how the and operator can work in the context of a while loop.

However, this isn’t the most efficient implementation you can write. You can refactor control_pressure() to use a single loop without using and:

def control_pressure():
    while True:
        pressure = measure_pressure()
        if pressure > 700:
            run_critical_safeties()
        elif 500 < pressure <= 700:
            run_standard_safeties()
        elif pressure <= 500:
            break
    print("Wow! The system is safe...")
In this alternative implementation, instead of using and, you use the chained expression 500 < pressure <= 700, which does the same as pressure > 500 and pressure <= 700 but is cleaner and more Pythonic. Another advantage is that you call measure_pressure() only once, which ends up being more efficient.


