# Condicional

exemplo do imc (implicações matemáticas de se não é < x, necessariamente é >= x)

``` python title="Índice de Massa Corporal"
--8<-- "imc.py:5:16"
```

https://realpython.com/python-conditional-statements/#introduction-to-the-if-statement

https://realpython.com/python-boolean/


Working With Boolean Logic in Python
Back in 1854, George Boole authored The Laws of Thought, which contains what’s known as Boolean algebra. This algebra relies on two values: true and false. It also defines a set of Boolean operations, also known as logical operations, denoted by the generic operators AND, OR, and NOT.

These Boolean values and operators are pretty helpful in programming. For example, you can construct arbitrarily complex Boolean expressions with the operators and determine their resulting truth value as true or false. You can use the truth value of Boolean expressions to decide the course of action of your programs.

In Python, the Boolean type bool is a subclass of int and can take the values True or False:


Using Python’s and Operator in Boolean Contexts
Like all of Python’s Boolean operators, the and operator is especially useful in Boolean contexts. Boolean contexts are where you’ll find most of the real-world use cases of Boolean operators.

Two main structures define Boolean contexts in Python:

if statements let you perform conditional execution and take different courses of action based on the result of some initial conditions.
while loops let you perform conditional iteration and run repetitive tasks while a given condition is true.
These two structures are part of what you’d call control flow statements. They help you decide your programs’ execution path.

You can use Python’s and operator to construct compound Boolean expressions in both if statements and while loops.


if Statements
Boolean expressions are commonly known as conditions because they typically imply the need for meeting a given requirement. They’re pretty useful in the context of conditional statements. In Python, this type of statement starts with the if keyword and continues with a condition. A conditional statement can additionally include elif and else clauses.

Python conditional statements follow the logic of conditionals in English grammar. If the condition is true, then the if code block executes. Otherwise, the execution jumps to a different code block:

>>>
>>> a = -8

>>> if a < 0:
...     print("a is negative")
... elif a > 0:
...     print("a is positive")
... else:
...     print("a is equal to 0")
...
a is negative
Since a holds a negative number, the condition a < 0 is true. The if code block runs, and you get the message a is negative printed on your screen. If you change the value of a to a positive number, however, then the elif block runs and Python prints a is positive. Finally, if you set a to zero, then the else code block executes. Go ahead and play with a to see what happens!

Now say you want to make sure that two conditions are met—meaning that they’re both true—before running a certain piece of code. To try this out, suppose you need to get the age of a user running your script, process that information, and display to the user their current life stage.

Fire up your favorite code editor or IDE and create the following script:

# age.py

age = int(input("Enter your age: "))

if age >= 0 and age <= 9:
    print("You are a child!")
elif age > 9 and age <= 18:
    print("You are an adolescent!")
elif age > 18 and age <= 65:
    print("You are an adult!")
elif age > 65:
    print("Golden ages!")
Here, you get the user’s age using input() and then convert it to an integer number with int(). The if clause checks if age is greater than or equal to 0. In the same clause, it checks if age is less than or equal to 9. To do this, you build an and compound Boolean expression.

The three elif clauses check other intervals to determine the life stage associated with the user’s age.

If you run this script from your command line, then you get something like this:

$ python age.py
Enter your age: 25
You are an adult!
Depending on the age you enter at the command line, the script takes one course of action or another. In this specific example, you provide an age of 25 years and get the message You are an adult! printed to your screen.


sing Python’s and Operator in Non-Boolean Contexts
The fact that and can return objects besides just True and False is an interesting feature. For example, this feature allows you to use the and operator for conditional execution. Say you need to update a flag variable if the first item in a given list is equal to a certain expected value. For this situation, you can use a conditional statement:

>>>
>>> a_list = ["expected value", "other value"]
>>> flag = False

>>> if len(a_list) > 0 and a_list[0] == "expected value":
...     flag = True
...

>>> flag
True
Here, the conditional checks if the list has at least one item. If so, it checks if the first item in the list is equal to the "expected value" string. If both checks pass, then flag changes to True. You can simplify this code by taking advantage of the and operator:

>>>
>>> a_list = ["expected value", "other value"]
>>> flag = False

>>> flag = len(a_list) > 0 and a_list[0] == "expected value"

>>> flag
True
In this example, the highlighted line does all the work. It checks both conditions and makes the corresponding assignment in one go. This expression takes the and operator out of the if statement you used in the previous example, which means that you’re not working in a Boolean context any longer.

The code in the example above is more concise than the equivalent conditional statement you saw before, but it’s less readable. To properly understand this expression, you’d need to be aware of how the and operator works internally.

Putting Python’s and Operator Into Action
So far, you’ve learned how to use Python’s and operator for creating compound Boolean expressions and non-Boolean expressions. You’ve also learned how to use this logical operator in Boolean contexts like if statements and while loops.

In this section, you’ll build a few practical examples that’ll help you decide when to use the and operator. With these examples, you’ll learn how to take advantage of and for writing better and more Pythonic code.

Flattening Nested if Statements
One principle from the Zen of Python states that “Flat is better than nested.” For example, while code that has two levels of nested if statements is normal and totally okay, your code really starts to look messy and complicated when you have more than two levels of nesting.

Say you need to test if a given number is positive. Then, once you confirm that it’s positive, you need to check if the number is lower than a given positive value. If it is, you can proceed with a specific calculation using the number at hand:

>>>
>>> number = 7

>>> if number > 0:
...     if number < 10:
...         # Do some calculation with number...
...         print("Calculation done!")
...
Calculation done!
Cool! These two nested if statements solve your problem. You first check if the number is positive and then check if it’s lower than 10. In this small example, the call to print() is a placeholder for your specific calculation, which runs only if both conditions are true.

Even though the code works, it’d be nice to make it more Pythonic by removing the nested if. How can you do that? Well, you can use the and operator to combine both conditions in a single compound condition:

>>>
>>> number = 7

>>> if number > 0 and number < 10:
...     # Do some calculation with number...
...     print("Calculation done!")
...
Calculation done!
Logical operators like the and operator often provide an effective way to improve your code by removing nested conditional statements. Take advantage of them whenever possible.

In this specific example, you use and to create a compound expression that checks if a number is in a given range or interval. Python provides an even better way to perform this check by chaining expressions. For example, you can write the condition above as 0 < number < 10. That’s a topic for the following section.

Checking Numeric Ranges
With a close look at the example in the section below, you can conclude that Python’s and operator is a convenient tool for checking if a specific numeric value is inside a given interval or range. For example, the following expressions check if a number x is between 0 and 10, both inclusive:

>>>
>>> x = 5
>>> x >= 0 and x <= 10
True

>>> x = 20
>>> x >= 0 and x <= 10
False
In the first expression, the and operator first checks if x is greater than or equal to 0. Since the condition is true, the and operator checks if x is lower than or equal to 10. The final result is true because the second condition is also true. This means that the number is within the desired interval.

In the second example, the first condition is true, but the second is false. The general result is false, which means the number isn’t in the target interval.

You can enclose this logic in a function and make it reusable:

>>>
>>> def is_between(number, start=0, end=10):
...     return number >= start and number <= end
...

>>> is_between(5)
True
>>> is_between(20)
False

>>> is_between(20, 10, 40)
True
In this example, is_between() takes number as an argument. It also takes start and end, which define the target interval. Note that these arguments have default argument values, which means they’re optional arguments.

Your is_between() function returns the result of evaluating an and expression that checks if number is between start and end, both inclusive.

Note: Unintentionally writing and expressions that always return False is a common mistake. Suppose you want to write an expression that excludes values between 0 and 10 from a given computation.

To achieve this result, you start with two Boolean expressions:

number < 0
number > 10
With these two expressions as a starting point, you think of using and to combine them in a single compound expression. However, no number is lower than 0 and greater than 10 at the same time, so you end up with an always-false condition:

>>>
>>> for number in range(-100, 100):
...     included = number < 0 and number > 10
...     print(f"Is {number} included?", included)
...
Is -100 included? False
Is -99 included? False

...

Is 0 included? False
Is 1 included? False

...

Is 98 included? False
Is 99 included? False
In this case, and is the wrong logical operator to approach the problem at hand. You should use the or operator instead. Go ahead and give it a try!

Even though using the and operator allows you to check gracefully if a number is within a given interval, there’s a more Pythonic technique to approach the same problem. In mathematics, you can write 0 < x < 10 to denote that x is between 0 and 10.

In most programming languages, this expression doesn’t make sense. In Python, however, the expression works like a charm:

>>>
>>> x = 5
>>> 0 < x < 10
True

>>> x = 20
>>> 0 < x < 10
False
In a different programming language, this expression would start by evaluating 0 < x, which is true. The next step would be to compare the true Boolean with 10, which doesn’t make much sense, so the expression fails. In Python, something different happens.

Python internally rewrites this type of expression to an equivalent and expression, such as x > 0 and x < 10. It then performs the actual evaluation. That’s why you get the correct result in the example above.

Just like you can chain several subexpressions with multiple and operators, you can also chain them without explicitly using any and operators:

>>>
>>> x = 5
>>> y = 15

>>> 0 < x < 10 < y < 20
True

>>> # Equivalent and expression
>>> 0 < x and x < 10 and 10 < y and y < 20
True
You can also use this Python trick to check if several values are equal:

>>>
>>> x = 10
>>> y = 10
>>> z = 10

>>> x == y == z
True

>>> # Equivalent and expression
>>> x == y and y == z
True
Chained comparison expressions are a nice feature, and you can write them in various ways. However, you should be careful. In some cases, the final expression can be challenging to read and understand, especially for programmers coming from languages in which this feature isn’t available.



Python’s and operator allows you to construct compound Boolean expressions that you can use to decide the course of action of your programs. You can use the and operator to solve several problems both in Boolean or non-Boolean contexts. Learning about how to use the and operator properly can help you write more Pythonic code.

In this tutorial, you learned how to:

Work with Python’s and operator
Build Boolean and non-Boolean expressions with Python’s and operator
Decide the course of action of your programs using the and operator in Boolean contexts
Make your code more concise using the and operator in non-Boolean contexts
Going through the practical examples in this tutorial can help you get a general idea of how to use the and operator to make decisions in your Python code.




O uso de condicionais é baseado no valores booleanos $verdadeiro$ e $falso$. Estes são os valores verdade da lógica matemática, e indicam o grau de verdade de uma proposição. Por exemplo, considerando os números inteiros 42 e 100, podemos a propor que $42 < 100$ e verificar que isto é verdadeiro.
As linguagens de programação podem oferecer um tipo de dado específico para estes valores ou interpretar outros tipos de dados como um dos dois resultados possíveis. Por exemplo, a linguagem C não tem um tipo primitivo e interpreta o valor numérico zero como o valor booleano $falso$, e qualquer valor diferente disso como $verdadeiro$. Já Python tem o tipo [bool](https://docs.python.org/pt-br/3/c-api/bool.html), mas também interpreta uma série de outros tipos de dados.

`<expr>` é uma expressão cujo valor resultante tem um significado booleano, ou seja, é **verdadeiro** ou **falso**.


https://realpython.com/python-boolean/
 Logical Operators in the Operators and Expressions in Python tutorial.
<statement> is a valid Python statement, which must be indented. (You will see why very soon.)
If <expr> is true (evaluates to a value that is “truthy”), then <statement> is executed. If <expr> is false, then <statement> is skipped over and not executed.

Note that the colon (:) following <expr> is required. Some programming languages require <expr> to be enclosed in parentheses, but Python does not.

Here are several examples of this type of if statement:



=== "Python"

    ``` python title="Estrutura condicional"
    if <expr>:
    	<instr>
    ```

=== "C"

    ``` C title="Estrutura condicional"
    if (<expr>) {
    	<instr>;
    }
    ```

<h2>Exercícios</h2>

https://realpython.com/quizzes/python-conditional-statements/viewer/

In a Python program, a control structure:

Defines program-specific data structures
Manages the input and output of control characters
Dictates what happens before the program starts and after it terminates
* Directs the order of execution of the statements in the program

Control structures determine which statements in the program will be executed and in what order, allowing for statements to be skipped over or executed repeatedly.

if, if/else, and if/elif/else statements are all examples of control structures that allow for statements to be skipped over or executed conditionally:

if <expr>:
    <statement>

if <expr>:
    <statement(s)>
else:
    <statement(s)>

if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>
The order of execution of statements in a program is called control flow.