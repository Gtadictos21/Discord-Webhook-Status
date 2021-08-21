from __future__ import print_function
from typing import Optional
import subprocess
import datetime
import psutil
import time
import math
import sys


from discord_webhook import DiscordWebhook, DiscordEmbed
import urllib.request
from uptime import uptime
from pythonping import ping

processName="EXAMPLE.py" # Nombre de archivo a controlar (Puede ser .jar/.js/.py/etc.)

# IP del servidor:
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

encontrado_og = False

def check_if_script_is_running(script_name):
    script_name_lower = script_name.lower()
    for proc in psutil.process_iter():
        try:
            for element in proc.cmdline():
                if element.lower() == script_name_lower:
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


while True:

    encontrado = check_if_script_is_running(processName)

    if not encontrado:
        print("Server OFF")
        if encontrado_og:

            # Ping a los servidores de Discord (Solo para verificar que la red se encuentre en condiciones) (https://support.discord.com/hc/es/articles/216740328--Windows-C%C3%B3mo-realizar-un-Traceroute-para-Discord)
            response_list = ping('brazil4777.discord.gg', size=40, count=10)

            embed_off = DiscordEmbed(title='¡{NOMBRE DEL SISTEMA AQUÍ} se ha desconectado!', description='Este proceso se encuentra 🔴', color=0xff0000)
            embed_off.add_embed_field(name="Uso de CPU:", value=f"{psutil.cpu_percent()}%", inline=False)
            embed_off.add_embed_field(name="Uso de RAM:", value=f"{math.ceil((psutil.virtual_memory()[3]/1024)/1024)} MB ({psutil.virtual_memory()[2]}%)", inline=False)
            embed_off.add_embed_field(name="Ping:", value=f"{response_list.rtt_avg_ms} ms", inline=False)
            embed_off.set_footer(text=f'IP: {external_ip} | Server uptime: {math.ceil(uptime()/3600)} horas')
            embed_off.set_thumbnail(url='') # INSERTAR URL DE LOGO
            embed_off.set_timestamp()
            webhook_off = DiscordWebhook(url='INSERTAR TU URL DE WEBHOOK AQUÍ',embeds=[embed_off])
            response_off = webhook_off.execute()
            encontrado_og = False

            
    elif encontrado:
        print("Server ON")
        if not encontrado_og:

            # Ping a los servidores de Discord (Solo para verificar que la red se encuentre en condiciones) (https://support.discord.com/hc/es/articles/216740328--Windows-C%C3%B3mo-realizar-un-Traceroute-para-Discord)
            response_list = ping('brazil4777.discord.gg', size=40, count=10)

            embed = DiscordEmbed(title='¡{NOMBRE DEL SISTEMA AQUÍ} se ha conectado!', description='Este proceso se encuentra 🟢', color=0x2bff00)
            embed.add_embed_field(name="Uso de CPU:", value=f"{psutil.cpu_percent()}%", inline=False)
            embed.add_embed_field(name="Uso de RAM:", value=f"{math.ceil((psutil.virtual_memory()[3]/1024)/1024)} MB ({psutil.virtual_memory()[2]}%)", inline=False)
            embed.add_embed_field(name="Ping:", value=f"{response_list.rtt_avg_ms} ms", inline=False)
            embed.add_embed_field(name="Ultima actualización:", value=f"<t:{int(datetime.datetime.now().timestamp())}:R>", inline=False)
            embed.set_footer(text=f'IP: {external_ip} | Server uptime: {math.ceil(uptime()/3600)} horas')
            embed.set_thumbnail(url='') # INSERTAR URL DE LOGO
            embed.set_timestamp()
            webhook = DiscordWebhook(url='INSERTAR TU URL DE WEBHOOK AQUÍ',embeds=[embed])
            response_on = webhook.execute()
            encontrado_og = True
        else:

            new_embed = DiscordEmbed(title='¡{NOMBRE DEL SISTEMA AQUÍ} se ha conectado!', description='Este proceso se encuentra 🟢', color=0x2bff00)
            new_embed.add_embed_field(name="Uso de CPU:", value=f"{psutil.cpu_percent()}%", inline=False)
            new_embed.add_embed_field(name="Uso de RAM:", value=f"{math.ceil((psutil.virtual_memory()[3]/1024)/1024)} MB ({psutil.virtual_memory()[2]}%)", inline=False)
            new_embed.add_embed_field(name="Ping:", value=f"{response_list.rtt_avg_ms} ms", inline=False)
            new_embed.add_embed_field(name="Ultima actualización:", value=f"<t:{int(datetime.datetime.now().timestamp())}:R>", inline=False)
            new_embed.set_footer(text=f'IP: {external_ip} | Server uptime: {math.ceil(uptime()/3600)} horas')
            new_embed.set_thumbnail(url='') # INSERTAR URL DE LOGO
            new_embed.set_timestamp()
            webhook.embeds = [new_embed]
            webhook.edit(response_on)

    time.sleep(60) # Hace un checkeo cada 60s, aunque esto se puede modificar.
