# Sistema Automático de Televigilancia

*Este sistema consiste en la vigilancia remota de sitios de interés, de manera que se puedan registrar y visualizar eventos de instrusión. Se desea crear una imagen a la medida para la Raspberry Pi 3 mediante Yocto Project, esta debe ser capaz de detectar eventos de intrusión (detección de objetos vivos que se mueven) y tener un registro de las intrusiones detectadas durante el día, además, la imagen también debe permitir una conexión a un servidor mediante el protocolo SSH para la visualización del video desde un centro de monitoreo. La descripción del sistema se puede visualizar en un diagrama que se encuentra en: https://github.com/bryansh08/Sistema-de-Televigilancia/blob/master/Concepto_Operaciones.pdf* 

## Proceso de Desarrollo del Sistema 🚀
* *El primer paso es crear la imagen para la raspberry pi 3*
* *Después de construida la imagen, agregamos las capas y recetas necesarias*

### Pre-requisitos para la Construcción de la Imagen 📋
*Para poder crear la imagen se debe cumplir con los siguientes requisitos*

* git versión 1.7.8 o mejor 
* tar versión 1.24 o mejor
* python versión 2.7.3 o mejor **(python 3.x no es soportado)**

### Proceso de Construcción de la Imagen 🛠️
*Una vez cumplido los requisitos, se procede a construir la imagen*

Se instala una lista de paquetes esenciales, gráficos de soporte y documentación y extras. Se utiliza el siguiente comando debido a la distribución de linux utilizada **(Ubuntu18.04.4)**.
```bash
$sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essentials chrpath socat libsdl1.2-dev xterm
 ```
Se clona la versión de poky deseada, en este caso se clonó **poky-sumo-19.0.1** mediante el siguiente comando
```bash
$git clone git://git.yoctoproject.org/poky
$git checkout sumo 
 ```
Obtenida la carpeta de poky, se accede a ella con el comando `cd` y dentro de la misma se clona el paquete de soporte **(BSP)** para Raspberry Pi 
```bash
$git clone -b sumo git://git.yoctoproject.org/cgit.cgi/meta-raspberrypi
 ```
Dentro de la carpeta de poky, se crean dos carpetar con el comando `mkdir`, una carpeta para la construcción de la imagen llamada *rpi2* y otra para las descargar que conlleva la construcción de la imagen llamada *downloads*. Una vez obtenidas las carpetas, se ejecuta el siguiente comando para la configuración del ambiente de Yocto
```bash
$source oe-init-build-env rpi2
 ```
Ejecutado este comando, se creará una carpeta dentro de *rpi2* llamada *conf*, dentro de esta se accede al archivo *local.conf* y se agregan las siguientes líneas al final
```bash
MACHINE ?= "raspberrypi3"
INHERIT += "rm_work"
DL_DIR ?= "/home/usuario/poky-sumo-19.0.1/donwloads"
```
Además, se accede al archivo *bblayers.conf*, el cual también se encuentra junto a *local.conf* y se agrega la capa *meta-raspberrypi* clonada anteriormente. Una vez finalizado este proceso se puede ejecutar el *bitbake* con el tipo de imagen deseado, en el caso de este proyecto de generó una imágen base 
```bash
$bitbake core-image-base
```
Terminado este proceso podemos cargar nuestra imagen en la tarjeta SD y botear la imagen desde la plataforma.

### Capas y Recetas Instaladas en la Imagen 📦
Las capas y recetas que se requerían, fueron consultadas en la página http://layers.openembedded.org/layerindex/branch/sumo/layers/. Las capas agregadas se encuentran en el archivo *bblayer.conf* y las recetas fueron agregadas en el archivo *local.conf*. La capa *meta-progra* es una capa personalizada, desarrollada para la inclusión de la aplicación en python. 

### Aplicación en Python 💻
La aplicación de desarrolló en tres partes: la primera parte era un programa que permitía la captura de video desde la cámara conectada a la Raspberry Pi 3, el segundo programa permite la detección de movimiento junto al reconocimiento facial para el informe de inclusiones y el último programa es una interfaz gráfica para que el sistema sea amigable con el usuario.

### Problemas Encontrados ❌
* De los programas mencionados anteriormente, solamente fue posible instalar uno en la imagen, el programa de detección de intrusión, a pesar de ser implementado dentro de *meta-progra* no fue posible ejecutarlo dentro de la Raspberry Pi 3 debido a problemas provenientes de los archivos *Haarcascade.xml* los cuales son necesarios para la detección, además, la interfaz gráfica hace uso de *tkinter*, módulo que, aunque fue incluido en el *local.conf*, la imagen nuna fue capaz de reconocer el módulo.
* En un inicio el proyecto fue pensado para ser desarrollado en QEMU, sin embargo, no encontramos la manera de detectar la cámara para el desarrollo del sistema de vigilancia, por esta razón cambiamos a la Raspberry Pi 3.
