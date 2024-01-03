# 

def greet(language):
    langs = {   
            ("english", "Welcome")
            , ("czech", "Vitejte")
            , ("danish", "Velkomst")
            , ("dutch", "Welkom")
            , ("estonian", "Tere tulemast")
            , ("finnish", "Tervetuloa")
            , ("flemish", "Welgekomen")
            , ("french", "Bienvenue")
            , ("german", "Willkommen")
            , ("irish", "Failte")
            , ("italian", "Benvenuto")
            , ("latvian", "Gaidits")
            , ("lithuanian", "Laukiamas")
            , ("polish", "Witamy")
            , ("spanish", "Bienvenido")
            , ("swedish", "Valkommen")
            , ("welsh", "Croeso")
            }
    
    if language in langs:
        return langs.get(language)
    else:
        return 'Welcome!'
    
print(greet("english"))
print(greet("spanish"))
print(greet("french"))
print(greet("catalan"))