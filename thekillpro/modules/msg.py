import os
from VCPlayBot.config import SOURCE_CODE
from VCPlayBot.config import ASSISTANT_NAME
from VCPlayBot.config import PROJECT_NAME
from VCPlayBot.config import SUPPORT_GROUP
from VCPlayBot.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info.\n\n Join @Girls_And_Boys_Chatting"
      HELP_MSG = [
        ".",
f"""
**Hola Bienvenido de nuevo a {PROJECT_NAME}

⚪️ {PROJECT_NAME}puede reproducir musica en tu videochat grupal

⚪️ Nombre del asistente>> @{ASSISTANT_NAME}\n\nClick para ver las instrucciones**

""",

f"""
**Configuración**

1) Hazte administrador del bot (Grupo y en el canal si usas cplay)
2) Inicia un chat de voz
3) Prueba /play [nombre de la canción] por primera vez por un admin
*) Si el bot se ha unido a la música, si no añade a @{ASSISTANT_NAME} a su grupo y vuelve a intentarlo

**Para la reproducción de la música del canal**
1) Hazme admin de tu canal 
2) Envía /userbotjoinchannel en el grupo vinculado
3) Ahora envía los comandos en el grupo vinculado
""",
f"""
**Comandos**

**=>> Reproducción de la canción 🎧**

- /reproducir: Reproduce la canción solicitada
- /play [yt url] : Reproduce la url yt dada
- /play [reply yo audio]: Reproduce el audio respondido
- /splay: Reproduce la canción a través de jio saavn
- /ytplay: Reproducir directamente la canción a través de Youtube Music

**=>> Reproducción ⏯**

- /player: Abrir el menú de configuración del reproductor
- /skip: Salta la pista actual
- /pausa: Pausa la pista
- /reanudar: Reanuda la pista pausada
- /finalizar: Detiene la reproducción multimedia
- /actual: Muestra la pista actual en reproducción
- /lista de reproducción: Muestra la lista de reproducción

*El cmd del reproductor y todos los demás cmds, excepto /play, /current y /playlist, son sólo para los administradores del grupo.
""",

f"""
**=>> Canal de reproducción de música 🛠**

⚪️ Sólo para administradores de grupos vinculados:

- /cplay [nombre de la canción] - reproduce la canción que has solicitado
- /csplay [nombre de la canción] - reproducir la canción que solicitó a través de jio saavn
- /cplaylist - Muestra la lista de canciones en reproducción
- /cccurrent - Muestra la reproducción actual
- /cplayer - abrir el panel de configuración del reproductor de música
- /cpause - pausa la reproducción de la canción
- /cresume - reanudar la reproducción de la canción
- /cskip - reproducir la siguiente canción
- /cend - detener la reproducción de la música
- /userbotjoinchannel - invitar al asistente a su chat

channel también se puede utilizar en lugar de c ( /cplay = /channelplay )

⚪️ Si no te gusta jugar en grupo vinculado:

1) Obtenga su ID de canal.
2) Crear un grupo con el título: Channel Music: your_channel_id
3) Añade el bot como administrador del canal con todos los permisos
4) Añade a @{ASSISTANT_NAME} al canal como administrador.
5) Simplemente envía los comandos en tu grupo. (recuerda usar /ytplay en lugar de /play)
""",

f"""
**=>> Más herramientas 🧑🔧**

- /musicplayer [on/off]: Activar/desactivar el reproductor de música
- /admincache: Actualiza la información del admin de tu grupo. Prueba si el bot no reconoce al admin
- /userbotjoin: Invita a @{ASSISTANT_NAME} Userbot a tu chat
""",
f"""
**=>> Descarga de la canción 🎸**

- /video [nombre de la cancion]: Descarga de la canción de vídeo de youtube
- /canción [nombre de la canción]: Descargar canción de audio desde youtube
- /saavn [nombre de la canción]: Descargar canción desde saavn
- /deezer [nombre de la canción]: Descargar canción desde deezer

**=>> Herramientas de búsqueda 📄**

- /search [nombre de la canción]: Buscar canciones en youtube
- /lyrics [nombre de la canción]: Obtener la letra de la canción
""",

f"""
**=>> Comandos para los usuarios de Sudo ⚔️**

 - /userbotleaveall - eliminar el asistente de todos los chats
 - /broadcast <reply to message> - emite globalmente el mensaje respondido a todos los chats
 - /pmpermit [on/off] - activar/desactivar el mensaje pmpermit
*Los usuarios de Sudo pueden ejecutar cualquier comando en cualquier grupo
"""
      ]
