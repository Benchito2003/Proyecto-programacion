# Rama de desarrollo
Esta rama esta diseñada como un filtro de cambios con la principal, 

## Funcionalidades a añadir:
Recuerden que todas las ventanas tenemos que hacerlas como clases para poder ser usada en la ventana principal
- [x] Crear el frame de inicio
    - [ ] Añadir la animacion del corazon al frame de inicio
    - [ ] Añadir animación de inicio
- [x] Crear una ventana para ingresar el nombre del usuario
- [x] Crear la ventana principal de nuestro programa.
- [x] Crear una ventana para añadir un nuevo usuario.
- [x] Crear una función que nos permita obtener datos de los "entry".
- [x] Crear función que permita asegurarnos que los campos estén correctamente llenos.
- [x] Crear una función que nos permita generar un nombre de usuario aleatorio a partir de:
    - Las 2 primeras letras del nombre.
    - Las 2 primeras letras del apellido.
    - Un número aleatorio de dos dígitos.
- [ ] Crear dos data frames: una para datos de usuario (con los datos capturados) y otra para las  rutas donde estan guardadas las frecuencias cardiacas.
- [ ] Crear una función que permita guardar los datos capturados en la dataframe
- [ ] Crear un progama que permita obtener datos de sensor.
- [ ] Crear una ventana que permita graficar los pulsos cardiacos.

## Funcionalidades a aclarar:
- ¿Con qué paleta de colores trabajaremos?

## Sugerencias:
pueden editar esta sección del readme para dar sugerencias como: funcionalidades extra que se les hayan ocurrido, algun cambio de alguna venta, etc.

## ¿Cómo instalar?
1. Haz un  git clone de este repositorio con:
```git 
git clone <url-del-repositorio>
```
2.  Cambiate a tu rama (si no encuentras tu rama comunicate con Rubén para que te haga una)
```git 
git fetch
```
```git
git checkout <nombre-de-tu-rama> 
```


## Cómo subo mis cambios?
Muy fácil: 
```git
git push 
```
Te va a pedir un usuario y una contraseña, en usuario ponen su nombre y en contraseña pegan la llave de github que les mandé.

*¿Si cometo un error arruinare el trabajo de los demás?* Mientras estés en tu rama, puedes hacer y deshacer lo que quieras, pero si moviste sin querer algo de la rama principal o del desarrollo, podemos deshacer el cambio hasta el último punto de guardado.

## Ambientes (el archivo ".venv" que ven en vscode)
Para poder tener todas las librerias necesarias de putazo ejecutar el siguiente comando:


```python
pip install -r requirements.txt
```

## crear y activar entornos en python:
crear un entorno:
```python
python -m venv <nombre-entorno>
```

Activar un entorno:
```python
# windows
<nombre-entorno>\Scripts\activate

#Unix
source <nombre-entorno>/bin/activate
```

Desactivar un entorno:
```python
deactivate
```

## Documentación
### tkinter
- https://docs.python.org/es/3/library/tk.html
### Custom Tkinter
- https://customtkinter.tomschimansky.com/documentation/
### Matplotlib
- https://matplotlib.org/
### PIL
- https://pillow.readthedocs.io/en/stable/
### Pandas
- https://pandas.pydata.org/docs/