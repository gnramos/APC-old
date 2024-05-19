### Símbolos

Símbolos são uma forma extremamente versátil de comunicar informações; o [alfabeto](https://pt.wikipedia.org/wiki/Alfabeto) define um pequeno conjunto de símbolos que, juntos, podem expressar [quase](https://pt.wikipedia.org/wiki/Emoticon) tudo que se deseja. Símbolos, como toda informação no computador, são representados por bits.

<h4>ASCII</h4>

O padrão ASCII[@ASCII] (*American Standard Code for Information Interchange*) foi desenvolvido nos anos 60, sendo composto por 95 símbolos gráficos (letras do alfabeto latino, algarismos arábicos, sinais de pontuação e sinais matemáticos) e 33 de controle.

<center>

<h5>Controle</h5>

| bits | Símbolo | bits | Símbolo | bits | Símbolo | bits | Símbolo |
|------|---------|------|---------|------|---------|------|---------|
| 0x00 | NUL     | 0x08 | BS      | 0x10 | DLE     | 0x18 | CAN     |
| 0x01 | SOH     | 0x09 | HT      | 0x11 | DC1     | 0x19 | EM      |
| 0x02 | STX     | 0x0A | LF      | 0x12 | DC2     | ⋮   | ⋮      |
| 0x03 | ETX     | 0x0B | VT      | 0x13 | DC3     | ⋮   | ⋮      |
| 0x04 | EOT     | 0x0C | FF      | 0x14 | DC4     | ⋮   | ⋮      |
| 0x05 | ENQ     | 0x0D | CR      | 0x15 | NAK     | ⋮   | ⋮      |
| 0x06 | ACK     | 0x0E | SO      | 0x16 | SYN     | ⋮   | ⋮      |
| 0x07 | BEL     | 0x0F | SI      | 0x17 | ETB     | 0x7F | DEL     |

<h5>Gráficos (Parcial)</h5>

| bits | Símbolo | bits | Símbolo | bits | Símbolo | bits | Símbolo |
|------|---------|------|---------|------|---------|------|---------|
| 0x20 | espaço  | 0x30 | 0       | 0x41 | A       | 0x61 | a       |
| 0x21 | !       | 0x31 | 1       | 0x42 | B       | 0x62 | b       |
| 0x22 | "       | 0x32 | 2       | 0x43 | C       | 0x63 | c       |
| 0x23 | #       | 0x33 | 3       | 0x44 | D       | 0x64 | d       |
| 0x24 | $       | 0x34 | 4       | 0x45 | E       | 0x65 | e       |
| 0x25 | %       | 0x35 | 5       | ⋮   | ⋮      | ⋮   | ⋮      |
| 0x26 | &       | 0x36 | 6       | 0x57 | W       | 0x77 | w       |
| 0x27 | '       | 0x37 | 7       | 0x58 | X       | 0x78 | x       |
| 0x28 | (       | 0x38 | 8       | 0x59 | Y       | 0x79 | y       |
| 0x29 | )       | 0x39 | 9       | 0x5A | Z       | 0x7A | z       |
| ⋮   | ⋮      | ⋮   | ⋮      | ⋮   | ⋮      | ⋮   | ⋮      |

</center>

Cada um dos 128 símbolos é associado à uma sequência arbitrária e única de 7 de bits. É bem comum associar esta sequência a um número inteiro, por exemplo o número 65 ao símbolo 'A' ("um mesmo conjunto de bits pode ser interpretado de diferentes formas"). Além disso, o padrão ASCII tem algumas características interessantes. Os algarismos são listados em ordem de valor, e as letras são organizadas em ordem alfabética, o que facilita os processos de comparação entre eles. As letras minúsculas estão deslocadas em 32 posições em relação às maiúsculas, então a diferença entre os bits que as representam é apenas no sexto bit!

Por conta de como as máquinas eram construídas, era muito comum usar um byte para armazenar cada símbolo, o que viabilizou definir outros 128 símbolos arbitrários. Entretanto, não houve maior consenso em quais seriam os símbolos, afinal cada grupo tinha seus próprios interesses. No Brasil, o mais comum era o [ISO/IEC 8859-1](https://pt.wikipedia.org/wiki/ISO/IEC_8859-1). Com o avanço da internet, a necessidade de comunicação entre máquinas e grupos distintos forçou a incorporação de um padrão internacional. Entretanto, algumas dificuldades deveriam ser consideradas...

Uma solução "simples" seria usar mais bits e ampliar o tamanho da tabela, mas isso implicaria que toda informação já representada num padrão como ASCII ocuparia mais memória que o necessário. Por exemplo, supondo que fossem usados 3 bytes (possibilitando mais de 16 milhões de símbolos), uma mensagem com 10 símbolos ASCII passa a ocupar 30 bytes, 200% a mais do que necessário. Também seria necessário lidar com informações armazenadas que usam o símbolo `NUL` para indicar o término de uma sequência de símbolos - uma sequência de 8 bits com valor 0 não seria rara considerando 3 bytes. Outro ponto relevante era lidar com os documentos existentes, gerar uma cópia de todo arquivo existente com esta nova codificação seria uma tarefa inviável. A solução encontrada foi uma forma elegante de lidar com tudo isso, além de viabilizar a incorporação de quaisquer novos símbolos que possam ser criados.

<h4>Unicode</h4>

Uma vez estabelecido um padrão de *codificação de caracteres* (associação [arbitrária] de bits a certos caracteres), pode-se armazenar estes símbolos na memória (e recuperá-los). Há diversar formas de se codificar caracteres: [EBCDIC](https://pt.wikipedia.org/wiki/Extended_Binary_Coded_Decimal_Interchange_Code), [Unicode](https://pt.wikipedia.org/wiki/Unicode) (veja [isso](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)), ente outros.

Nesta disciplina, o foco é a representação em [ASCII](https://pt.wikipedia.org/wiki/ASCII), uma forma extremamente compacta e a mais utilizada no padrão ANSI. Neste contexto, um <code>char</code> é um pequeno inteiro, de modo que pode ser livremente usado em expressões aritméticas[@Kernighan1989] (veja \linkFile[../src/exemplos/05_EstruturasDeDados/02_Simbolos]{00-ascii.c} e \linkFile[../src/exemplos/05_EstruturasDeDados/02_Simbolos]{01-ascii.c}).

A versão 3 da \lP~utiliza outra abordagem, cada caractere é representado como [Unicode](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), mas os valores numéricos/simbólicos podem ser utilizados por intermédio das funções [<code>ord](https://docs.python.org/3.3/library/functions.html#ord)</code> e [<code>chr](https://docs.python.org/3.3/library/functions.html#chr)</code>, respectivamente (veja \linkFile[../src/exemplos/05_EstruturasDeDados/02_Simbolos]{00-ascii.py} e \linkFile[../src/exemplos/05_EstruturasDeDados/02_Simbolos]{01-ascii.py}).
\else%
\begin{frame}%
    A *codificação de caracteres* é a associação de bits a símbolos.
    \begin{center}\includegraphics[width=.5\textwidth]{misc/LouisBraille}\end{center}
    \vfill%
    Por necessidade de diálogos entre os diferentes computadores, foram criados
    diversos códigos objetivando a padronização.
\end{frame}%

\begin{frame}<handout:0>%
    \framesubtitle{*Extended Binary Coded Decimal Interchange Code* (EBCDIC)}%
    \begin{center}\includegraphics[width=.75\textwidth]{computing/programming/EBCDIC}\end{center}
\end{frame}%

\begin{frame}<handout:0>%
    \framesubtitle{*American Standard Code for Information Interchange* (ASCII)}%
    \begin{center}\includegraphics[width=.95\textwidth]{computing/programming/ascii}\end{center}
\end{frame}%

\begin{frame}<handout:0>[fragile]%
    \lstC[linerange={9-21}]{exemplos/05_EstruturasDeDados/02_Simbolos}{00-ascii.c}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstPython[firstline=12]{exemplos/05_EstruturasDeDados/02_Simbolos}{00-ascii.py}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstC[linerange={9-21}]{exemplos/05_EstruturasDeDados/02_Simbolos}{01-ascii.c}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstPython[firstline=9]{exemplos/05_EstruturasDeDados/02_Simbolos}{01-ascii.py}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstREADME[lastline=8]{exercicios/05_EstruturasDeDados/02_Simbolos}{00-maior}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstREADME[lastline=8]{exercicios/05_EstruturasDeDados/02_Simbolos}{01-toupper}%
\end{frame}

\begin{frame}<handout:0>%
    \framesubtitle{Unicode}%
    \vspace{-4em}%
    \hfill\includegraphics[width=.2\textwidth]{computing/programming/unicode}%
    \\\vspace{-1em}%
    \begin{itemize}
    \item Padrão universal de codificação de caracteres
    \item Fornece um número único para cada caractere, não importando a plataforma (a máquina e/ou sistema operacional em uso), o programa ou o idioma.
    \item Permite definir caracteres cuja representação interna no computador utiliza mais de um byte (UTF-8), tais como:
    16 bits (UTF-16) e 32 bits (UTF-32).
    \item Atualmente, o padrão consiste de mais de 100 mil caracteres e pode ser usado em vários sistemas operacionais, programas e navegadores modernos.
    \end{itemize}
\end{frame}%
\fi%



## Objetos em Python
\subsection{Ponteiros na \LP}%
\ifIsArticle%
A \lP~não utiliza ponteiros diretamente e, por projeto, manipula objetos de forma diferente de C. Em ambas, os [argumentos são passados por valor](http://stackoverflow.com/a/986145), mas dependendo do tipo de objeto ([mutável/imutável](https://pythonhelp.wordpress.com/2013/02/20/variaveis-valores-e-referencias/)), a manipulação dentro do escopo de uma função tem ou não efeito em um escopo externo.

Primeiro, é preciso lembrar alguns [detalhes da própria linguagem](https://wiki.python.org.br/ProgramacaoOrientadaObjetoPython): os objetos (que ficam na memória) têm os seguintes atributos: *tipo*, que define a informação (e valores) que o objeto pode receber e as operações que podem ser executadas nele; *valor*, que é o endereço de memória ocupado pelo objeto; *nome*, que identifica o objeto diferenciando dos demais elementos na memória; e *tempo de vida*, que é o período de tempo de execução do programa durante o qual o objeto existe. Na \lP{ }lida-se com [referências para objetos](https://pythonhelp.wordpress.com/2013/02/20/variaveis-valores-e-referencias/), as quais desempenham papéis similares a ponteiros.
\fi%

\ifIsArticle%
Os objetos são *imutáveis* (como \texttt{int}, \texttt{float}, \texttt{str}, etc.) ou *mutáveis* (como \texttt{lista}, \texttt{dict}, etc.). Toda variável é, na verdade, uma referência para algum objeto da memória. Considerando objetos imutáveis, como ilustrado na figura abaixo, o valor de nome `*z*' não varia a não ser que você o mude explicitamente, e o operador \texttt{=} não é de *atribuição de valor* (como na \lC), mas de *referência*, e o [coletor de lixo](https://pt.wikipedia.org/wiki/Coletor_de_lixo_(inform%C3%A1tica)) lida com a informação \texttt{42} ao término de seu tempo de vida.
\else%
\begin{frame}[fragile]%
    %https://pythonhelp.wordpress.com/2013/02/20/variaveis-valores-e-referencias/
    Python não utiliza ponteiros como tipos de dados, mas lida com referências de forma ``diferente''...%
    \\\pause\vfill%
    Os objetos em \texttt{Python} são:
    \begin{description}
         \item[imutáveis:] \texttt{int}, \texttt{float}, \texttt{str}, $\dots$
         \item[mutáveis:] \texttt{lista}, $\dots$
     \end{description}
\end{frame}

\begin{frame}%
    Toda variável em \texttt{Python} é uma referência para algum objeto da memória.
    \\\pause\vfill%
    Nesta abordagem para lidar com a memória, o valor de nome `*a*' não varia a não ser que você o mude explicitamente\footnote<2->{*Explícito é melhor que implícito.*}.
\end{frame}
\fi%

\ifIsArticle%
\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.3\textwidth}
        \begin{tikzpicture}[start chain=going right, node distance=0pt, mem/.style={inMemory,text width=2em, minimum height=1.7em}]%
            \node[mem,label={[address,above]0xB1}] (M0) {};%
            \node[mem,label={[address,above]0xB5}] (M1) {42};%
            \node[mem,label={[address,above]0xB9}] (M2) {$\pi$};%
            \node[mem,label={[address,above]0xBD}] (M3) {43};%

            \node[ptr,below of=M0,yshift=-3em] (a) {\textbf{x}};%
            \draw[ptr] (a) -| (M1.south);%
            \node[ptr,below of=a,yshift=-2em] (b) {\textbf{y}};%
            \draw[ptr] (b) -| (M2.south);%
            \node[ptr,below of=b,yshift=-2em] (c) {\textbf{z}};%
            \draw[ptr] (c) -| (M3.south);%
        \end{tikzpicture}%
        \caption{\texttt{x, y, z = 42, $\pi$, 43}}
    \end{subfigure}
    \hspace{4em}%
    \begin{subfigure}[b]{0.3\textwidth}
        \begin{tikzpicture}[start chain=going right, node distance=0pt, mem/.style={inMemory,text width=2em, minimum height=1.7em}]%
            \node[mem,label={[address,above]0xB1}] (M0) {};%
            \node[mem,label={[address,above]0xB5}] (M1) {};%
            \node[mem,label={[address,above]0xB9}] (M2) {$\pi$};%
            \node[mem,label={[address,above]0xBD}] (M3) {43};%

            \node[ptr,below of=M0,yshift=-3em] (a) {\textbf{x}};%
            \draw[ptr] (a) -| (M2.south);%
            \node[ptr,below of=a,yshift=-2em] (b) {\textbf{y}};%
            \draw[ptr] (b) -| (M3.south);%
            \node[ptr,below of=b,yshift=-2em] (c) {\textbf{z}};%
            \draw[ptr] (c) -| (M3.south);%
        \end{tikzpicture}%
        \caption{\texttt{x, y = y, z}}
    \end{subfigure}
\end{figure}
\else%
\begin{frame}[fragile]%
    %https://pythonhelp.wordpress.com/2013/02/20/variaveis-valores-e-referencias/
    O operador \texttt{=} não é de *atribuição*, mas de *referência*.%
    \vfill%
    \begin{columns}
        \column{.7\textwidth}%
            \begin{tikzpicture}[start chain=going right, node distance=0pt, mem/.style={inMemory,text width=2em, minimum height=1.7em}]%
                \node[mem,label={[address,above]0xB1}] (M0) {};%
                \node[mem,label={[address,above]0xB5}] (M1) {\only<2>{42}};%
                \node[mem,label={[address,above]0xB9}] (M2) {\only<5->{$\pi$}};%
                \node[mem,label={[address,above]0xBD}] (M3) {\only<3->{43}};%
                \node[mem,label={[address,above]0xC0}] (M4) {};%

                \node<2->[ptr,below of=M0,yshift=-4em] (a) {\textbf{a}};%
                \draw<2>[ptr] (a) -| (M1.south);%
                \draw<3-4>[ptr] (a) -| (M3.south);%
                \node<4->[ptr,below of=a,yshift=-2em] (b) {\textbf{b}};%
                \draw<4->[ptr] (b) -| (M3.south);%
                \draw<5->[ptr] (a) -| (M2.south);%
            \end{tikzpicture}%
        \column{.2\textwidth}%
            \pause
\begin{lstlisting}[style=CIC-Python]
a = 42
\end{lstlisting}%
\pause\vspace*{-1.1em}%
\begin{lstlisting}[style=CIC-Python,firstnumber=2]
a += 1
\end{lstlisting}%
\pause\vspace*{-1.1em}%
\begin{lstlisting}[style=CIC-Python,firstnumber=3]
b = a
\end{lstlisting}%
\pause\vspace*{-1.1em}%
\begin{lstlisting}[style=CIC-Python,firstnumber=4]
a = 3.14
\end{lstlisting}%
    \end{columns}%
\end{frame}
\fi%

\ifIsArticle%
Na \lP, o conteúdo de uma variável é acessado por seu *nome*, e não é permitida a manipulação direta da memória por um endereço. Isso tem uma série de vantagens (simplifica o uso e evita ) e desvantagens (desempenho). Internamente, o sistema acumula identificadores próprios para cada objeto enquanto durar o seu *tempo de vida* (veja \linkFile[../src/exemplos/05_EstruturasDeDados/03_Ponteiros]{00-identificador.py} e \linkFile[../src/exemplos/05_EstruturasDeDados/03_Ponteiros]{01-identificador.py}).
\else%
\begin{frame}[fragile]
    \lstPython[linerange={9-13,15-23}]{exemplos/05_EstruturasDeDados/03_Ponteiros}{00-identificador.py}%
\end{frame}

\begin{frame}[fragile]
    \lstPython[linerange={9-14,25-32}]{exemplos/05_EstruturasDeDados/03_Ponteiros}{01-identificador.py}%
\end{frame}
\fi%

\ifIsArticle%
A \lP~tem tipo [dinâmico e forte](https://pt.wikipedia.org/wiki/Tipo_de_dado#Tipo_est%C3%A1tico_e_din%C3%A2mico), portanto ao declarar um objeto se sabe, em tempo de execução, o tipo de dado referenciado e como ele é representado na memória.
\else%
\begin{frame}[fragile]%
    Um tipo é *dinâmico e forte* (em tempo de execução, sabe-se o tipo de dado referenciado e como ele é representado na memória).
    \\\vfill%
    \begin{columns}
        \column{.5\textwidth}%
            \begin{tikzpicture}[start chain=going right, node distance=0pt, mem/.style={inMemory,text width=2.5em, minimum height=1.7em}]%
                \node[mem,label={[address,above]0xB1}] (M0) {42};%
                \node[mem,label={[address,above]0xB5},text width=5em] (M1) {\only<2->{Lovelace}};%
                \node[ptr,below of=M0,xshift=-2em,yshift=-3em] (a) {\textbf{x}};%
                \draw<1>[ptr] (a) -| (M0.south);%
                \draw<2->[ptr] (a) -| (M1.south);%
            \end{tikzpicture}%
        \column{.5\textwidth}%
            \begin{lstlisting}[style=CIC-Python]
x = 42
\end{lstlisting}%
            \vspace{-1.1em}\pause%
            \begin{lstlisting}[style=CIC-Python,firstnumber=2]
x = 'Lovelace'
\end{lstlisting}%
    \end{columns}%
\end{frame}
\fi%

\ifIsArticle%
No caso da passagem de informações a funções por argumentos, a \lP~define a variável local como [referência ao valor passado](https://stackoverflow.com/a/986145) (similar a passar a referência para o valor armazenado). A diferença ocorre na questão de qual é o objeto dado, se é *mutável*, a função recebe uma referência para ele e pode alterá-lo (desde que a referência local não seja variada); se é *imutável*, a função não pode alterá-lo.

A comunicação de dados entre [sub]algoritmos é feita pela passagem de argumentos e pelo valor de retorno, e a \lP possibilita o retorno de múltiplos valores.

\noindent%
\lstPython[linerange={9-9,18-24}]{exemplos/05_EstruturasDeDados/03_Ponteiros}{05-bhaskara.py}%
\else%
\begin{frame}[fragile]%
     É possível retornar de múltiplos valores.
    \\\vfill%
    \lstPython[linerange={9-9,18-24}]{exemplos/05_EstruturasDeDados/03_Ponteiros}{05-bhaskara.py}%
\end{frame}
\fi%

\ifIsArticle%
Na \lP, funções também são objetos, e podem ser fornecidas como argumentos para outras funções de forma mais simplificada (comparada a \lC). Um exemplo simples disso é:

\lstPython[linerange={9-19}]{exemplos/05_EstruturasDeDados/03_Ponteiros}{06-funcao.py}%

Da mesma forma, pode-se abstrair o método de aproximação de raízes e passar a função do polinômio (\linkFile[../src/exercicios/05_EstruturasDeDados/03_Ponteiros/01-Newton-Raphson]{Newton-Raphson.py}).
\else%
\subsection{Funções como Argumentos de Funções}%
\begin{frame}<handout:0>[fragile]%

    \lstPython[firstline=9]{exemplos/05_EstruturasDeDados/03_Ponteiros}{06-funcao.py}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \vspace{-1em}%
    \lstPython[linerange={83-83,94-102},morekeywords={valor_inicial,aproxima,erro},escapechar=]{exercicios/05_EstruturasDeDados/03_Ponteiros/01-Newton-Raphson}{Newton-Raphson.py}%
\end{frame}
\fi%

% Os detalhes de ponteiros na \lP{ }não serão aprofundados aqui, mas vale a pena aprender sobre isso.



%     [chamada por compartilhamento](https://pt.wikipedia.org/wiki/Estrat%C3%A9gia_de_avalia%C3%A7%C3%A3o#Chamada_por_compartilhamento)

%     índice negativo
%     https://docs.python.org/3/faq/programming.html#what-s-a-negative-index



%     O comportamento de ``passagem por referência'' pode ser obtido de [outras formas](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference).

% \begin{frame}%

% %%%%%%%%%%%%%%%%%%%
% http://wiki.python.org.br/IntroPython

% Tipos mutáveis e imutáveis

% Alguns tipos no Python permitem que elementos que fazem parte de sua estrutura sejam modificados, como as listas e dicionários. Estes tipos são chamados mutáveis.

% Exemplo:

% Esconder número das linhas

%    1 >>> l = ['Nirvana', 'Rush', 'Bauhaus']
%    2 >>> l[1] = 'Who'
%    3 >>> l
%    4 ['Nirvana', 'Who', 'Bauhaus']
%    5 >>>

% Outros tipos não permitem isso, como tuplas e strings. Estes são chamados imutáveis.


% \end{frame}%

## Strings

\subsection{Strings}%

\ifIsArticle%
Uma *palavra*/*frase* é um conjunto finito e ordenado de símbolos. Um [*string](https://pt.wikipedia.org/wiki/Cadeia_de_caracteres)* é um vetor de caracteres, a ``melhor'' forma de comunicação com humanos.%

\lstset{morekeywords={mostra_indices,mostra_n_chars,mostra_ate_char}}%
\lstC[linerange={10-22}]{exemplos/05_EstruturasDeDados/04_Vetor}{04-string.c}%

O código acima funciona muito bem, mas tem um comportamento interessante quando se digita uma frase menor que os 50 caracteres definidos. Entretanto, forçar a utilização de frases com tamanho fixo [não é uma opção viável](http://www.3minovacao.com.br/blog/os-irao-dominar-o-mundo). A solução de melhor custo/benefício é obter um vetor ``grande o suficiente'' para a tarefa em questão, de modo que haja um tamanho restringindo a aplicação (por exemplo, [140 caracteres](https://pt.wikipedia.org/wiki/Twitter)), e utilizar uma marcação específica para indicar o término dos símbolos de interesse.%

\noindent%
\begin{minipage}[t]{.56\textwidth}%
\lstC[linerange={10-22}]{exemplos/05_EstruturasDeDados/04_Vetor}{05-string.c}%
\end{minipage}%
\hfill%
\begin{minipage}[t]{.44\textwidth}%
\lstC[linerange={10-19}]{exemplos/05_EstruturasDeDados/04_Vetor}{06-string.c}%
\end{minipage}%

<code>`.'</code> não é uma boa escolha de símbolo terminador (afinal, sempre aparece alguém dizendo ``*Hello World!*''), então escolheu-se o símbolo <code>`\textbackslash0'</code> (o primeiro caractere da [tabela ASCII](https://pt.wikipedia.org/wiki/ASCII)) como terminador de um string para representação interna[@Kernighan1989]. Assumindo que *todo string segue este padrão*, pode-se ignorar o tamanho do vetor e simplesmente percorrê-lo até encontrar o caractere de término.%

Algumas ideias interessantes para lidar com strings são: contagem do tamanho de uma palavra, de palavras em um texto, comparação de strings, transformação em letras maiúsculas/minúsculas, [criptografia](https://www.urionlinejudge.com.br/judge/pt/problems/view/1253), etc..

Considere o código abaixo, e veja se percebe o que está errado:
\lstC[linerange={12-16}]{exemplos/05_EstruturasDeDados/04_Vetor}{08-memoria.c}%

<code>scanf</code>\ armazena os caracteres digitados no endereço indicado por \var{buffer}. Como a variável não foi inicializada, não é possível dizer qual é este endereço. Se \var{buffer} é o [caractere nulo](http://pt.wikipedia.org/wiki/Null_%28programa%C3%A7%C3%A3o%29) (\var{NULL}), então <code>scanf</code>\ tentará armazenar os caracteres em um local proibido e a execução do programa será interrompida. Senão, \var{buffer}\ tem um número (que estava já armazenado na memória por algum motivo) que é interpretado como um endereço de memória onde <code>scanf</code>\ tentará armazenar os caracteres. Embora sintaticamente correto, esta é uma ação perigosa pois tal espaço não foi alocado para seu uso, então o programa estará trabalhando em um local que pode estar sendo usado por outro programa e, portanto, que poderia atrapalhar a execução do seu ou, pior ainda, o seu atrapalhar a execução dele (por exemplo, sobrescrevendo um pedaço do arquivo que contém a declaração do imposto de renda).

Uma solução é definir \var{buffer}\ como um vetor (digamos, de tamanho 50). Mas esta solução é parcialmente correta, pois <code>scanf</code>\ continuará escrevendo na memória caso o usuário forneça mais caracteres que o vetor pode armazenar. É necessário, então, limitar a quantidade de caracteres que pode ser considerada:%

\lstC[linerange={33-37}]{exemplos/05_EstruturasDeDados/04_Vetor}{08-memoria.c}%

É importante considerar este tipo de [programação defensiva](http://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_defensiva), pois nunca se sabe o que o usuário vai fazer (nem [como estas vulnerabilidades podem ser exploradas](http://www.lume.ufrgs.br/handle/10183/18550)).

% \begin{lstlisting}
% #include <string.h>

% void f(char *bar) {
%   char c[12];
%   strncpy(c, bar, strlen(bar));
% }

% int main(int argc, char **argv) {
%   f(argv[1]);
% }
% \end{lstlisting}%
%  Potencialmente muito perigoso
\fi%

## Vetores

\section{Vetores}

\ifIsArticle%
É fácil manipular um dado para resolver um problema:%
\begin{lstlisting}
z = min(x, y);
\end{lstlisting}%

Mas e $n$ problemas?
\begin{lstlisting}
z = min(x1, min(x2, min (x3, min(x4, min(x5, /* ... */ min(xk, xn)/* ... */)))));
\end{lstlisting}%
\else%
\begin{frame}[fragile]%
É fácil manipular um dado para resolver um problema:\\\vfill%
\begin{lstlisting}
z = min(x, y);
\end{lstlisting}%
\vfill\pause
Mas e \strikeText{2} \strikeText{3} $n$ problemas?\\\vfill%
\small%
\begin{lstlisting}
z = min(x1, min(x2, min(x3, /* ... */ min(xk,xn)/* ... */)));
\end{lstlisting}%
\end{frame}
\fi%

\ifIsArticle%
Não é factível [considerar escrever tanto código](http://vidadeprogramador.com.br/2014/05/12/treinando-o-alonso/), nem pensar nas dificuldades de eventuais alterações. Felizmente há uma solução mais eficiente. Suponha que você tenha um ponteiro com o endereço de um caractere na memória, e que saiba que os $n$ bytes imediatamente seguintes estão alocados para você armazenar outros caracteres. Você poderia identificá-los como $\{c_0, c_1, \cdots, c_{n-1}\}$ e lidar com estes $n$ elementos no código, ou, dado que sabe o endereço do primeiro, utilizar aritmética de ponteiros para acessar qualquer outro caractere em função do deslocamento em relação a posição inicial.

\begin{minipage}[t]{.52\textwidth}%
\begin{lstlisting}
printf("c0 = %c\n", c0);
printf("c1 = %c\n", c1);
/* ... */
\end{lstlisting}%
\vspace{-1.1em}%
\begin{lstlisting}[firstnumber=1000]
printf("c999 = %c\n", c999); /* n==1000 */
\end{lstlisting}%
\end{minipage}%
\hfill%
\begin{minipage}[t]{.45\textwidth}%
\begin{lstlisting}
for(i = 0; i < n; ++i)
printf("c%d = %c\n", i, *(c+i));
\end{lstlisting}%
\end{minipage}%
\vspace{1em}%
\else%
\begin{frame}[fragile]%
    Mostrar 1000 caracteres não seria agradável...
    \only<2->{Mas suponha eles estão magicamente armazenados sequencialmente, começando em um endereço de memória que você conhece...}
    \\\vfill
\hspace*{.5em}\small%
\begin{minipage}[t]{.45\textwidth}%
\begin{lstlisting}
printf("c0=%c\n", c0);
printf("c1=%c\n", c1);
printf("c2=%c\n", c2);
printf("c3=%c\n", c3);
/* ... */
\end{lstlisting}%
\begin{lstlisting}[firstnumber=997]
/* ... */
printf("c997=%c\n", c997);
printf("c998=%c\n", c998);
printf("c999=%c\n", c999);
\end{lstlisting}%
\end{minipage}%
\pause\pause%
\begin{minipage}[t]{.55\textwidth}%
\begin{lstlisting}
for(i = 0; i < n; ++i)
printf("c%d=%c\n", i, *(c+i));
\end{lstlisting}%
\end{minipage}%
\end{frame}
\fi%

\ifIsArticle%
Um [vetor](https://pt.wikipedia.org/wiki/Arranjo_%28computa%C3%A7%C3%A3o%29) (\texttt{array}) é um conjunto [finito](https://pt.wikipedia.org/wiki/Conjunto_finito) e [ordenado](https://pt.wikipedia.org/wiki/Ordena%C3%A7%C3%A3o_%28%C3%A1lgebra_relacional%29) (em relação a posição) de elementos homogêneos (do mesmo tipo). É um modo particular de organizar dados para facilitar o acesso e manipulação dos dados, caracterizado pelas operações sobre os dados, e não pelo tipo do dado (já que se baseia na aritmética de ponteiros).

Desta forma, é possível ter um vetor de qualquer tipo de dado. Considerando $n$ caracteres, o computador aloca um bloco de memória de $n$ bytes (supondo que um <code>char</code> seja armazenado em 1 byte). Analogamente, supondo $n$ inteiros (de 4 bytes cada), serão alocados $4n$ bytes de memória (que equivalem a $n$ unidades [de memória] de inteiros).

\begin{center}%
    \tikzinput{memoria/vetor/array}%
\end{center}%
\else%
\begin{frame}%
    \begin{block}{Vetor (\texttt{array})}%
        É um conjunto *finito* e *ordenado*\footnote[frame]{Em relação a posição.} de elementos *homogêneos*.
    \end{block}%
    \vfill\pause%
    Quais elementos?%
    \vfill\pause%
    O vetor é um modo particular de organizar dados \pause para facilitar o acesso
    e manipulação dos dados.
    \vfill%
    \begin{center}%
        \tikzinput{memoria/vetor/array}%
    \end{center}%
\end{frame}
\fi%

\ifIsArticle%
Portanto, para lidar com um vetor basta saber duas coisas: o endereço do primeiro elemento e quantos são os elementos armazenados. Na \lC, fica fácil declarar um vetor:

\begin{lstlisting}
int   inteiros[1000];
float reais[50];
char  caracteres[8];
\end{lstlisting}%

Considerando o vetor de caracteres, o que acontece na execução é que o computador armazena o ponteiro para caracteres ($c$) (em algum lugar da memória) e um espaço do tamanho desejado (<code>8*[sizeof](http://www.cprogressivo.net/2013/03/A-funcao-sizeof-e-blocos-vizinhos-de-memoria-em-C.html)(char)</code>) em outro lugar. O acesso a cada elemento, dado o endereço do primeiro, é direto com aritmética de ponteiros ou com o operador <code>[\ \ ]</code>:

\noindent%
\begin{minipage}[t]{.52\textwidth}%
\begin{lstlisting}
for(i = 0; i < n; ++i)
    printf("c%d = %c\n", i, *(c+i));
\end{lstlisting}%
\end{minipage}%
\hfill%
\begin{minipage}[t]{.45\textwidth}%
\begin{lstlisting}
for(i = 0; i < n; ++i)
    printf("c%d = %c\n", i, c[i]);
\end{lstlisting}%
\end{minipage}%

\begin{center}%
\tikzinput{memoria/vetor/lovelace}%
\end{center}%
\else%
\begin{frame}[fragile]%
    Vetor em \texttt{C}: *endereço do primeiro elemento* e *quantidade de elementos*.
    \vfill%
\begin{lstlisting}
int    inteiros[1000];
float     reais[50];
char caracteres[8];
\end{lstlisting}%
\vfill\pause%
\begin{center}%
    \scalebox{.8}{\tikzinput{memoria/vetor/lovelace}}%
\end{center}%
\vfill\pause%
\begin{minipage}[t]{.52\textwidth}%
\begin{lstlisting}
for(i = 0; i < n; ++i)
printf("c%d=%c\n",i,*(c+i));
\end{lstlisting}%
\end{minipage}%
\pause%
\begin{minipage}[t]{.48\textwidth}%
\begin{lstlisting}
for(i = 0; i < n; ++i)
printf("c%d=%c\n",i,c[i]);
\end{lstlisting}%
\end{minipage}%
\vfill\pause
\begin{center}%
RAM + indexação $\Rightarrow$ \alert{velocidade}%
\end{center}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstREADME[lastline=8]{exercicios/05_EstruturasDeDados/04_Vetor}{00-salarios}%
\end{frame}

\titledImageFrame<handout:0>[height=17\baselineskip]{}{comics/VidaDeProgramador/FOR}%
\fi%

\ifIsArticle%
A \lP~tem uma abordagem diferente, no contexto desta disciplina, usaremos [listas](http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_08.html) como vetores[@Downey2002]. Embora a implementação seja distinta, o funcionamento é bastante similar.

\begin{lstlisting}[style=CIC-Python]
inteiros = [0, 1, 2, 3]
reais = [0.0] * 10
caracteres = ['L', 'o', 'v', 'e', 'l', 'a', 'c', 'e']
\end{lstlisting}%
\begin{minipage}[t]{.52\textwidth}%
\begin{lstlisting}[style=CIC-Python]
for i in range(len(inteiros)):
print(inteiros[i])
\end{lstlisting}%
\end{minipage}%
\pause\hfill%
\begin{minipage}[t]{.4\textwidth}%
\begin{lstlisting}[style=CIC-Python]
for c in caracteres:
print(c);
\end{lstlisting}%
\end{minipage}%
\else%
\begin{frame}[fragile]%
    Em \texttt{Python}, o termo que descreve um conjunto de elementos é coleção, e a mais simples é a lista. O funcionamento é similar ao de um vetor em C, mas com uma série de facilidades.
    \vfill%
\begin{lstlisting}[style=CIC-Python]
inteiros = [0, 1, 2, 3]
reais = [0.0] * 10
caracteres = ['L', 'o', 'v', 'e', 'l', 'a', 'c', 'e']
\end{lstlisting}%
\vfill\pause%
\begin{minipage}[t]{.52\textwidth}%
\begin{lstlisting}[style=CIC-Python]
for i in range(len(inteiros)):
print(inteiros[i])
\end{lstlisting}%
\end{minipage}%
\pause\hfill%
\begin{minipage}[t]{.4\textwidth}%
\begin{lstlisting}[style=CIC-Python]
for c in caracteres:
print(c);
\end{lstlisting}%
\end{minipage}%
\end{frame}
\fi%

\ifIsArticle%
O [acesso aos elementos](http://xkcd.com/163/) depende da posição deles em relação ao endereço de início. Dependendo da linguagem, o primeiro elemento tem [índice 0](http://exple.tive.org/blarg/2013/10/22/citation-needed/) (como em C, Java, Python, e Lisp) ou 1 (Fortran, COBOL, e Lua), mas por uma questão de simplicidade e facilidade de uso, a numeração deveria começar em zero[@Dijkstra1982].

O acesso correto aos elementos depende também do tamanho do vetor. Na \lC, os $n$ elementos do vetor estão localizados em um bloco contínuo de bytes (com deslocamento em $[0, n)$, mas a aritmética de ponteiros permite que se acesse outras posições [talvez inválidas] de memória. Por exemplo, considerando a figura, a expressão <code>*(c-1)</code> (equivalente a  <code>c[-1]</code>) é uma expressão sintaticamente correta, e resulta em endereço de memória válido (pois existe), mas é semanticamente incorreta pois acessa um bloco de memória que não foi alocado para o vetor em questão.

\lstC[linerange={10-24}]{exemplos/05_EstruturasDeDados/04_Vetor}{00-vetor.c}%

Na \lP, os $n$ elementos sus podem ser acessados pelo índice correto: $[0, n)$, mas - obviamente - não há aritmética de ponteiros. Entretanto, há certas variações que facilitam a vida. Por exemplo, o uso da função [\fn(len)](http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_08.html#comprimento-da-lista) e o uso de índices negativos para acessar os elementos em ordem inversa. No caso,

\begin{lstlisting}[style=CIC-Python]
lista = [x for x in range(1, 10)]  # lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

len(lista)        # 10
lsita.append(10)  # lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista[0]   # 1
lista[-0]  # 1
lista[-1]  # 10
lista[1:3] # [2, 3]∈

for i in range(1, len(lista) + 1):
print(lista[-i], end=' ')  # Ordem inversa: 10 9 8 7 6 5 4 3 2 1
\end{lstlisting}%
\else%
\begin{frame}%
  Considerações para vetores:
  \begin{itemize}%
  \item *Muito cuidado com os índices utilizados*, use somente $i\in[0,n)$.
  \item Pode não ser preciso ocupar todas as posições do vetor, usar um vetor maior que o necessário muitas vezes facilita a vida...\pause%
  \item Em \lC: *alocação estática de memória*.
  \item Em \lP: *alocação ``dinâmica'' de memória*.
  \end{itemize}%
\end{frame}%

\begin{frame}<handout:0>[fragile]%
    \lstREADME[lastline=6]{exercicios/05_EstruturasDeDados/04_Vetor}{01-medias}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstREADME[lastline=8]{exercicios/05_EstruturasDeDados/04_Vetor}{02-intercalados}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstREADME[lastline=6]{exercicios/05_EstruturasDeDados/04_Vetor}{03-funcoes}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstREADME[lastline=6]{exercicios/05_EstruturasDeDados/04_Vetor}{04-mais_funcoes}%
\end{frame}
\fi%

\ifIsArticle%
[Vetores não são ponteiros](http://eli.thegreenplace.net/2009/10/21/are-pointers-and-arrays-equivalent-in-c), mas na \lC~eles são [praticamente equivalentes](http://c-faq.com/aryptr/aryptrequiv.html), e a relação é tão forte que eles devem ser discutidos juntos[@Kernighan1989]. O vetor é conjunto contíguo de elementos homogêneos pré-alocados com posição e tamanho fixos, já o ponteiro é uma referência para um [tipo específico de] dado qualquer. Um ponteiro é uma variável, então <code>a = p</code> e <code>p++</code> são operações válidas; já um vetor não é uma variável, então <code>a = v</code> e <code>v++</code> *não* são válidas[@VanDerLinden1994].

\lstC[linerange={10-24}]{exemplos/05_EstruturasDeDados/04_Vetor}{01-vetor.c}%

\begin{center}%
\tikzinput{memoria/vetor_ptr}%
\end{center}%
\else%
\begin{frame}%
    \framesubtitle{\LC}%
    Vetores *não são ponteiros*.
    \\\vfill
    \begin{center}%
    \tikzinput{memoria/vetor_ptr}%
    \end{center}%
\end{frame}

\begin{frame}<handout:0>[fragile]%
    \lstC[linerange={10-24}]{exemplos/05_EstruturasDeDados/04_Vetor}{01-vetor.c}%
\end{frame}
\fi%

\ifIsArticle%
Na \lP, listas são objetos *mutáveis*, portanto uma função pode alterar os elementos de uma lista dada como argumento:
\begin{lstlisting}[style=CIC-Python]
def troca_primeiros(lista):
lista[0], lista[1] = lista[1], lista[0]

lista = [x for x in range(1, 10)]
troca_primeiros(lista)
lista  # [2, 1, 3, 4, 5, 6, 7, 8, 9]
\end{lstlisting}%

Na \lC, muito cuidado ao utilizá-los como argumento de funções - a situação de ``equivalência'' pode gerar uma série de problemas.

\noindent%
\begin{minipage}[t]{.5\textwidth}%
\lstC[linerange={14-21}]{exemplos/05_EstruturasDeDados/04_Vetor}{apc_vetor.h}%
\end{minipage}%
\hfill%
\begin{minipage}[t]{.5\textwidth}%
\lstC[linerange={11-21}]{exemplos/05_EstruturasDeDados/04_Vetor}{02-vetor.c}%
\end{minipage}%

Certas aplicações interessantes de vetores exigem que seus elementos estejam [ordenados](https://pt.wikipedia.org/wiki/Ordena%C3%A7%C3%A3o_%28computa%C3%A7%C3%A3o%29) (em relação ao conteúdo). Existem diversas formas de se fazer isso (consegue elaborar um algoritmo de ordenação?), cada uma com certas características. Por exemplo, para ordenar em ordem crescente, pode-se considerar o primeiro elemento e compará-lo com todos os demais, sempre que o primeiro for menor que o comparado, troca-se os conteúdos de posição. Desta forma, ao final de todas as comparações, o elemento na primeira posição será o menor de todos. Então basta repetir este procedimento para cada posição subsequente e, ao final da execução, tem-se o vetor ordenado.%

\begin{lstlisting}[style=CIC-Python]
for i in range(len(vetor) - 1):
for j in range(i + 1, len(vetor)):
    if(vetor[i] > vetor[j])
        vetor[i], vetor[j] = vetor[j], vetor[i]
\end{lstlisting}%

Este simples algoritmo pode ser facilmente adaptado para ordenar o vetor em ordem decrescente. Na verdade, é possível abstrair ainda mais este procedimento com uma função de comparação, que indica uma ordem entre dois elementos. Então, supondo uma função <code>em\_ordem</code>\ que indica se os elementos estão ordenados, o algoritmo pode ser redefinido como:%

\lstC[linerange={16-25}]{exemplos/05_EstruturasDeDados/04_Vetor}{03-vetor.c}%

Assim o algoritmo abstrai a função de comparação, e pode ser usado para realizar ordenações diferentes:

\lstC[linerange={13-14,26-27,33-33,37-37    ,40-42},morekeywords={ordena}]{exemplos/05_EstruturasDeDados/04_Vetor}{03-vetor.c}%

Por fim, a \lC~tem ``declarações complicadas'' (seção 5.12 de \cite{Kernighan1989}), é melhor entender o funcionamento que [tentar] adivinhar o tipo. Por exemplo:

\begin{lstlisting}[style=CIC-C]
char **argv
/* argv: ponteiro para ponteiro para char */

int (* tabdia)[13]
/* tabdia: ponteiro para vetor[13] de int */

int * tabdia[13]
/* tabdia: vetor[13] de ponteiro para int */

void *comp()
/* comp: função retornando ponteiro para void */

void (* comp)()
/* comp: ponteiro para função retornando void */

char (*(*x())[])()
/* x: função retornando ponteiro para vetor[] de ponteiro para função retornando char */

char (*(*x[3])[]())[5]
/* x: vetor[3] de ponteiro para função retornando ponteiro para vetor[5] de char */
\end{lstlisting}%
\fi%



<h2>Exercícios</h2>

??? question "Considerando 4 bits para armazenar um número real como ponto fixo, determine qual a representação do valor $1,25_{10}$ como $Q1.3$, $Q2.2$ e $Q3.1$. "

    * $Q1.3 \Rightarrow 1,25_{10} = 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} + 0\cdot2^{-3} = 1010_2$
    * $Q2.2 \Rightarrow 1,25_{10} = 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} = 0101_2$
    * $Q3.1$ não é adequado para este valor. Tem-se duas possibilidades:
        * $1,25_{10} \approx 0\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} = 0001_2 (=1,5_{10})$
        * $1,25_{10} \approx 0\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 0\cdot2^{-2} = 0010_2 (=1,0_{10})$
