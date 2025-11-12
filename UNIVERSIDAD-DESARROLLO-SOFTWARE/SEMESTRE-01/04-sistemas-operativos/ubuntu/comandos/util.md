cd: cambiar de directorio- change directory
ls: listar directorio
ls -la: listar directorio con archivos ocultos
adduser: agregar usuario con perfiles
userradd: crear usuario sin perfiles
--------------------------------------------------------------
4   2   1
R   W   X
1   0   0

change mode
chmod <decimal del permiso> <nombre del directorio/archivo>

change owner
chown <user>:<group> .profile

superuser do
sudo

elevar a superusuario
sudo su

addgroup <nombre>
groupadd -g <id> <nuevo>
usermod -a -G <group> <user>

si el root es el owner de un archivo el resto de usuarios no puede escribir, usuarios.

etc/group

su - <usuario>

etc/shadow / informacion de usuario
etc/passwd // que puede o no hacer el usuario

passwd <usario> // cambiar el password


