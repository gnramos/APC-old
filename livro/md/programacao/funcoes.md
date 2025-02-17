# Funções

Here’s what you’ll learn in this tutorial:

How functions work in Python and why they’re beneficial
How to define and call your own Python function
Mechanisms for passing arguments to your function
How to return data from your function back to the calling environment
Free PDF Download: Python 3 Cheat Sheet

Functions in Python
You may be familiar with the mathematical concept of a function. A function is a relationship or mapping between one or more inputs and a set of outputs. In mathematics, a function is typically represented like this:

mathematical function
Here, f is a function that operates on the inputs x and y. The output of the function is z. However, programming functions are much more generalized and versatile than this mathematical definition. In fact, appropriate function definition and use is so critical to proper software development that virtually all modern programming languages support both built-in and user-defined functions.

In programming, a function is a self-contained block of code that encapsulates a specific task or related group of tasks. In previous tutorials in this series, you’ve been introduced to some of the built-in functions provided by Python. id(), for example, takes one argument and returns that object’s unique integer identifier:

>>>
>>> s = 'foobar'
>>> id(s)
56313440
len() returns the length of the argument passed to it:

>>>
>>> a = ['foo', 'bar', 'baz', 'qux']
>>> len(a)
4
any() takes an iterable as its argument and returns True if any of the items in the iterable are truthy and False otherwise:

>>>
>>> any([False, False, False])
False
>>> any([False, True, False])
True

>>> any(['bar' == 'baz', len('foo') == 4, 'qux' in {'foo', 'bar', 'baz'}])
False
>>> any(['bar' == 'baz', len('foo') == 3, 'qux' in {'foo', 'bar', 'baz'}])
True
Each of these built-in functions performs a specific task. The code that accomplishes the task is defined somewhere, but you don’t need to know where or even how the code works. All you need to know about is the function’s interface:

What arguments (if any) it takes
What values (if any) it returns
Then you call the function and pass the appropriate arguments. Program execution goes off to the designated body of code and does its useful thing. When the function is finished, execution returns to your code where it left off. The function may or may not return data for your code to use, as the examples above do.

When you define your own Python function, it works just the same. From somewhere in your code, you’ll call your Python function and program execution will transfer to the body of code that makes up the function.

Note: In this case, you will know where the code is and exactly how it works because you wrote it!

When the function is finished, execution returns to the location where the function was called. Depending on how you designed the function’s interface, data may be passed in when the function is called, and return values may be passed back when it finishes.

Virtually all programming languages used today support a form of user-defined functions, although they aren’t always called functions. In other languages, you may see them referred to as one of the following:

Subroutines
Procedures
Methods
Subprograms
So, why bother defining functions? There are several very good reasons. Let’s go over a few now.

Abstraction and Reusability
Suppose you write some code that does something useful. As you continue development, you find that the task performed by that code is one you need often, in many different locations within your application. What should you do? Well, you could just replicate the code over and over again, using your editor’s copy-and-paste capability.

Later on, you’ll probably decide that the code in question needs to be modified. You’ll either find something wrong with it that needs to be fixed, or you’ll want to enhance it in some way. If copies of the code are scattered all over your application, then you’ll need to make the necessary changes in every location.

Note: At first blush, that may seem like a reasonable solution, but in the long term, it’s likely to be a maintenance nightmare! While your code editor may help by providing a search-and-replace function, this method is error-prone, and you could easily introduce bugs into your code that will be difficult to find.

A better solution is to define a Python function that performs the task. Anywhere in your application that you need to accomplish the task, you simply call the function. Down the line, if you decide to change how it works, then you only need to change the code in one location, which is the place where the function is defined. The changes will automatically be picked up anywhere the function is called.

The abstraction of functionality into a function definition is an example of the Don’t Repeat Yourself (DRY) Principle of software development. This is arguably the strongest motivation for using functions.

Modularity
Functions allow complex processes to be broken up into smaller steps. Imagine, for example, that you have a program that reads in a file, processes the file contents, and then writes an output file. Your code could look like this:

# Main program

# Code to read file in
<statement>
<statement>
<statement>
<statement>

# Code to process file
<statement>
<statement>
<statement>
<statement>

# Code to write file out
<statement>
<statement>
<statement>
<statement>
In this example, the main program is a bunch of code strung together in a long sequence, with whitespace and comments to help organize it. However, if the code were to get much lengthier and more complex, then you’d have an increasingly difficult time wrapping your head around it.

Alternatively, you could structure the code more like the following:

def read_file():
    # Code to read file in
    <statement>
    <statement>
    <statement>
    <statement>

def process_file():
    # Code to process file
    <statement>
    <statement>
    <statement>
    <statement>

def write_file():
    # Code to write file out
    <statement>
    <statement>
    <statement>
    <statement>


# Main program
read_file()
process_file()
write_file()
This example is modularized. Instead of all the code being strung together, it’s broken out into separate functions, each of which focuses on a specific task. Those tasks are read, process, and write. The main program now simply needs to call each of these in turn.

Note: The def keyword introduces a new Python function definition. You’ll learn all about this very soon.

In life, you do this sort of thing all the time, even if you don’t explicitly think of it that way. If you wanted to move some shelves full of stuff from one side of your garage to the other, then you hopefully wouldn’t just stand there and aimlessly think, “Oh, geez. I need to move all that stuff over there! How do I do that???” You’d divide the job into manageable steps:

Take all the stuff off the shelves.
Take the shelves apart.
Carry the shelf parts across the garage to the new location.
Re-assemble the shelves.
Carry the stuff across the garage.
Put the stuff back on the shelves.
Breaking a large task into smaller, bite-sized sub-tasks helps make the large task easier to think about and manage. As programs become more complicated, it becomes increasingly beneficial to modularize them in this way.

Namespace Separation
A namespace is a region of a program in which identifiers have meaning. As you’ll see below, when a Python function is called, a new namespace is created for that function, one that is distinct from all other namespaces that already exist.

The practical upshot of this is that variables can be defined and used within a Python function even if they have the same name as variables defined in other functions or in the main program. In these cases, there will be no confusion or interference because they’re kept in separate namespaces.

This means that when you write code within a function, you can use variable names and identifiers without worrying about whether they’re already used elsewhere outside the function. This helps minimize errors in code considerably.

Note: You’ll learn much more about namespaces later in this series.

Hopefully, you’re sufficiently convinced of the virtues of functions and eager to create some! Let’s see how.

Function Calls and Definition
The usual syntax for defining a Python function is as follows:

def <function_name>([<parameters>]):
    <statement(s)>
The components of the definition are explained in the table below:

Component	Meaning
def	The keyword that informs Python that a function is being defined
<function_name>	A valid Python identifier that names the function
<parameters>	An optional, comma-separated list of parameters that may be passed to the function
:	Punctuation that denotes the end of the Python function header (the name and parameter list)
<statement(s)>	A block of valid Python statements
The final item, <statement(s)>, is called the body of the function. The body is a block of statements that will be executed when the function is called. The body of a Python function is defined by indentation in accordance with the off-side rule. This is the same as code blocks associated with a control structure, like an if or while statement.

The syntax for calling a Python function is as follows:

<function_name>([<arguments>])
<arguments> are the values passed into the function. They correspond to the <parameters> in the Python function definition. You can define a function that doesn’t take any arguments, but the parentheses are still required. Both a function definition and a function call must always include parentheses, even if they’re empty.

As usual, you’ll start with a small example and add complexity from there. Keeping the time-honored mathematical tradition in mind, you’ll call your first Python function f(). Here’s a script file, foo.py, that defines and calls f():

 1def f():
 2    s = '-- Inside f()'
 3    print(s)
 4
 5print('Before calling f()')
 6f()
 7print('After calling f()')
Here’s how this code works:

Line 1 uses the def keyword to indicate that a function is being defined. Execution of the def statement merely creates the definition of f(). All the following lines that are indented (lines 2 to 3) become part of the body of f() and are stored as its definition, but they aren’t executed yet.

Line 4 is a bit of whitespace between the function definition and the first line of the main program. While it isn’t syntactically necessary, it is nice to have. To learn more about whitespace around top-level Python function definitions, check out Writing Beautiful Pythonic Code With PEP 8.

Line 5 is the first statement that isn’t indented because it isn’t a part of the definition of f(). It’s the start of the main program. When the main program executes, this statement is executed first.

Line 6 is a call to f(). Note that empty parentheses are always required in both a function definition and a function call, even when there are no parameters or arguments. Execution proceeds to f() and the statements in the body of f() are executed.

Line 7 is the next line to execute once the body of f() has finished. Execution returns to this print() statement.

The sequence of execution (or control flow) for foo.py is shown in the following diagram:

When foo.py is run from a Windows command prompt, the result is as follows:

C:\Users\john\Documents\Python\doc>python foo.py
Before calling f()
-- Inside f()
After calling f()
Occasionally, you may want to define an empty function that does nothing. This is referred to as a stub, which is usually a temporary placeholder for a Python function that will be fully implemented at a later time. Just as a block in a control structure can’t be empty, neither can the body of a function. To define a stub function, use the passstatement:

>>>
>>> def f():
...     pass
...
>>> f()
As you can see above, a call to a stub function is syntactically valid but doesn’t do anything.

Argument Passing
So far in this tutorial, the functions you’ve defined haven’t taken any arguments. That can sometimes be useful, and you’ll occasionally write such functions. More often, though, you’ll want to pass data into a function so that its behavior can vary from one invocation to the next. Let’s see how to do that.

Positional Arguments
The most straightforward way to pass arguments to a Python function is with positional arguments (also called required arguments). In the function definition, you specify a comma-separated list of parameters inside the parentheses:

>>>
>>> def f(qty, item, price):
...     print(f'{qty} {item} cost ${price:.2f}')
...
When the function is called, you specify a corresponding list of arguments:

>>>
>>> f(6, 'bananas', 1.74)
6 bananas cost $1.74
The parameters (qty, item, and price) behave like variables that are defined locally to the function. When the function is called, the arguments that are passed (6, 'bananas', and 1.74) are bound to the parameters in order, as though by variable assignment:

Parameter		Argument
qty	←	6
item	←	bananas
price	←	1.74
In some programming texts, the parameters given in the function definition are referred to as formal parameters, and the arguments in the function call are referred to as actual parameters:

Difference between parameters and arguments
Although positional arguments are the most straightforward way to pass data to a function, they also afford the least flexibility. For starters, the order of the arguments in the call must match the order of the parameters in the definition. There’s nothing to stop you from specifying positional arguments out of order, of course:

>>>
>>> f('bananas', 1.74, 6)
bananas 1.74 cost $6.00
The function may even still run, as it did in the example above, but it’s very unlikely to produce the correct results. It’s the responsibility of the programmer who defines the function to document what the appropriate arguments should be, and it’s the responsibility of the user of the function to be aware of that information and abide by it.

With positional arguments, the arguments in the call and the parameters in the definition must agree not only in order but in number as well. That’s the reason positional arguments are also referred to as required arguments. You can’t leave any out when calling the function:

>>>
>>> # Too few arguments
>>> f(6, 'bananas')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    f(6, 'bananas')
TypeError: f() missing 1 required positional argument: 'price'
Nor can you specify extra ones:

>>>
>>> # Too many arguments
>>> f(6, 'bananas', 1.74, 'kumquats')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    f(6, 'bananas', 1.74, 'kumquats')
TypeError: f() takes 3 positional arguments but 4 were given
Positional arguments are conceptually straightforward to use, but they’re not very forgiving. You must specify the same number of arguments in the function call as there are parameters in the definition, and in exactly the same order. In the sections that follow, you’ll see some argument-passing techniques that relax these restrictions.

Keyword Arguments
When you’re calling a function, you can specify arguments in the form <keyword>=<value>. In that case, each <keyword> must match a parameter in the Python function definition. For example, the previously defined function f() may be called with keyword arguments as follows:

>>>
>>> f(qty=6, item='bananas', price=1.74)
6 bananas cost $1.74
Referencing a keyword that doesn’t match any of the declared parameters generates an exception:

>>>
>>> f(qty=6, item='bananas', cost=1.74)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module&ggt;
TypeError: f() got an unexpected keyword argument 'cost'
Using keyword arguments lifts the restriction on argument order. Each keyword argument explicitly designates a specific parameter by name, so you can specify them in any order and Python will still know which argument goes with which parameter:

>>>
>>> f(item='bananas', price=1.74, qty=6)
6 bananas cost $1.74
Like with positional arguments, though, the number of arguments and parameters must still match:

>>>
>>> # Still too few arguments
>>> f(qty=6, item='bananas')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f(qty=6, item='bananas')
TypeError: f() missing 1 required positional argument: 'price'
So, keyword arguments allow flexibility in the order that function arguments are specified, but the number of arguments is still rigid.

You can call a function using both positional and keyword arguments:

>>>
>>> f(6, price=1.74, item='bananas')
6 bananas cost $1.74

>>> f(6, 'bananas', price=1.74)
6 bananas cost $1.74
When positional and keyword arguments are both present, all the positional arguments must come first:

>>>
>>> f(6, item='bananas', 1.74)
SyntaxError: positional argument follows keyword argument
Once you’ve specified a keyword argument, there can’t be any positional arguments to the right of it.

Default Parameters
If a parameter specified in a Python function definition has the form <name>=<value>, then <value> becomes a default value for that parameter. Parameters defined this way are referred to as default or optional parameters. An example of a function definition with default parameters is shown below:

>>>
>>> def f(qty=6, item='bananas', price=1.74):
...     print(f'{qty} {item} cost ${price:.2f}')
...
When this version of f() is called, any argument that’s left out assumes its default value:

>>>
>>> f(4, 'apples', 2.24)
4 apples cost $2.24
>>> f(4, 'apples')
4 apples cost $1.74

>>> f(4)
4 bananas cost $1.74
>>> f()
6 bananas cost $1.74

>>> f(item='kumquats', qty=9)
9 kumquats cost $1.74
>>> f(price=2.29)
6 bananas cost $2.29
In summary:

Positional arguments must agree in order and number with the parameters declared in the function definition.
Keyword arguments must agree with declared parameters in number, but they may be specified in arbitrary order.
Default parameters allow some arguments to be omitted when the function is called.
Mutable Default Parameter Values
Things can get weird if you specify a default parameter value that is a mutable object. Consider this Python function definition:

>>>
>>> def f(my_list=[]):
...     my_list.append('###')
...     return my_list
...
f() takes a single list parameter, appends the string '###' to the end of the list, and returns the result:

>>>
>>> f(['foo', 'bar', 'baz'])
['foo', 'bar', 'baz', '###']

>>> f([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5, '###']
The default value for parameter my_list is the empty list, so if f() is called without any arguments, then the return value is a list with the single element '###':

>>>
>>> f()
['###']
Everything makes sense so far. Now, what would you expect to happen if f() is called without any parameters a second and a third time? Let’s see:

>>>
>>> f()
['###', '###']
>>> f()
['###', '###', '###']
Oops! You might have expected each subsequent call to also return the singleton list ['###'], just like the first. Instead, the return value keeps growing. What happened?

In Python, default parameter values are defined only once when the function is defined (that is, when the def statement is executed). The default value isn’t re-defined each time the function is called. Thus, each time you call f() without a parameter, you’re performing .append() on the same list.

You can demonstrate this with id():

>>>
>>> def f(my_list=[]):
...     print(id(my_list))
...     my_list.append('###')
...     return my_list
...
>>> f()
140095566958408
['###']
>>> f()
140095566958408
['###', '###']
>>> f()
140095566958408
['###', '###', '###']
The object identifier displayed confirms that, when my_list is allowed to default, the value is the same object with each call. Since lists are mutable, each subsequent .append() call causes the list to get longer. This is a common and pretty well-documented pitfall when you’re using a mutable object as a parameter’s default value. It potentially leads to confusing code behavior, and is probably best avoided.

As a workaround, consider using a default argument value that signals no argument has been specified. Most any value would work, but None is a common choice. When the sentinel value indicates no argument is given, create a new empty list inside the function:

>>>
>>> def f(my_list=None):
...     if my_list is None:
...         my_list = []
...     my_list.append('###')
...     return my_list
...

>>> f()
['###']
>>> f()
['###']
>>> f()
['###']

>>> f(['foo', 'bar', 'baz'])
['foo', 'bar', 'baz', '###']

>>> f([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5, '###']
Note how this ensures that my_list now truly defaults to an empty list whenever f() is called without an argument.

Pass-By-Value vs Pass-By-Reference in Pascal
In programming language design, there are two common paradigms for passing an argument to a function:

Pass-by-value: A copy of the argument is passed to the function.
Pass-by-reference: A reference to the argument is passed to the function.
Other mechanisms exist, but they are essentially variations on these two. In this section, you’re going to take a short detour from Python and briefly look at Pascal, a programming language that makes a particularly clear distinction between these two.

Note: Don’t worry if you aren’t familiar with Pascal! The concepts are similar to those of Python, and the examples shown are accompanied by enough detailed explanation that you should get a general idea. Once you’ve seen how argument passing works in Pascal, we’ll circle back around to Python, and you’ll see how it compares.

Here’s what you need to know about Pascal syntax:

Procedures: A procedure in Pascal is similar to a Python function.
Colon-equals: This operator (:=) is used for assignment in Pascal. It’s analogous to the equals sign (=) in Python.
writeln(): This function displays data to the console, similar to Python’s print().
With that bit of groundwork in place, here’s the first Pascal example:

 1// Pascal Example #1
 2
 3procedure f(fx : integer);
 4begin
 5    writeln('Start  f():  fx = ', fx);
 6    fx := 10;
 7    writeln('End    f():  fx = ', fx);
 8end;
 9
10// Main program
11var
12    x : integer;
13
14begin
15    x := 5;
16    writeln('Before f():  x = ', x);
17    f(x);
18    writeln('After  f():  x = ', x);
19end.
Here’s what’s going on:

Line 12: The main program defines an integer variable x.
Line 15: It initially assigns x the value 5.
Line 17: It then calls procedure f(), passing x as an argument.
Line 5: Inside f(), the writeln() statement shows that the corresponding parameter fx is initially 5, the value passed in.
Line 6: fx is then assigned the value 10.
Line 7: This value is verified by this writeln() statement executed just before f() exits.
Line 18: Back in the calling environment of the main program, this writeln() statement shows that after f() returns, x is still 5, as it was prior to the procedure call.
Running this code generates the following output:

Before f():  x = 5
Start  f():  fx = 5
End    f():  fx = 10
After  f():  x = 5
In this example, x is passed by value, so f() receives only a copy. When the corresponding parameter fx is modified, x is unaffected.

Note: If you want to see this in action, then you can run the code for yourself using an online Pascal compiler.

Just follow these steps:

Copy the code from the code box above.
Visit the Online Pascal Compiler.
In the code box on the left, replace any existing contents with the code you copied in step 1.
Click Execute.
You should see the same output as above.

Now, compare this with the next example:

 1// Pascal Example #2
 2
 3procedure f(var fx : integer);
 4begin
 5    writeln('Start  f():  fx = ', fx);
 6    fx := 10;
 7    writeln('End    f():  fx = ', fx);
 8end;
 9
10// Main program
11var
12    x : integer;
13
14begin
15    x := 5;
16    writeln('Before f():  x = ', x);
17    f(x);
18    writeln('After  f():  x = ', x);
19end.
This code is identical to the first example, with one change. It’s the presence of the word var in front of fx in the definition of procedure f() on line 3. That indicates that the argument to f() is passed by reference. Changes made to the corresponding parameter fx will also modify the argument in the calling environment.

The output from this code is the same as before, except for the last line:

Before f():  x = 5
Start  f():  fx = 5
End    f():  fx = 10
After  f():  x = 10
Again, fx is assigned the value 10 inside f() as before. But this time, when f() returns, x in the main program has also been modified.

In many programming languages, that’s essentially the distinction between pass-by-value and pass-by-reference:

If a variable is passed by value, then the function has a copy to work on, but it can’t modify the original value in the calling environment.
If a variable is passed by reference, then any changes the function makes to the corresponding parameter will affect the value in the calling environment.
The reason why comes from what a reference means in these languages. Variable values are stored in memory. In Pascal and similar languages, a reference is essentially the address of that memory location, as demonstrated below:

In the diagram on the left, x has memory allocated in the main program’s namespace. When f() is called, x is passed by value, so memory for the corresponding parameter fx is allocated in the namespace of f(), and the value of x is copied there. When f() modifies fx, it’s this local copy that is changed. The value of x in the calling environment remains unaffected.

In the diagram on the right, x is passed by reference. The corresponding parameter fx points to the actual address in the main program’s namespace where the value of x is stored. When f() modifies fx, it’s modifying the value in that location, just the same as if the main program were modifying x itself.

Pass-By-Value vs Pass-By-Reference in Python
Are parameters in Python pass-by-value or pass-by-reference? The answer is they’re neither, exactly. That’s because a reference doesn’t mean quite the same thing in Python as it does in Pascal.

Recall that in Python, every piece of data is an object. A reference points to an object, not a specific memory location. That means assignment isn’t interpreted the same way in Python as it is in Pascal. Consider the following pair of statements in Pascal:

x := 5
x := 10
These are interpreted this way:

The variable x references a specific memory location.
The first statement puts the value 5 in that location.
The next statement overwrites the 5 and puts 10 there instead.
By contrast, in Python, the analogous assignment statements are as follows:

x = 5
x = 10
These assignment statements have the following meaning:

The first statement causes x to point to an object whose value is 5.
The next statement reassigns x as a new reference to a different object whose value is 10. Stated another way, the second assignment rebinds x to a different object with value 10.
In Python, when you pass an argument to a function, a similar rebinding occurs. Consider this example:

>>>
 1>>> def f(fx):
 2...     fx = 10
 3...
 4>>> x = 5
 5>>> f(x)
 6>>> x
 75
In the main program, the statement x = 5 on line 4 creates a reference named x bound to an object whose value is 5. f() is then called on line 5, with x as an argument. When f() first starts, a new reference called fx is created, which initially points to the same 5 object as x does:

Argument Passing Summary
Argument passing in Python can be summarized as follows. Passing an immutable object, like an int, str, tuple, or frozenset, to a Python function acts like pass-by-value. The function can’t modify the object in the calling environment.

Passing a mutable object such as a list, dict, or set acts somewhat—but not exactly—like pass-by-reference. The function can’t reassign the object wholesale, but it can change items in place within the object, and these changes will be reflected in the calling environment.

Side Effects
So, in Python, it’s possible for you to modify an argument from within a function so that the change is reflected in the calling environment. But should you do this? This is an example of what’s referred to in programming lingo as a side effect.

More generally, a Python function is said to cause a side effect if it modifies its calling environment in any way. Changing the value of a function argument is just one of the possibilities.

Note: You’re probably familiar with side effects from the field of human health, where the term typically refers to an unintended consequence of medication. Often, the consequence is undesirable, like vomiting or sedation. On the other hand, side effects can be used intentionally. For example, some medications cause appetite stimulation, which can be used to an advantage, even if that isn’t the medication’s primary intent.

The concept is similar in programming. If a side effect is a well-documented part of the function specification, and the user of the function is expressly aware of when and how the calling environment might be modified, then it can be okay. But a programmer may not always properly document side effects, or they may not even be aware that side effects are occurring.

When they’re hidden or unexpected, side effects can lead to program errors that are very difficult to track down. Generally, it’s best to avoid them.

The return Statement
What’s a Python function to do then? After all, in many cases, if a function doesn’t cause some change in the calling environment, then there isn’t much point in calling it at all. How should a function affect its caller?

Well, one possibility is to use function return values. A return statement in a Python function serves two purposes:

It immediately terminates the function and passes execution control back to the caller.
It provides a mechanism by which the function can pass data back to the caller.
Exiting a Function
Within a function, a return statement causes immediate exit from the Python function and transfer of execution back to the caller:

>>>
>>> def f():
...     print('foo')
...     print('bar')
...     return
...

>>> f()
foo
bar
In this example, the return statement is actually superfluous. A function will return to the caller when it falls off the end—that is, after the last statement of the function body is executed. So, this function would behave identically without the return statement.

However, return statements don’t need to be at the end of a function. They can appear anywhere in a function body, and even multiple times. Consider this example:

>>>
 1>>> def f(x):
 2...     if x < 0:
 3...         return
 4...     if x > 100:
 5...         return
 6...     print(x)
 7...
 8
 9>>> f(-3)
10>>> f(105)
11>>> f(64)
1264
The first two calls to f() don’t cause any output, because a return statement is executed and the function exits prematurely, before the print() statement on line 6 is reached.

This sort of paradigm can be useful for error checking in a function. You can check several error conditions at the start of the function, with return statements that bail out if there’s a problem:

def f():
    if error_cond1:
        return
    if error_cond2:
        return
    if error_cond3:
        return

    <normal processing>
If none of the error conditions are encountered, then the function can proceed with its normal processing.

Returning Data to the Caller
In addition to exiting a function, the return statement is also used to pass data back to the caller. If a return statement inside a Python function is followed by an expression, then in the calling environment, the function call evaluates to the value of that expression:

>>>
 1>>> def f():
 2...     return 'foo'
 3...
 4
 5>>> s = f()
 6>>> s
 7'foo'
Here, the value of the expression f() on line 5 is 'foo', which is subsequently assigned to variable s.

A function can return any type of object. In Python, that means pretty much anything whatsoever. In the calling environment, the function call can be used syntactically in any way that makes sense for the type of object the function returns.

For example, in this code, f() returns a dictionary. In the calling environment then, the expression f() represents a dictionary, and f()['baz'] is a valid key reference into that dictionary:

>>>
>>> def f():
...     return dict(foo=1, bar=2, baz=3)
...

>>> f()
{'foo': 1, 'bar': 2, 'baz': 3}
>>> f()['baz']
3
In the next example, f() returns a string that you can slice like any other string:

>>>
>>> def f():
...     return 'foobar'
...

>>> f()[2:4]
'ob'
Here, f() returns a list that can be indexed or sliced:

>>>
>>> def f():
...     return ['foo', 'bar', 'baz', 'qux']
...

>>> f()
['foo', 'bar', 'baz', 'qux']
>>> f()[2]
'baz'
>>> f()[::-1]
['qux', 'baz', 'bar', 'foo']
If multiple comma-separated expressions are specified in a return statement, then they’re packed and returned as a tuple:

>>>
>>> def f():
...     return 'foo', 'bar', 'baz', 'qux'
...

>>> type(f())
<class 'tuple'>
>>> t = f()
>>> t
('foo', 'bar', 'baz', 'qux')

>>> a, b, c, d = f()
>>> print(f'a = {a}, b = {b}, c = {c}, d = {d}')
a = foo, b = bar, c = baz, d = qux
When no return value is given, a Python function returns the special Python value None:

>>>
>>> def f():
...     return
...

>>> print(f())
None
The same thing happens if the function body doesn’t contain a return statement at all and the function falls off the end:

>>>
>>> def g():
...     pass
...

>>> print(g())
None
Recall that None is falsy when evaluated in a Boolean context.

Since functions that exit through a bare return statement or fall off the end return None, a call to such a function can be used in a Boolean context:

>>>
>>> def f():
...     return
...
>>> def g():
...     pass
...

>>> if f() or g():
...     print('yes')
... else:
...     print('no')
...
no
Here, calls to both f() and g() are falsy, so f() or g() is as well, and the else clause executes.

Revisiting Side Effects
Suppose you want to write a function that takes an integer argument and doubles it. That is, you want to pass an integer variable to the function, and when the function returns, the value of the variable in the calling environment should be twice what it was. In Pascal, you could accomplish this using pass-by-reference:

 1procedure double(var x : integer);
 2begin
 3    x := x * 2;
 4end;
 5
 6var
 7    x : integer;
 8
 9begin
10    x := 5;
11    writeln('Before procedure call: ', x);
12    double(x);
13    writeln('After procedure call:  ', x);
14end.
Executing this code produces the following output, which verifies that double() does indeed modify x in the calling environment:

Before procedure call: 5
After procedure call:  10
In Python, this won’t work. As you now know, Python integers are immutable, so a Python function can’t change an integer argument by side effect:

>>>
>>> def double(x):
...     x *= 2
...

>>> x = 5
>>> double(x)
>>> x
5
However, you can use a return value to obtain a similar effect. Simply write double() so that it takes an integer argument, doubles it, and returns the doubled value. Then, the caller is responsible for the assignment that modifies the original value:

>>>
>>> def double(x):
...     return x * 2
...

>>> x = 5
>>> x = double(x)
>>> x
10
This is arguably preferable to modifying by side effect. It’s very clear that x is being modified in the calling environment because the caller is doing so itself. Anyway, it’s the only option, because modification by side effect doesn’t work in this case.

Still, even in cases where it’s possible to modify an argument by side effect, using a return value may still be clearer. Suppose you want to double every item in a list. Because lists are mutable, you could define a Python function that modifies the list in place:

>>>
>>> def double_list(x):
...     i = 0
...     while i < len(x):
...             x[i] *= 2
...             i += 1
...

>>> a = [1, 2, 3, 4, 5]
>>> double_list(a)
>>> a
[2, 4, 6, 8, 10]
Unlike double() in the previous example, double_list() actually works as intended. If the documentation for the function clearly states that the list argument’s contents are changed, then this may be a reasonable implementation.

However, you can also write double_list() to pass the desired list back by return value and allow the caller to make the assignment, similar to how double() was re-written in the previous example:

>>>
>>> def double_list(x):
...     r = []
...     for i in x:
...             r.append(i * 2)
...     return r
...

>>> a = [1, 2, 3, 4, 5]
>>> a = double_list(a)
>>> a
[2, 4, 6, 8, 10]
Either approach works equally well. As is often the case, this is a matter of style, and personal preferences vary. Side effects aren’t necessarily consummate evil, and they have their place, but because virtually anything can be returned from a function, the same thing can usually be accomplished through return values as well.

Variable-Length Argument Lists
In some cases, when you’re defining a function, you may not know beforehand how many arguments you’ll want it to take. Suppose, for example, that you want to write a Python function that computes the average of several values. You could start with something like this:

>>>
>>> def avg(a, b, c):
...     return (a + b + c) / 3
...
All is well if you want to average three values:

>>>
>>> avg(1, 2, 3)
2.0
However, as you’ve already seen, when positional arguments are used, the number of arguments passed must agree with the number of parameters declared. Clearly then, all isn’t well with this implementation of avg() for any number of values other than three:

>>>
>>> avg(1, 2, 3, 4)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    avg(1, 2, 3, 4)
TypeError: avg() takes 3 positional arguments but 4 were given
You could try to define avg() with optional parameters:

>>>
>>> def avg(a, b=0, c=0, d=0, e=0):
...     .
...     .
...     .
...
This allows for a variable number of arguments to be specified. The following calls are at least syntactically correct:

avg(1)
avg(1, 2)
avg(1, 2, 3)
avg(1, 2, 3, 4)
avg(1, 2, 3, 4, 5)
But this approach still suffers from a couple of problems. For starters, it still only allows up to five arguments, not an arbitrary number. Worse yet, there’s no way to distinguish between the arguments that were specified and those that were allowed to default. The function has no way to know how many arguments were actually passed, so it doesn’t know what to divide by:

>>>
>>> def avg(a, b=0, c=0, d=0, e=0):
...     return (a + b + c + d + e) / # Divided by what???
...
Evidently, this won’t do either.

You could write avg() to take a single list argument:

>>>
>>> def avg(a):
...     total = 0
...     for v in a:
...             total += v
...     return total / len(a)
...

>>> avg([1, 2, 3])
2.0
>>> avg([1, 2, 3, 4, 5])
3.0
At least this works. It allows an arbitrary number of values and produces a correct result. As an added bonus, it works when the argument is a tuple as well:

>>>
>>> t = (1, 2, 3, 4, 5)
>>> avg(t)
3.0
The drawback is that the added step of having to group the values into a list or tuple is probably not something the user of the function would expect, and it isn’t very elegant. Whenever you find Python code that looks inelegant, there’s probably a better option.

In this case, indeed there is! Python provides a way to pass a function a variable number of arguments with argument tuple packing and unpacking using the asterisk (*) operator.

Conclusion
As applications grow larger, it becomes increasingly important to modularize code by breaking it up into smaller functions of manageable size. You now hopefully have all the tools you need to do this.

You’ve learned:

How to create a user-defined function in Python
Several different ways you can pass arguments to a function
How you can return data from a function to its caller
How to add documentation to functions with docstrings and annotations
Next up in this series are two tutorials that cover searching and pattern matching. You will get an in-depth look at a Python module called re, which contains functionality for searching and matching using a versatile pattern syntax called a regular expression.



Getting Started With Python Functions
Most programming languages allow you to assign a name to a code block that performs a concrete computation. These named code blocks can be reused quickly because you can use their name to call them from different places in your code.

Programmers call these named code blocks subroutines, routines, procedures, or functions depending on the language they use. In some languages, there’s a clear difference between a routine or procedure and a function.

Sometimes that difference is so strong that you need to use a specific keyword to define a procedure or subroutine and another keyword to define a function. For example the Visual Basic programming language uses Sub and Function to differentiate between the two.

In general, a procedure is a named code block that performs a set of actions without computing a final value or result. On the other hand, a function is a named code block that performs some actions with the purpose of computing a final value or result, which is then sent back to the caller code. Both procedures and functions can act upon a set of input values, commonly known as arguments.

In Python, these kinds of named code blocks are known as functions because they always send a value back to the caller. The Python documentation defines a function as follows:

A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body. (Source)

Even though the official documentation states that a function “returns some value to the caller,” you’ll soon see that functions can return any Python object to the caller code.

In general, a function takes arguments (if any), performs some operations, and returns a value (or object). The value that a function returns to the caller is generally known as the function’s return value. All Python functions have a return value, either explicit or implicit. You’ll cover the difference between explicit and implicit return values later in this tutorial.

To write a Python function, you need a header that starts with the def keyword, followed by the name of the function, an optional list of comma-separated arguments inside a required pair of parentheses, and a final colon.

The second component of a function is its code block, or body. Python defines code blocks using indentation instead of brackets, begin and end keywords, and so on. So, to define a function in Python you can use the following syntax:

def function_name(arg1, arg2,..., argN):
    # Function's code goes here...
    pass
When you’re coding a Python function, you need to define a header with the def keyword, the name of the function, and a list of arguments in parentheses. Note that the list of arguments is optional, but the parentheses are syntactically required. Then you need to define the function’s code block, which will begin one level of indentation to the right.

In the above example, you use a pass statement. This kind of statement is useful when you need a placeholder statement in your code to make it syntactically correct, but you don’t need to perform any action. pass statements are also known as the null operation because they don’t perform any action.

Note: The full syntax to define functions and their arguments is beyond the scope of this tutorial. For an in-depth resource on this topic, check out Defining Your Own Python Function.

To use a function, you need to call it. A function call consists of the function’s name followed by the function’s arguments in parentheses:

function_name(arg1, arg2, ..., argN)
You’ll need to pass arguments to a function call only if the function requires them. The parentheses, on the other hand, are always required in a function call. If you forget them, then you won’t be calling the function but referencing it as a function object.

To make your functions return a value, you need to use the Python return statement. That’s what you’ll cover from this point on.














## Argumentos Opcionais

Defining your own functions is an essential skill for writing clean and effective code. In this tutorial, you’ll explore the techniques you have available for defining Python functions that take optional arguments. When you master Python optional arguments, you’ll be able to define functions that are more powerful and more flexible.

In this tutorial, you’ll learn:

What the difference is between parameters and arguments
How to define functions with optional arguments and default parameter values
How to define functions using args and kwargs
How to deal with error messages about optional arguments

Creating Functions in Python for Reusing Code
You can think of a function as a mini-program that runs within another program or within another function. The main program calls the mini-program and sends information that the mini-program will need as it runs. When the function completes all of its actions, it may send some data back to the main program that has called it.

The primary purpose of a function is to allow you to reuse the code within it whenever you need it, using different inputs if required.

When you use functions, you are extending your Python vocabulary. This lets you express the solution to your problem in a clearer and more succinct way.

In Python, by convention, you should name a function using lowercase letters with words separated by an underscore, such as do_something(). These conventions are described in PEP 8, which is Python’s style guide. You’ll need to add parentheses after the function name when you call it. Since functions represent actions, it’s a best practice to start your function names with a verb to make your code more readable.

Defining Functions With No Input Parameters
In this tutorial, you’ll use the example of a basic program that creates and maintains a shopping list and prints it out when you’re ready to go to the supermarket.

Start by creating a shopping list:

shopping_list = {
    "Bread": 1,
    "Milk": 2,
    "Chocolate": 1,
    "Butter": 1,
    "Coffee": 1,
}
You’re using a dictionary to store the item name as the key and the quantity you need to buy of each item as the value. You can define a function to display the shopping list:

# optional_params.py

shopping_list = {
    "Bread": 1,
    "Milk": 2,
    "Chocolate": 1,
    "Butter": 1,
    "Coffee": 1,
}

def show_list():
    for item_name, quantity in shopping_list.items():
        print(f"{quantity}x {item_name}")

show_list()
When you run this script, you’ll get a printout of the shopping list:

$ python optional_params.py
1x Bread
2x Milk
1x Chocolate
1x Butter
1x Coffee
The function you’ve defined has no input parameters as the parentheses in the function signature are empty. The signature is the first line in the function definition:

def show_list():
You don’t need any input parameters in this example since the dictionary shopping_list is a global variable. This means that it can be accessed from everywhere in the program, including from within the function definition. This is called the global scope. You can read more about scope in Python Scope & the LEGB Rule: Resolving Names in Your Code.

Using global variables in this way is not a good practice. It can lead to several functions making changes to the same data structure, which can lead to bugs that are hard to find. You’ll see how to improve on this later on in this tutorial when you’ll pass the dictionary to the function as an argument.

Note: For more information on using global variables in functions, head over to Using and Creating Global Variables in Your Python Functions.

In the next section, you’ll define a function that has input parameters.

Defining Functions With Required Input Arguments
Instead of writing the shopping list directly in the code, you can now initialize an empty dictionary and write a function that allows you to add items to the shopping list:

# optional_params.py

shopping_list = {}

# ...

def add_item(item_name, quantity):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item("Bread", 1)
print(shopping_list)
The function iterates through the dictionary’s keys, and if the key exists, the quantity is increased. If the item is not one of the keys, the key is created and a value of 1 is assigned to it. You can run this script to show the printed dictionary:

$ python optional_params.py
{'Bread': 1}
You’ve included two parameters in the function signature:

item_name
quantity
Parameters don’t have any values yet. The parameter names are used in the code within the function definition. When you call the function, you pass arguments within the parentheses, one for each parameter. An argument is a value you pass to the function.

The distinction between parameters and arguments can often be overlooked. It’s a subtle but important difference. You may sometimes find parameters referred to as formal parameters and arguments as actual parameters.

The arguments you input when calling add_item() are required arguments. If you try to call the function without the arguments, you’ll get an error:

# optional_params.py

shopping_list = {}

def add_item(item_name, quantity):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item()
print(shopping_list)
The traceback will give a TypeError stating that the arguments are required:

$ python optional_params.py
Traceback (most recent call last):
  File "optional_params.py", line 11, in <module>
    add_item()
TypeError: add_item() missing 2 required positional arguments: 'item_name' and 'quantity'
You’ll look at more error messages related to using the wrong number of arguments, or using them in the wrong order, in a later section of this tutorial.

Using Python Optional Arguments With Default Values
In this section, you’ll learn how to define a function that takes an optional argument. Functions with optional arguments offer more flexibility in how you can use them. You can call the function with or without the argument, and if there is no argument in the function call, then a default value is used.

Default Values Assigned to Input Parameters
You can modify the function add_item() so that the parameter quantity has a default value:

# optional_params.py

shopping_list = {}

def add_item(item_name, quantity=1):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item("Bread")
add_item("Milk", 2)
print(shopping_list)
In the function signature, you’ve added the default value 1 to the parameter quantity. This doesn’t mean that the value of quantity will always be 1. If you pass an argument corresponding to quantity when you call the function, then that argument will be used as the value for the parameter. However, if you don’t pass any argument, then the default value will be used.

Parameters with default values can’t be followed by regular parameters. You’ll read more about the order in which you can define parameters later in this tutorial.

The function add_item() now has one required parameter and one optional parameter. In the code example above, you call add_item() twice. Your first function call has a single argument, which corresponds to the required parameter item_name. In this case, quantity defaults to 1. Your second function call has two arguments, so the default value isn’t used in this case. You can see the output of this below:

$ python optional_params.py
{'Bread': 1, 'Milk': 2}
You can also pass required and optional arguments into a function as keyword arguments. Keyword arguments can also be referred to as named arguments:

add_item(item_name="Milk", quantity=2)
You can now revisit the first function you defined in this tutorial and refactor it so that it also accepts a default argument:

def show_list(include_quantities=True):
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)
Now when you use show_list(), you can call it with no input arguments or pass a Boolean value as a flag argument. If you don’t pass any arguments when calling the function, then the shopping list is displayed by showing each item’s name and quantity. The function will display the same output if you pass True as an argument when calling the function. However, if you use show_list(False), only the item names are displayed.

You should avoid using flags in cases where the value of the flag alters the function’s behavior significantly. A function should only be responsible for one thing. If you want a flag to push the function into an alternative path, you may consider writing a separate function instead.

Common Default Argument Values
In the examples you worked on above, you used the integer 1 as a default value in one case and the Boolean value True in the other. These are common default values you’ll find in function definitions. However, the data type you should use for default values depends on the function you’re defining and how you want the function to be used.

The integers 0 and 1 are common default values to use when a parameter’s value needs to be an integer. This is because 0 and 1 are often useful fallback values to have. In the add_item() function you wrote earlier, setting the quantity for a new item to 1 is the most logical option.

However, if you had a habit of buying two of everything you purchase when you go to the supermarket, then setting the default value to 2 may be more appropriate for you.

When the input parameter needs to be a string, a common default value to use is the empty string (""). This assigns a value whose data type is string but doesn’t put in any additional characters. You can modify add_item() so that both arguments are optional:

def add_item(item_name="", quantity=1):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity
You have modified the function so that both parameters have a default value and therefore the function can be called with no input parameters:

add_item()
This line of code will add an item to the shopping_list dictionary with an empty string as a key and a value of 1. It’s fairly common to check whether an argument has been passed when the function is called and run some code accordingly. You can change the above function to do this:

def add_item(item_name="", quantity=1):
    if not item_name:
        quantity = 0
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity
In this version, if no item is passed to the function, the function sets the quantity to 0. The empty string has a falsy value, which means that bool("") returns False, whereas any other string will have a truthy value. When an if keyword is followed by a truthy or falsy value, the if statement will interpret these as True or False. You can read more about truthy and falsy values in Python Booleans: Use Truth Values in Your Code.

Therefore, you can use the variable directly within an if statement to check whether an optional argument was used.

Another common value that’s often used as a default value is None. This is Python’s way of representing nothing, although it is actually an object that represents the null value. You’ll see an example of when None is a useful default value to use in the next section.

Data Types That Shouldn’t Be Used as Default Arguments
You’ve used integers and strings as default values in the examples above, and None is another common default value. These are not the only data types you can use as default values. However, not all data types should be used.

In this section, you’ll see why mutable data types should not be used as default values in function definitions. A mutable object is one whose values can be changed, such as a list or a dictionary. You can find out more about mutable and immutable data types in Python’s Mutable vs Immutable Types: What’s the Difference?, Immutability in Python, and Python’s official documentation.

You can add the dictionary containing the item names and quantities as an input parameter to the function you defined earlier. You can start by making all arguments required ones:

def add_item(item_name, quantity, shopping_list):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list
You can now pass shopping_list to the function when you call it. This makes the function more self-contained as it doesn’t rely on a variable called shopping_list to exist in the scope that’s calling the function. This change also makes the function more flexible as you can use it with different input dictionaries.

You’ve also added the return statement to return the modified dictionary. This line is technically not required at this stage as dictionaries are a mutable data type and therefore the function will change the state of the dictionary that exists in the main module. However, you’ll need the return statement later when you make this argument optional, so it’s best to include it now.

To call the function, you’ll need to assign the data returned by the function to a variable:

shopping_list = add_item("Coffee", 2, shopping_list)
You can also add a shopping_list parameter to show_list(), the first function you defined in this tutorial. You can now have several shopping lists in your program and use the same functions to add items and display the shopping lists:

# optional_params.py

hardware_store_list = {}
supermarket_list = {}

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name, quantity, shopping_list):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list

hardware_store_list = add_item("Nails", 1, hardware_store_list)
hardware_store_list = add_item("Screwdriver", 1, hardware_store_list)
hardware_store_list = add_item("Glue", 3, hardware_store_list)

supermarket_list = add_item("Bread", 1, supermarket_list)
supermarket_list = add_item("Milk", 2, supermarket_list)

show_list(hardware_store_list)
show_list(supermarket_list)
You can see the output of this code below. The list of items to buy from the hardware store is shown first. The second part of the output shows the items needed from the supermarket:

$ python optional_params.py

1x Nails
1x Screwdriver
3x Glue

1x Bread
2x Milk
You’ll now add a default value for the parameter shopping_list in add_item() so that if no dictionary is passed to the function, then an empty dictionary is used. The most tempting option is to make the default value an empty dictionary. You’ll see why this is not a good idea soon, but you can try this option for now:

# optional_params.py

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name, quantity, shopping_list={}):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list

clothes_shop_list = add_item("Shirt", 3)
show_list(clothes_shop_list)
When you run this script, you’ll get the output below showing the items needed from the clothes shop, which may give the impression that this code works as intended:

$ python optional_params.py

3x Shirt
However, this code has a serious flaw that can lead to unexpected and wrong results. You can add a new shopping list for items needed from the electronics store by using add_item() with no argument corresponding to shopping_list. This leads to the default value being used, which you’d hope would create a new empty dictionary:

# optional_params.py

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name, quantity, shopping_list={}):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list

clothes_shop_list = add_item("Shirt", 3)
electronics_store_list = add_item("USB cable", 1)
show_list(clothes_shop_list)
show_list(electronics_store_list)
You’ll see the problem when you look at the output from this code:

$ python optional_params.py

3x Shirt
1x USB cable

3x Shirt
1x USB cable
Both shopping lists are identical even though you assigned the output from add_item() to different variables each time you called the function. The problem happens because dictionaries are a mutable data type.

You assigned an empty dictionary as the default value for the parameter shopping_list when you defined the function. The first time you call the function, this dictionary is empty. However, as dictionaries are a mutable type, when you assign values to the dictionary, the default dictionary is no longer empty.

When you call the function the second time and the default value for shopping_list is required again, the default dictionary is no longer empty as it was populated the first time you called the function. Since you’re calling the same function, you’re using the same default dictionary stored in memory.

This behavior doesn’t happen with immutable data types. The solution to this problem is to use another default value, such as None, and then create an empty dictionary within the function when no optional argument is passed:

# optional_params.py

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name, quantity, shopping_list=None):
    if shopping_list is None:
        shopping_list = {}
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list

clothes_shop_list = add_item("Shirt", 3)
electronics_store_list = add_item("USB cable", 1)
show_list(clothes_shop_list)
show_list(electronics_store_list)
You can check whether a dictionary has been passed as an argument using the if statement. You should not rely on the falsy nature of None but instead explicitly check that the argument is None. Relying on the fact that None will be treated as a false value can cause problems if another argument that is falsy is passed.

Now when you run your script again, you’ll get the correct output since a new dictionary is created each time you use the function with the default value for shopping_list:

$ python optional_params.py

3x Shirt

1x USB cable
You should always avoid using a mutable data type as a default value when defining a function with optional parameters.


Functions Accepting Any Number of Arguments
Before defining a function that accepts any number of arguments, you’ll need to be familiar with the unpacking operator. You can start with a list such as the following one:

>>>
>>> some_items = ["Coffee", "Tea", "Cake", "Bread"]
The variable some_items points to a list, and the list, in turn, has four items within it. If you use some_items as an argument to print(), then you’re passing one variable to print():

>>>
>>> print(some_items)
['Coffee', 'Tea', 'Cake', 'Bread']
print() displays the list, as you would expect. However, if you had to use *some_items within the parentheses of print(), you’ll get a different outcome:

>>>
>>> print(*some_items)
Coffee Tea Cake Bread
This time, print() displays the four separate strings rather than the list. This is equivalent to writing the following:

>>>
>>> print("Coffee", "Tea", "Cake", "Bread")
Coffee Tea Cake Bread
When the asterisk or star symbol (*) is used immediately before a sequence, such as some_items, it unpacks the sequence into its individual components. When a sequence such as a list is unpacked, its items are extracted and treated as individual objects.

You may have noticed that print() can take any number of arguments. You’ve used it with one input argument and with four input arguments in the examples above. You can also use print() with empty parentheses, and it will print a blank line.

You’re now ready to define your own functions that accept a variable number of input arguments. For the time being, you can simplify add_items() to accept only the names of the items you want in the shopping list. You’ll set the quantity to 1 for each item. You’ll then get back to including the quantities as part of the input arguments in the next section.

The function signature that includes the variable number of input arguments using args looks like this:

def add_items(shopping_list, *args):
You’ll often see function signatures that use the name args to represent this type of optional argument. However, this is just a parameter name. There is nothing special about the name args. It is the preceding * that gives this parameter its particular properties, which you’ll read about below. Often, it’s better to use a parameter name that suits your needs best to make the code more readable, as in the example below:

# optional_params.py

shopping_list = {}

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_items(shopping_list, *item_names):
    for item_name in item_names:
        shopping_list[item_name] = 1

    return shopping_list

shopping_list = add_items(shopping_list, "Coffee", "Tea", "Cake", "Bread")
show_list(shopping_list)
The first argument when calling add_items() is a required argument. Following the first argument, the function can accept any number of additional arguments. In this case, you’ve added four additional arguments when calling the function. Here’s the output of the above code:

$ python optional_params.py

1x Coffee
1x Tea
1x Cake
1x Bread
You can understand what’s happening with the item_names parameter by looking at a simplified example:

>>>
>>> def add_items_demo(*item_names):
...     print(type(item_names))
...     print(item_names)
...
>>> add_items_demo("Coffee", "Tea", "Cake", "Bread")
<class 'tuple'>
('Coffee', 'Tea', 'Cake', 'Bread')
When you display the data type, you can see that item_names is a tuple. Therefore, all the additional arguments are assigned as items in the tuple item_names. You can then use this tuple within the function definition as you did in the main definition of add_items() above, in which you’re iterating through the tuple item_names using a for loop.

This is not the same as passing a tuple as an argument in the function call. Using *args allows you to use the function more flexibly as you can add as many arguments as you wish without the need to place them in a tuple in the function call.

If you don’t add any additional arguments when you call the function, then the tuple will be empty:

>>>
>>> add_items_demo()
<class 'tuple'>
()
When you add args to a function definition, you’ll usually add them after all the required and optional parameters. You can have keyword-only arguments that follow the args, but for this tutorial, you can assume that args will usually be added after all other arguments, except for kwargs, which you’ll learn about in the following section.


Functions Accepting Any Number of Keyword Arguments
When you define a function with parameters, you have a choice of calling the function using either non-keyword arguments or keyword arguments:

>>>
>>> def test_arguments(a, b):
...     print(a)
...     print(b)
...
>>> test_arguments("first argument", "second argument")
first argument
second argument
>>> test_arguments(a="first argument", b="second argument")
first argument
second argument
In the first function call, the arguments are passed by position, whereas in the second one they’re passed by keyword. If you use keyword arguments, you no longer need to input arguments in the order they are defined:

>>>
>>> test_arguments(b="second argument", a="first argument")
first argument
second argument
You can change this default behavior by declaring positional-only arguments or keyword-only arguments.

When defining a function, you can include any number of optional keyword arguments to be included using kwargs, which stands for keyword arguments. The function signature looks like this:

def add_items(shopping_list, **kwargs):
The parameter name kwargs is preceded by two asterisks (**). The double star or asterisk operates similarly to the single asterisk you used earlier to unpack items from a sequence. The double star is used to unpack items from a mapping. A mapping is a data type that has paired values as items, such as a dictionary.

The parameter name kwargs is often used in function definitions, but the parameter can have any other name as long as it’s preceded by the ** operator. You can now rewrite add_items() so that it accepts any number of keyword arguments:

# optional_params.py

shopping_list = {}

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_items(shopping_list, **things_to_buy):
    for item_name, quantity in things_to_buy.items():
        shopping_list[item_name] = quantity

    return shopping_list

shopping_list = add_items(shopping_list, coffee=1, tea=2, cake=1, bread=3)
show_list(shopping_list)
The output from this code displays the items in the dictionary shopping_list, showing all four things you wish to buy and their respective quantities. You included this information as keyword arguments when you called the function:

$ python optional_params.py

1x coffee
2x tea
1x cake
3x bread
Earlier, you learned that args is a tuple, and the optional non-keyword arguments used in the function call are stored as items in the tuple. The optional keyword arguments are stored in a dictionary, and the keyword arguments are stored as key-value pairs in this dictionary:

>>>
>>> def add_items_demo(**things_to_buy):
...     print(type(things_to_buy))
...     print(things_to_buy)
...
>>> add_items_demo(coffee=1, tea=2, cake=1, bread=3)
<class 'dict'>
{'coffee': 1, 'tea': 2, 'cake': 1, 'bread': 3}
To learn more about args and kwargs, you can read Python args and kwargs: Demystified, and you’ll find more detail about keyword and non-keyword arguments in functions and the order in which arguments can be used in Defining Your Own Python Function.

Conclusion
Defining your own function to create a self-contained subroutine is one of the key building blocks when writing code. The most useful and powerful functions are those that perform one clear task and that you can use in a flexible manner. Using optional arguments is a key technique to achieve this.

In this tutorial, you’ve learned:

What the difference is between parameters and arguments
How to define functions with optional arguments and default parameter values
How to define functions using args and kwargs
How to deal with error messages about optional arguments
A good understanding of optional arguments will also help you use functions in the standard library and in other third-party modules. Displaying the documentation for these functions will show you the function signature from which you’ll be able to identify which arguments are required, which ones are optional, and which ones are args or kwargs.

However, the main skill you’ve learned in this tutorial is to define your own functions. You can now start writing functions with required and optional parameters and with a variable number of non-keyword and keyword arguments. Mastering these skills will help you take your Python coding to the next level.