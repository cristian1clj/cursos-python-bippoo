a = [{'1':'hola', '2':'chao','3':'algo mas'}, {'7':'hola', '8':'chao','9':'algo mas'}]
b = [{'4':'4hola'}, {'5':'5chao'}, {'6':'6algo mas'}]

for values in a:
    if (values['8'] or values['3']) == "chao":
        print("siiii")
        break
     