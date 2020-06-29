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
