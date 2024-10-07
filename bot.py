import random
import discord
import os
import requests
from discord.ext import commands
from bot_token import token
from parola_olustur import gen_pass


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def geridonusum(ctx):
    await ctx.send("Geri dönüşüm, hava kirliliği, yerlere plastik pil gibi atıkların atılması  gibi sorunların çözüm noktasıdır. Plastik, kağıt, cam, metal ve pilleri geri dönüşüm tesislerinde yeniden kullanılır hale getirilir. Bunları yapmak Dünya'mızı daha temiz bir hale getiririz.") 
    with open('M2L2\images\geridonusum.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def parola_ver(ctx, parola_uzunlugu = 8):
    parola = gen_pass(parola_uzunlugu)
    await ctx.send("Sizin için oluşturulan parola: " + parola)
    
@bot.command()
async def mem1(ctx):
    with open('M2L2\memler\mem1.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('M2L2\memler\mem2.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('M2L2\memler\mem3.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem4(ctx):
    with open('M2L2\memler\mem4.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def random_mem(ctx):
    memler = os.listdir('M2L2\memler')
    secilen_mem = random.choice(memler)
    with open(f'M2L2\memler/{secilen_mem}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    hayvanlar = os.listdir('M2L2\hayvanlar')
    secilen_hayvan = random.choice(hayvanlar)
    with open(f'M2L2\hayvanlar/{secilen_hayvan}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

# API

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command()
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def dog(ctx):
    '''dog komutunu çağırdığımızda, program kopek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

# def get_fox_image_url():    
#     url = 'https://randomfox.ca/floof/'
#     res = requests.get(url)
#     data = res.json()
#     return data['url']

# @bot.command()
# async def fox(ctx):
#     '''fox komutunu çağırdığımızda, program tilki_resmi_urlsi_al fonksiyonunu çağırır.'''
#     image_url = get_fox_image_url()
#     await ctx.send(image_url)

bot.run(token)