<div align="center">
  <h1>LMQL Tutorial</h1>
  <h4>By Amelia Opsahl </h4>
  <img src="https://lmql.ai/assets/lmql.6950db7a.svg" alt="Alt text" width="300">
  <h2> Exploring an emerging programming language for large language models </h2>
</div>

The Language Model Query Language, or LMQL, is a programming language that was designed with the express purpose of language model interaction. LMQL was developed by the SRI Lab at ETH Zürich and aims to make interactions between the user and language models smoother and more efficient. LMQL is unique in that it combines traditional programming with the ability to call large lanuage models (LLMs) in a user's code, allowing for the integration of LLM interaction natively at the level of program code. 

> <span style="color:gray; opacity:0.7;">For more information on LMQL from its developpers, users can visit the [LMQL website](https://lmql.ai/) or the SRI Lab's [GitHub repository](https://github.com/eth-sri/lmql) on LMQL.</span>

This tutorial gives a more detailed overview of LMQL works, walks through how to get started with LMQL, explores its main features, and evaluates the efectiveness and efficiency of those features in comparison to those of an LLM used without LMQL. For follow-up questions about the tutorial or suggestions for improvement, please contact the author, [Amelia Opsahl](mailto:aopsahl25@cmc.edu).

## Understanding LMQL

An LMQL query is formatted very similary to a standard Python program. However, in an LMQL query top-level strings are interpreted as query strings that are passed to an LLM. For example:
```
@lmql.query
def example():
    '''lmql 
    "Q:How tall is the empire state building?"
    "A: [ANSWER]"
    return ANSWER
    '''
print(example())
```
Program Output: 
```
The Empire State Building is 1,454 feet (443.2 meters) tall.
```
This scenario shows how an LMQL query containing both traditional algorithmic logic and LLM calls can be used to automatically complete template variables like `ANSWER`. Moreover, LMQL queries can leverage natural language prompting to allow for more personalzied outputs to program variables and enhanced model reasoning capabilities. For example:
```
@lmql.query
def example1():
    '''lmql 
    "Q:How tall is the empire state building? Give me just the height in feet without any other informaiton."
    "A: [ANSWER]"
    return ANSWER
    '''
print(example())
```
Program Output: 
```
1,454 feet.
```
Here, we see how algorithmic logic, LLM behavior, and prompt engineering can all come together in LMQL programs to fine-tune program output and efficiently handle complex queries.

## Getting started - LMQL Installation

LMQL can be installed locally on a user's personal computer. This tutorial will walk through example LMQL queries that are run locally from within Python. 

> <span style="color:gray; opacity:0.7;">LMQL can also be used via a local instance of a playground IDE. Using the playground instance requires the installation of Node.js, which can be done by following the instructions on the [Node.js](https://nodejs.org/en/download/package-manage) website.</span>

To use LMQL in Python, users can import the `lmql` package, run query code with `lmql.run`, or use a decorator `@lmql.query` for LMQL query functions. This tutorial will use the `@lmql.query` decorator for Pyton integration. The `lmql.run` function is favorable in that it allows users to directly run a string of LMQL code without having to define a function, but this tutorial uses the decorator because of its included support for accessing the surrounding Python environment.

As seen earlier, the `@lmql.query` decorator uses a piece of LMQL code as a Python function, which can then be called from a user's existing code:
```
@lmql.query
def example2(): 
    '''lmql
    "Q: What is the sum of 2+5?"
    "A: [SUM]"
    return SUM
    '''
print(example2())
```
Program Output: 
```
7
```
In terms of query configuration, users can further control query execution by setting the model, decoder, logging parameters, etc. for the query. For example, the following code would override the model and decoder specified in the query program and communicate whether to print verbose logging outputs during execution (e.g., LLM inference parameters). 
```
@lmql.query(model = lmql.model("chatgpt"), decoder = "argmax", verbose=False)
def example3(): 
    '''lmql
    "Q: Name five bird species."
    "A: [SUM]"
    return SUM
    '''
print(example3())
```
Program Output:
```
1. Robin
2. Blue Jay
3. Bald Eagle
4. Hummingbird
5. Pigeon
```
## Feature 1 - Prompt Construction

















