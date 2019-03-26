from utils import default

version = "v1.2.4"
invite = "https://discord.gg/DpxkY3x"
owners = default.get("config.json").owners
vpspriv = default.get("config.json").vpspriv


def is_owner(ctx):
    return ctx.author.id in owners

def is_vpspriv(ctx):
	return ctx.author.id in vpspriv