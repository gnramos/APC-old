## Automação

O uso de mecanismos para realização de um processo específico tem uma série de vantagens. Provavelmente aumenta a eficiência na produção dos resultados e a uniformidade destes, reduz a incidência de erros e viabiliza o recurso humano para lidar com outras atividades. Além disso, muitas tarefas cotidianas são repetitivas e poderiam ser realizadas por um computador dadas as instruções corretas[@Sweigart2020].

Parte importante deste processo é o entendimento do que pode ser computado e também do que não pode ser. O computador existe como entidade física e opera dentro de certos limites. Portanto, apesar de podermos planejar soluções matematicamente corretas, é possível que estas não possam ser executadas na máquina. Por exemplo, há [métodos para calcular o valor exato de π](https://pt.wikipedia.org/wiki/Pi#M%C3%A9todos_de_s%C3%A9ries_infinitas), mas o resultado é um valor irracional e o processo para calcular o valor exato também é infinitamente demorado!

$$\pi = 4\cdot\sum\limits_{n=0}^{\infty}\frac{(-1)^n}{2n+1}$$

Além disso, certas operações podem demandar que uma quantidade inviável de informações seja armazenada, ou que sejam realizados tantos processos que se torna impraticável aguardar o término da computação (se ocorrer). O processo de formulação de uma solução algorítmica necessariamente deve considerar essas limitações de modo a chegar a uma opção que seja realizável.

Outro aspecto relevante neste processo é que, para ser realizada por um computador, a tarefa e deve ser programada de tal modo que os padrões de interação envolvidos escondam, mas não retirem os detalhes do contexto. Em Ciência da Computação, essa abstração é o processo de eliminar especificidades ao ignorar certas características e de esconder informações que não sejam necessárias[@Colburn2007], o que permite que os padrões de interações entre processos sejam aplicáveis em diversos contextos.
