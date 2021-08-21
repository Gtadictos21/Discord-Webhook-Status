# WebHook para verificar el estado de un proceso 
## Este proyecto fue creado por [Julián](https://github.com/Gtadictos21/) y [Galo](https://github.com/Galo223344/)

Este script de Python verifica e informa mediante los WebHooks de Discord el estado de un determinado proceso (Si el proceso está corriendo o nó). Ademas, muestra el uso del CPU, RAM, Ping (en ms) e IP del servidor en donde se encuentra, por no mencionar que se auto-actualiza para mostrar siempre los recursos utilizados mas recientes.

![Webhook](https://user-images.githubusercontent.com/83682754/130176128-ed76fdd5-787a-4c4f-a500-ce89d28065be.jpg)

## Instalar WebHook y sus dependencias:
¡Este WebHook requiere Python3 version: 3.9.x, y pip!
```
git clone https://github.com/Gtadictos21/Discord-Webhook-Status.git
```
```
pip install discord-webhook
```
```
pip install psutil
```
```
pip install pythonping
```
```
pip3 install uptime
```

**ATENCIÓN:** Tienen que agregar el [link a su WebHook](https://support.discord.com/hc/es/articles/228383668-Introducci%C3%B3n-a-los-webhook) en el codigo, y deben (si es que quieren tener un logo en el webhook) agregar un link a un logo/foto. Ademas, si quieren que el bot haga el ping a otro servidor (que no sea los servidores de Discord), también deben cambiar el dominio al cual el bot le hace ping, y por ultimo, **DEBEN CAMBIAR EL NOMBRE DEL PROCESO A REVISAR, EN LA [LINEA 16](https://github.com/Gtadictos21/Discord-Webhook-Status/blob/079e1c85cfe8001373fbd101206bb51c55c90ad4/webhook.py#L16)**. Claro que pueden personalizar cada mensaje, y pueden adaptarlo a sus necesidades.

Para ejecutar el WebHook: `python3 webhook.py`, o pueden hacerlo con [Systemd](https://github.com/Gtadictos21/Discord-Webhook-Status/blob/main/webhook.service) (recomendable)

Ultima actualización: 20/08/2021 por: [Julián](https://github.com/Gtadictos21/) (Gtadictos21)
