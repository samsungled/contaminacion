import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user} y fui creado para dar consejos de la contaminacion!')


consejos = [
    'Usa bolsas reutilizables para tus compras',
    'Evita los productos de un solo uso como sorbetes y cubiertos de plastico'
]
efectos = [
    'puede aumentar el riesgo de infecciones respiratorias',
    'enfermedades cardíacas'
    'accidentes cerebrovasculares y cáncer de pulmón'
]
energia = [
    'Apaga el televisor si no lo están viendo. ',
    'Cuando cocines, alista de una sola vez todos los alimentos de la nevera'
    'Aprovecha al máximo la luz natural; utiliza la energía eléctrica sólo si la necesitas. '
]
@bot.command()
async def consejodeldia(ctx):
    consejo = random.choice(consejos)
    await ctx.send(consejo)

@bot.command()
async def efectoscontaminacion(ctx):
    consejo = random.choice(efectos)
    await ctx.send(efectos)

@bot.command()
async def ahorroenergia(ctx):
    consejo = random.choice(energia)
    await ctx.send(consejo)

# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    defcn = "La contaminación es la presencia de un constituyente, impureza o algún otro elemento indeseable que estropea"
    await ctx.send(defcn)

@bot.command()
async def plastico(ctx):
    defc = "La contaminación por plástico puede alterar los hábitats y los procesos naturales, reduciendo la capacidad de los ecosistemas para adaptarse al cambio climático, afectando directamente a los medios de vida de millones de personas, a su capacidad de producción de alimentos y a su bienestar social."
    await ctx.send(defc)

@bot.command()
async def reciclaje(ctx):
    await ctx.send(f'Instala recipientes específicos donde puedas dividir la basura: orgánica, vidrio, cartón, plásticos y residuos tóxicos. Separa correctamente los residuos e indica al recolector de basura como están clasificados. Lava los envases y las latas antes de tirarlas para evitar vertidos tóxicos en el agua')


bot.run()
