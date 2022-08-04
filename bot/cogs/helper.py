from discord import Game as DiscordGame
from discord.ext import commands

from bot.bot import PREFIX

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

AUTHOR = config["INFO"]["Author"]
VERSION = config["INFO"]["Version"]

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        presence = f"{PREFIX}help | ver {VERSION}"
        await self.bot.change_presence(activity=DiscordGame(name=presence))

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f"Current ping: {round(self.bot.latency * 1000)}ms")
    
    @commands.command(name="help")
    async def help(self, ctx):
        help_str = f"""```
[Name: {self.bot.user}]
[Version: {VERSION}]
[Author: {AUTHOR}]```"""
        await ctx.send(help_str)

def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Basic(bot))