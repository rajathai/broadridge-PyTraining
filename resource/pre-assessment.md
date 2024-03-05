### Python Pre Assessment Questions

#### Multiple Choice and Multi Select Type of Questions.

1. **What is the output of the following code snippet?**

   ```python
   print(8 // 3)
   ```

   A) 2.66
   B) 2
   C) 3
   D) 2.67
   **Answer: B) 2**

2. **Which of the following are immutable types in Python?** 

   A) Lists
   B) Tuples
   C) Dictionaries
   D) Sets
   **Answer: B) Tuples**

3. **What will be the output of the following code?**

   ```python
   x = "abcdef"
   i = "i"
   while i in x:
       print(i, end = " ")
   ```

   A) i i i i i i ...
   B) No output
   C) abcdef
   D) Error
   **Answer: D) Error**

4. **Which of the following is not a valid Python variable name?** 

   A) _myvar
   B) my_var
   C) 1myvar
   D) myVar
   **Answer: C) 1myvar**

5. **Select the correct way to create a function in Python.** 

   A) function myFunc():
   B) def myFunc():
   C) create myFunc():
   D) function: myFunc()
   **Answer: B) def myFunc():**

6. **What does the `len()` function do in Python?** 

   A) Returns the length of an object
   B) Converts an object to a list
   C) Counts the number of elements in a list
   D) Checks if the object is iterable
   **Answer: A) Returns the length of an object**

7. **Which of the following statements about Python dictionaries is correct?** 

   A) Dictionaries can have duplicate keys.
   B) Dictionaries are ordered collections.
   C) Dictionary values must be of the same data type.
   D) Dictionaries are accessed by key.
   **Answer: D) Dictionaries are accessed by key.**

8. **What is the output of the following code?**

   ```python
   def fun(x):
       x += 1
       return x
   
   x = 2
   x = fun(x+1)
   print(x)
   ```

   A) 2
   B) 3
   C) 4
   D) 5
   **Answer: C) 4**

9. **Select all that apply: Which of these are valid ways to create a list in Python?** 

   A) `list1 = list()`
   B) `list2 = []`
   C) `list3 = list[1, 2, 3]`
   D) `list4 = [1, 2, 3]`
   **Answer: A) `list1 = list()`, B) `list2 = []`, D) `list4 = [1, 2, 3]`**

10. **What is a correct syntax to return the first character in a string?** 

    A) `str[0]`
    B) `str.first()`
    C) `str.charAt(0)`
    D) `str[1]`
    **Answer: A) `str[0]`**

11. **How is memory managed in Python?** 

    A) Memory management is done manually by the programmer.
    B) Python uses an automatic garbage collector.
    C) Python's memory management is handled through Windows Memory Management.
    D) Python programs run inside a virtual machine which manages memory automatically.
    **Answer: B) Python uses an automatic garbage collector.**

12. **What is the result of the following code snippet?**

    ```python
    list = [x*x for x in range(5)]
    def fun(lst):
        del lst[lst[2]]
        return lst
    
    print(fun(list))
    ```

    A) `[0, 1, 4, 9, 16]`
    B) `[1, 4, 9, 16]`
    C) `[0, 1, 9, 16]`
    D) `[0, 1, 4, 16]`
    **Answer: C) `[0, 1, 9, 16]`**

13. **What does the `\*args` argument in Python functions signify?** 

    A) It signifies a syntax error.
    B) It stands for a single required argument.
    C) It represents an arbitrary number of positional arguments.
    D) It is used to pass a keyworded, variable-length argument dictionary.
    **Answer: C) It represents an arbitrary number of positional arguments.**

14. **In Python, what is the difference between `==` and `is`?** 

    A) No difference, both are used for equality checking.
    B) `==` checks for equality of value, whereas `is` checks for equality of identity (same object in memory).
    C) `==` is used for numerical comparisons, while `is` is used for string comparisons.
    D) `is` is an older version of `==` and is now deprecated.
    **Answer: B) `==` checks for equality of value, whereas `is` checks for equality of identity (same object in memory).**

15. **What will the following code print?**

    ```python
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)
    ```

    A) `[1, 2, 3]`
    B) `[1, 2, 3, 4]`
    C) `[4, 1, 2, 3]`
    D) Error
    **Answer: B) `[1, 2, 3, 4]`**

