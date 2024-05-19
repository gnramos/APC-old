<h2>Exercícios</h2>

??? question "Faça um algoritmo em descrição narrativa para trocar uma lâmpada queimada de um abajur já tendo outra lâmpada nova disponível."

    ``` linguagem_natural title="Trocar Lâmpada"
    Desligue o abajur da tomada e retire a lâmpada queimada desenroscando-a em sentido anti-horário (separe para descartar no local apropriado). Pegue a lâmpada nova e a coloque no abajur, rosqueando-a no sentido horário. Ligue o abajur na tomada.
    ```

??? question "Represente o algoritmo para cálculo da média aritmética de quatro números usando fluxograma."

    ``` mermaid
    flowchart TD
        I([Início]) --> L4[/Leia 4 notas/] --> M["µ = notas ÷ 4"] --> A[Apresente µ] --> T([Fim])
    ```

??? question "Monte um fluxograma para um algoritmo que leia os três coeficientes de uma equação de segundo grau e diga se as raízes são reais ou complexas, e se são iguais. $ax^2+bx+c = 0 \Rightarrow r = \frac{-b\pm\sqrt{b^2-4ac}}{2a}$"

    ``` mermaid
    flowchart TD
        I([Início]) --> L4[/Leia 4 notas/] --> D["Δ = b² - 4ac"] --> M0{"Δ < 0?"} -->|Sim| RC[/Raízes complexas/] --> F([Fim])
        M0 --> |Não| RR[/Raízes reais/] --> D0{"Δ = 0?"} -->|Sim| VR[/Raízes iguais/] --> F
        D0 -->|Não| F
    ```

??? question "Descreva, em pseudocódigo, um algoritmo para ler dois números e apresentar o resultado da divisão do primeiro pelo segundo."

    ``` title="Divisão"
    Início
        Escreva "Digite o numerador: "
        Leia [numerador].
        Escreva "Digite o denominador: "
        Leia o [denominador].
        divisão = numerador ÷ denominador
        Escreva "O resultado é [divisão]."
    Fim
    ```

??? question "Descreva, em pseudocódigo, o algoritmo para ler a idade de uma pessoa (em anos, meses e dias), e escrever a quantidade de horas vividas por ela. Assuma que todo ano tem 365 dias e todo mês tem 30 dias."

    ``` title="Dias vividos"
    Início
        Escreva "Digite quantos anos você tem: "
        Leia [anos].
        Escreva "Digite quantos meses você tem: "
        Leia [meses].
        Escreva "Digite quantos dias você tem: "
        Leia [dias].
        total = ((anos * 365) + (meses * 30) + dias) * 24
        Escreva "Você já viveu [total] horas."
    Fim
    ```
