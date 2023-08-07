text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
x = text.replace(""",""",""" """).replace(""".""",""" """)
y = list(map(len,(x.split())))
s = ""
s_y =[str(n) for n in y]
print(s.join(s_y))

