## Examples: Python `input( )` Function

The `input( )` function lets you prompt the user for specific information.

The `input( )` function ALWAYS collects string data from the user.  In other words, if you prompt the user for a number (such as a person's age or the length of a room), you must **convert** the user's input into a number before you can do math with the user's input.

If you don't convert text input into a number when you want to do math in Python, you'll get an error when you run your code.

```python
# Example 1
# Prompting the user to enter the name of the town or city they live in
# TIP: Always give the user an example of the input you're prompting them for

city = input('Enter the name of the city you live in: (Example: Milwaukee)\n')

# Example 2
# Prompting the user to enter the name of the month they were born in
city = input('In what month were you born? (Example: October)\n')
```

