# Rama de desarrollo
Esta rama esta diseñada como un filtro de cambios con la principal, 

## Funcionalidades a añadir:
Recuerden que todas las ventanas tenemos que hacerlas como clases para poder ser usada en 
- [ ] Crear una ventana para ingresar el nombre del usuario
- [ ] Crear una ventana para añadir un nuevo usuario (capturar: Nombre, Apellido, fecha de nacimiento, y crearle un nombre de usuario)
- [ ] Crear una base de datos o un data frame (mejor trabajaremos con lo que veamos que es más cómodo) con dos tablas: una para datos de usuario (con los datos capturados) y otra para las frecuencias cardiacas.
- [ ] Crear la ventana principal de nuestro programa (opciones para ver registros pasados, crear un nuevo registro, etc.)
- [ ] Crear un programa que funcione de intermediario entre nuestra base de datos y los programas: que permita traer datos de la base de datos en forma de datos con los que podamos trabajar y que permita tambien subir a la base de datos los registros que tomemos. 
- [ ] Hacer un programa que permita hacer CRUD (Create, Read, Update, Delete)de forma sencilla con la base de datos
- [ ] Crear una ventana que para calcular media, moda y mediana de un conjunto de datos
- [ ] Crear un progama que permita obtener datos de sensor (ya después con calma vemos si los mostramos en tiempo real)
- [ ] Crear una ventana que permita graficar los pulsos cardiacos.

## Funcionalidades a aclarar:
- ¿Que datos necesitamos del usuario?
- ¿Con qúe prefieren trabajar data frames o una base de datos?
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
Para poder todas las librerias necesarias de putazo ejecutar el siguiente comando:

### instalar los modulos necesarios para el entorno
```python
pip install -r requirements.txt
```

### crear y activar entornos en python:
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
### Custom Tkinter
- https://customtkinter.tomschimansky.com/documentation/
### tkinter
- https://docs.python.org/es/3/library/tk.html
