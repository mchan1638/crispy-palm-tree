#Pokemon Evolution Game

#Initialize
import random

#Global Variables
pokemon_level = 0
day = 0
evo = False
evo1 = False

#Functions
def charmander1():
    print("""⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜
⬜⬜⬛🟧⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜🟧🟧🟧⬛
⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛
⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛
⬜⬜⬜⬛🟧🟧⬛⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜
⬜⬜⬜⬛🟧🟧🟧⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛⬜⬜
⬜⬜⬜⬜⬛🟧🟧⬛⬛🟧🟧🟧⬛🟧🟧⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟧⬛🟧🟧🟧🟧🟧⬛🟧🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟨🟨🟨⬛⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧🟧🟧⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜🟧⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def charmander2():
    print("""⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟥⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟥🟥🟥⬛⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬛🟥🟥⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟥⬛⬜⬜⬜⬛⬛🟥🟥⬛🟥⬛⬜⬜⬜
⬜⬜⬜⬛⬛🟥🟨⬛⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬜⬛⬛🟥🟥⬛⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬛🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬜
⬛🟥🟥🟥⬛⬜⬜⬜⬜⬛⬛🟥🟥🟥⬜⬛🟥🟥🟥🟥🟥⬛
⬛🟥🟥🟥⬛⬜⬜⬛⬛🟥🟥⬛🟥⬛⬜⬛⬛🟥🟥🟥🟥⬛
⬛🟥🟥🟥🟥⬛⬛🟥🟥🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥🟥⬛⬜
⬛⬛🟥🟥🟥⬛🟥🟥🟥⬛🟥🟥🟥🟥⬛🟥🟥🟥⬛⬛⬜⬜
⬜⬛🟥🟥🟥🟥🟥⬛🟥⬛🟥🟥🏻🏻⬛⬛⬛⬛🟥🟥⬛⬜
⬜⬜⬛🟥⬛🟥🟥⬛🟥⬜⬛🏻🏻🏻⬛⬜⬜⬛🟥🟥⬜⬛
⬜⬜⬜⬛⬛🟥🟥⬛🟥🟥🟥⬛🏻⬛⬜⬜⬜⬜⬛⬜🟥⬛
⬜⬜⬜⬜⬛🟥🟥🟥⬛🟥⬜⬛🏻⬛⬛⬜⬜⬜⬜⬛⬛⬜
⬜⬜⬜⬜⬛⬛🟥🟥🟥⬛⬛🏻⬛🟥⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟥🟥🟥🟥⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟥⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜🟥⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def charmander3():
    print("""⬜⬜⬜⬜🟥🟥🟥🟨🟨🟨🟨🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🟥🟥🟥🟨🟥🟨🟥⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜🟥🟥🟧🟥🟨🟨⬜⬛🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜🟧🟧⬜🟥⬜⬜⬜🟥⬜🟧⬛⬜⬜⬜⬜⬜⬜🟧🟧🟧⬜⬜⬜
⬜⬜⬜⬜🟧🟧🟧🟧⬜⬜🟥⬜⬛🟥🟥🟥🟧⬛⬜⬜⬜⬜⬜🟧🟧🟧🟧⬜⬜
⬜⬜⬜🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬛🟥🟥🟧⬛⬛⬜⬜⬜⬜🟧🟦🟧🟧🟧⬜
⬜⬜⬜🟧🟧🟦🟧⬜⬜⬜⬜🏻🏻🏻🟥🟫🟧⬜⬛⬜⬜⬜🟧🟧🟦🟦🟦🟧⬜
⬜⬜🟧🟧🟦🟦🟧🟧⬜⬜⬜⬛🟪🏻🏻🟫🟧🟧🟧⬛⬜⬜🟧🟦🟦🟦🟦🟧🟧
⬜⬜🟧🟦🟦🟦🟧🟧⬜⬜⬛🟧⬛⬛⬛🟧🟧⬛🟧⬛⬜🟧🟧🟦🟦🟦🟦🟦🟧
⬜🟧🟧🟦🟦🟦🟧🟧⬜⬜⬜⬛🟧🟧🟧🟧⬛⬛🟧🟧⬛🟧🟧🟦🟦🟦🟥🟦🟧
⬜🟧🟦🟦🟦🟦🟧🟧⬜⬜⬜⬜⬛⬛⬛🟧⬛⬜⬛⬛⬛🟧🟦🟦🟥🟥🟦🟦🟧
🟧🟧🟦🟦🟦🟦🟦🟧🟧⬜⬜⬜⬛🟧🟧🟧⬛⬜⬜⬜🟧🟧🟦🟦🟥🟨🟦🟦🟥
🟧🟦🟦🟦🟦🟦🟦🟧🟧🟧⬜⬜⬛🟧🟧🟧⬛⬜⬜🟧🟧🟦🟦🟥🟥🟦🟥🟥🟥
🟧🟦🟦🟦🟦🟦🟦🟦🟧🟧🟧⬜⬛🟧🟧🟧⬛⬜🟧🟧🟧🟦🟦🟥🟨🟥🟨🟥🟧
🟧🟦🟦⬛⬜⬛🟦🟦🟦🟧🟧⬛🟧🟧🟧🟧⬛🟧🟧🟧🟦🟦🟦🟥🟨🟨🟥🟧🟥
🟧🟦⬜⬜🟧⬜⬛🟦🟦🟧⬛🟧🟧🟧🟧🟧🟧⬛🟧🟧🟦🟦🟥🟨🟨🟨🟨🟥🟧
🟧⬜⬜⬛🟧🟧⬛🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧⬛🟧🟦⬜⬜⬛🟥🟧🟨🟨🟧🟥
🟧⬜⬜⬜⬛🟧🟧⬛⬛🟧🟧🏻🏻🏻🏻🟧🟧🟧⬛🟦⬛🟧⬜🟥🟥🟧🟨🟨🟥
⬜⬜⬜⬜⬜⬛🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🟧🟧🟧⬛🟧🟧⬛🟦⬛🟧⬛🟥🟦
⬜⬜⬜⬜⬛⬛⬛⬛⬛🏻🏻🏻🏻🏻🏻🏻🟧⬛🟧🟧🟧⬛🟦⬜⬛🟧⬛⬜🟦
⬜⬜⬛⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧⬛⬛⬛🟦⬜⬛🟧🟧⬛⬜⬜
⬜⬛🟧🟧🟧🟧⬛⬛⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧⬛🟧🟧⬛⬛🟧🟧⬛⬜⬜⬜
⬜⬛🟧🟧🟧⬛🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜
⬜⬛🟧🟧⬛🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧⬛🟧🟧⬛⬜⬜⬜⬜⬜
⬜⬛🏻🟧⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬛🏻🏻🏻⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬛⬛🟧🟧🟧⬛🏻⬛⬛⬛⬛⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬜🟧🟧🟧🟧⬛🏻🏻🏻⬛⬜⬜⬜⬛🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜""")
def squirtle1():
    print("""⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜
⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🏿⬛⬛⬜⬛🟦🟦🟦⬛🟦🟦⬛
⬛🟫🟦🟦🟦🟦🟦🟦🟦🟦🏿🟫🏿⬛🟦🟦🟦⬛🟦🟦🟦⬛
⬛🟦🟦🟦🟦⬜⬛🟦🟦🟦🏽🟫🟫🏿⬛🟦🟦⬛🟦🟦⬛⬜
⬛🟦🟦🟦🟦⬛🟫🟦🟦🟦⬜🟫🟫🟫⬛🟦⬛⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦⬛🟫🟦🟦🟦⬛⬜⬜🟫🟫⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦⬛⬛🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟦⬛⬛⬛⬛🟦🟦🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟨🟨⬛🟦🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨⬛⬛⬛⬛🏽🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟦⬛🟫🟨🟨🟨🟫⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛🟫🟫🟦⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def squirtle2():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜
⬜⬜⬛⬜⬜⬛⬛⬛⬛⬜⬛⬜⬜⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛🟦🟦🟦🟦🟪🟪⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬛🟪🟦🟦🟦🟦🟦◼️⬜⬛⬜⬛⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜
⬜⬜⬛🟦🟦🟦🟦🟦🟦◼️⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜
⬜⬛🟦🟦🟦🟦🟦🟦⬛🟪⬛⬜⬜⬛🟨⬛⬜⬛⬜⬜⬛⬛⬜⬛⬜⬜
⬜⬛🟦🟦🟦🟦🟦⬛⬜🟦🟦⬛⬛🟫🟨🟫⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬛🟦🟦🟦⬛⬛⬜⬜🟦⬛⬜⬜🟫🟨⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬛🟦🟦🟦🟦🟫⬜🟦🟪⬛⬛⬜🟫🟨🟨⬛⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬛🟦⬛🟦🟪🟦🟦🟦⬛⬛🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬛⬜🟦⬛⬛⬛⬛⬛🟨⬛🟦🟦🟦⬜🟫🟨⬛⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬜⬛⬜🟨🟨⬛⬜🟦🟦⬛⬜🟫🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨⬛🟦⬜⬛⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟦⬛⬛🟨⬛⬛🟨⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟦🟦⬛⬛🟨🟨⬛🟦⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟪🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def squirtle3():
    print("""⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜🏽🏽⬛⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬜⬛⬜🟫🟫🟫🟫⬛⬛⬛🏽🏽⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟦⬛⬛🟫🟫🟫🟫🟫🟫⬛⬜⬛⬛🏽⬛⬜⬜⬜⬜
⬜⬜⬜⬛🟦🟦🟦⬛⬛🟫⬛⬛🟫⬜⬜⬛⬛🏽⬛⬜⬜⬜⬜
⬜⬜⬛🟦🟦🟦🟦🟦🟦⬛🟦⬛🟫⬜🏽🏽🏽⬛⬜⬜⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟫🟫🏽🏽⬛🟫⬛⬜⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦⬛🟦🟦⬛🏽🏽🏽⬛⬛🟫🟫⬛⬜⬜⬜⬜
⬛🟦🟦🟦🟦🟦⬛⬜🟦🟦🟦⬛⬛⬛⬛⬛🏽🟫🟫⬛⬛⬛⬛
⬛🟦🟦🟦🟦⬛⬛🟦🟦🟨🟦⬛⬛🟦🟦🟦⬛🏽🟫⬛🟦🟦⬛
⬛⬜🟦🟦🟦🟦🟦🟦🟨🟨⬛🏽⬛🟦🟦🟦⬛🏽🟫⬛🟦⬛⬜
⬜⬛🟨🟨🟦🟦🟨🟨🟨⬛🏽⬛🟦🟦🟦🟦⬛🏽🏽⬛⬛⬜⬜
⬜⬜⬛⬛⬜🟨🟨⬛⬛🟨⬛🟦🟦🟦🟦⬛🟦⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🟨🟨⬛⬜🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨⬛⬛🟦🟦⬛🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛🟨🟨⬛⬜⬛⬛⬛⬛🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨⬛🟨⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜🟦🟦⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
def bulbasaur1():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬜⬛⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜
⬜⬜⬛🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛🟦🟦🟦⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦⬜⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜⬜🟦🟦⬛🟦🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦🟦⬛🟥⬜🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
def bulbasaur2():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻🏻⬛🟥⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛🏻🏻🏻⬛🟥⬛🏽🏽⬛⬜⬜⬜
⬜⬜⬜⬛⬜⬛🏽🏽⬛🏻🏻⬛🟥🟥⬛⬛⬛🟩⬛⬜⬜
⬜⬜⬛🟦⬛🟩🟩⬛⬛⬛🏻🟥🟥⬛🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬛🟦🟦⬛⬛🟩🟩🏽⬛⬛⬛⬛⬛⬛⬛🟩🟩⬛⬜
⬜⬜⬛🟦🏽🟦🟦⬛⬛⬛🟩🟩⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬜⬛🟦🟦🏽🏽🟦🟦🟦🟦⬛⬛⬛🟩🟩⬛🟩🟩⬛🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🏽🟦🟦🟦🟦⬛🟩⬛🟩⬛🟩⬛⬛
⬛⬛🟦🟦🟦🏽🏽🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛🟩🟩⬛
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🏽🟦⬛⬛⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🏽🟦🌫️⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦⬛🟥🟥⬜🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
def bulbasaur3():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥🟨🟨⬛🟥🟨🟨🟥⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟥🟥🟥⬛⬛⬛🟥🟥🟨🟨🟥⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥🟥⬛⬛🟨🟨🟨⬛⬛⬛⬛🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥⬛⬛🟥🟥⬛⬛🟨🟨⬛🟥🟨⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟥🟨🟨🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟩⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛🟨🟨🟥🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛🟥🟥🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬛⬜⬜
⬜⬜⬜⬛🟦⬛⬛🟩⬛🟩🟩⬛⬛⬛🟥🟥🟥⬛⬛⬛⬛⬛⬛🟩⬛⬛⬜
⬜⬜⬜⬛🟦🟦⬛⬛⬛🟩⬛⬛🟩🟩⬛⬛⬛🟩⬛🟩🟩🟩⬛⬛🟩🟩⬛
⬜⬜⬜⬛🟦🟦🟦🟦🟦⬛⬛⬛⬛🟩🟩⬛🟩⬛⬛🟩⬛🟩🟩⬛🟩⬛⬛
⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛🟦⬛⬛🟩⬛🟩⬛🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬛🟩⬛🟩⬛
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦⬛🟦🟦🟦⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦🟦🟦⬛🟦🟦🌫️⬛⬜⬜
⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛🟦⬛🟦⬛🟦🌫️⬛⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦🟦🟦⬛⬜⬛⬛⬜⬜⬜⬜
⬜⬛⬛🟦🟦🟦🟦🟦⬛⬜⬜🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜""")

def evolve_pokemon():
    global evo
    global evo1
    global pokemon_level
    global pokemon_character
    global pokemon_name
    if pokemon_level == 5 or pokemon_level == 6 and evo == False: #evolution mechanics
        print(str(pokemon_name) + " is evolving!")
        if pokemon_character == "Charmander":
            charmander2()
            pokemon_character = "Charmeleon"
            evo = True
        elif pokemon_character == "Squirtle":
            squirtle2()
            pokemon_character = "Wartortle"
            evo = True
        elif pokemon_character == "Bulbasaur":
            bulbasaur2()
            pokemon_character = "Ivysaur"
            evo = True
    elif pokemon_level == 10 or pokemon_level == 11 and evo1 == False: #evolution mechanics
        print(str(pokemon_name) + " is evolving!")
        if pokemon_character == "Charmeleon":
            charmander3()
            pokemon_character = "Charizard"
            evo1 = True
        elif pokemon_character == "Wartortle":
            squirtle3()
            pokemon_character = "Blastoise"
            evo1 = True
        elif pokemon_character == "Ivysaur":
            bulbasaur3()
            pokemon_character = "Venusaur"
            evo1 = True

def pokemon_evolution_simulator():
    global evo
    global evo1
    global pokemon_level
    global pokemon_character
    global pokemon_name
    global day
    print("""Welcome to Pokemon Evolution Simulator!
    Which starter pokemon do you choose? (Charmander/Squirtle/Bulbasaur)""")
    pokemon_character = input("Which starter pokemon do you choose? (Charmander/Squirtle/Bulbasaur)")
    print("Congratulations! You picked " + str(pokemon_character) + "!") #choosing starter pokemon
    if pokemon_character == "Charmander":
        charmander1()
    elif pokemon_character == "Squirtle":
        squirtle1()
    elif pokemon_character == "Bulbasaur":
        bulbasaur1()
    pokemon_name = input("What would you like to name your new pokemon?") #naming pokemon
    print(str(pokemon_name) + " the " + str(pokemon_character) + "!")
    print(" ")
    while True:
        print("Please choose an activity. Day: " + str(day))
        print("""
        1. Train
        2. Gym Battle
        3. Rest (Display Info)
        4. End
        """)
        ans = input("Please choose an option (1/2/3/4)")

        if ans == "1": #train pokemon
            pokemon_level = pokemon_level + 1
            print("Your Pokemon has leveled up!")
            print("Level " + str(pokemon_level))
            print(" ")
        elif ans == "2": #enter gym battle
            print("Your pokemon is fighting!")
            print("...")
            fight = random.randint(0,2)
            if fight == 1:
                print("Your pokemon won!")
                pokemon_level = pokemon_level + 2
                print("Level " + str(pokemon_level))
                print(" ")
            else:
                print("Your pokemon lost...")
                print("Level " + str(pokemon_level))
                print(" ")
        elif ans == "3": #shows stats
            print("Here are your pokemon's stats:")
            print("Name: " + str(pokemon_name))
            print("Pokemon: " + str(pokemon_character))
            if pokemon_character == "Charmander":
                print(charmander1())
            elif pokemon_character == "Charmeleon":
                print(charmander2())
            elif pokemon_character == "Charizard":
                print(charmander3())
            elif pokemon_character == "Squirtle":
                print(squirtle1())
            elif pokemon_character == "Wartortle":
                print(squirtle2())
            elif pokemon_character == "Blastoise":
                print(squirtle3())
            elif pokemon_character == "Bulbasaur":
                print(bulbasaur1())
            elif pokemon_character == "Ivysaur":
                print(bulbasaur2())
            elif pokemon_character == "Venusaur":
                print(bulbasaur3())
            print("Level " + str(pokemon_level))
            print(" ")
        elif ans == "4": #quits game
            print(" ")
            print("Thank you for playing!")
            break
        day = day + 1
        evolve_pokemon()


#Main
pokemon_evolution_simulator()
