# Stack-Based Mathematical Expression Evaluator

## 1. Introduction

This project implements a Python program that evaluates
mathematical expressions using a stack data structure.

The program reads mathematical expressions from input.txt,
evaluates them, and writes the results to output.txt.

## 2. Objectives

The objectives of the project are:

- To implement a Stack class.
- To perform stack operations.
- To evaluate mathematical expressions using stacks.
- To handle operator precedence.
- To handle parentheses.
- To read expressions from a text file.
- To write evaluated results to another text file.

## 3. Data Structures Used

The program uses the stack data structure.

A stack follows the Last In, First Out (LIFO) principle.
The last element inserted is the first element removed.

The following operations are implemented:

- push(): Adds an element to the stack.
- pop(): Removes and returns the top element.
- peek(): Returns the top element without removing it.
- is_empty(): Checks whether the stack is empty.
- size(): Returns the number of elements.

Two stacks are used during evaluation:
an operator stack and a value stack.

## 4. Program Design

The program consists of the following functions:

1. tokenize(): Splits expressions into tokens.
2. infix_to_postfix(): Converts expressions into postfix notation.
3. evaluate_postfix(): Evaluates postfix expressions using a stack.
4. evaluate_expression(): Evaluates an expression.
5. format_result(): Formats the calculated result.
6. process_files(): Reads input.txt and writes output.txt.

## 5. Input and Output Files

The input.txt file contains mathematical expressions.
Each expression is written on a separate line.

Lines containing dashes separate the expressions.

The output.txt file contains the calculated results.
The separator lines are preserved.

## 6. Testing and Results

The program was tested using the following expressions:

3 + 5 * 2 = 13

(8 / 4) + 7 * 2 = 16

10 - (2 + 3) * 4 = -10

These examples demonstrate operator precedence,
parentheses, multiplication, division, addition,
and subtraction.

## 7. Conclusion

The project demonstrates how stacks can be used to
evaluate mathematical expressions.

It also demonstrates file handling, operator precedence,
expression parsing, and error handling in Python.

## 8. Requirements

Python 3 is required.

No additional libraries are needed.

## 9. Instructions for Running the Program

1. Save main.py and input.txt in the same folder.
2. Open a terminal in that folder.
3. Run the command: python main.py
4. Open output.txt to view the results.