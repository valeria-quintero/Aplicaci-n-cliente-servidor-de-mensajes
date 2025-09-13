# Cliente-Servidor
Este proyecto implementa un sistema de chat cliente-servidor utilizando sockets TCP en Python.
Reglas del protocolo: cuando el servidor recibe un mensaje, lo reenvía a todos los clientes conectados. Cuando recibe EXIT , desconecta al cliente y avisa al resto que salió. Todo cliente recibe mensajes en el mismo formato.
Varios clientes pueden conectarse al servidor.
