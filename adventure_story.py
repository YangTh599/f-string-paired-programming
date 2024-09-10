# Thayer Yang
# 10 SEP 2024
# f-String Adventure Story

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information:

     - the hero's first name
     - the setting of the story (e.g., forest, desert, cave system)
     - the object the hero finds while on his/her adventure

3. Assign each piece of information collected to a variable with a short, specific name.

4. Declare (create) a variable named `story` and assign to it the `f-string` that is your adventure story

5. Use the `print( )` function to display your adventure story on the screen.

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''

hero_name = input("What is your hero's name? \n")
setting = input("Where does your journey begin? Whats the setting? \n")
item = input("What object will your hero collect? \n")

if setting[0:1] == "a":
    story = f'Somewhere in {setting}, a hero suddenly appears. Their name.. {hero_name.capitalize()}! {hero_name.capitalize()} rose from their sudden spawnpoint, and at their feet they pick up a {item.lower()}.'

elif setting[0:1] == "A":
     story = f'Somewhere in a {setting[2:len(setting)]}, a hero suddenly appears. Their name.. {hero_name.capitalize()}! {hero_name.capitalize()} rose from their sudden spawnpoint, and at their feet they pick up a {item.lower()}.'
else:
     story = f'Somewhere in a {setting}, a hero suddenly appears. Their name.. {hero_name.capitalize()}! {hero_name.capitalize()} rose from their sudden spawnpoint, and at their feet they pick up a {item.lower()}.'


print("\n"+story)