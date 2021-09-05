COLOURS_DICT = {"aliceblue": '#f0f8ff', "antiquewhite": '#faebd7',
                "aquamarine1": '#7fffd4', "azure1": '#f0ffff',
                "beige": '#f5f5dc', "cadetblue3": '#7ac5cd',
                "chocolate": '#d2691e', "cornflowerblue": '#6495ed',
                "darkgoldenrod": '#b8860b', "darkgreen": '#006400'}

colour_name = input("Enter Colour: ")
while colour_name != "":
    print(COLOURS_DICT.get(colour_name))
    colour_code = input("Enter Colour: ")
