estoy_ocupado = False # cuando es Cero estoy trabajando cuando es uno estoy ocupado
cuarto_oscuro = False # cuando es cero estoy adentro cuando es uno estoy afuera

if estoy_ocupado and cuarto_oscuro:
    print("Estoy trabajando dentro del cuarto oscuro.")
elif estoy_ocupado and not cuarto_oscuro:
    print("Puedes ingresar, Estoy adendro del cuarto oscutro pero no estoy trabajando.")
elif not estoy_ocupado and not cuarto_oscuro:
    print("Puedes ingresar, Estoy afuera del cuarto oscutro pero estoy trabajando")
else:
    print("El cuarto está ocupado y hay luz.")


