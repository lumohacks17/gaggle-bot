import discord

client = discord.Client()

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith(".role") and msg.channel.name == "roles":
        return_msg = "I don't know what that command is. Type \".role help\" for info about role commands."
        parts = msg.content.split()

        if len(parts) == 1:
            return_msg = "Type \".role help\" for info about role commands."
        elif len(parts) == 2 and parts[1] == "help":
            return_msg = HELP_MESSAGE
        elif len(parts) == 3:
            role = find_role(ROLE_MAP.get(parts[2], None), msg.channel.server.roles)
            if role is not None:
                if parts[1] == "add":
                    await client.add_roles(msg.author, role)
                    return_msg = "You have added the role: " + role.name
                elif parts[1] == "remove":
                    await client.remove_roles(msg.author, role)
                    return_msg = "You have removed the role: " + role.name

        await client.send_message(msg.channel, return_msg)

def find_role(name, roles):
    if name is not None:
        for r in roles:
            if name == r.name:
                return r
    return None

ROLE_MAP = {
    "winter_2019": "Winter 2019",
    "summer_2019": "Summer 2019",
    "interviewing": "Interviewing"
}
HELP_MESSAGE = """
Use ".role add [role]" to add a role.
Use ".role remove [role]" to remove a role.

Available roles:
   winter_2019
   summer_2019
   interviewing

Example:
.role add winter_2019
"""
TOKEN = "NDk5ODE5MTI0Mzc4MzA0NTEy.DqB1Xg.JAF_F-1VI_Y9Rs5wH_5mRiQsK0s"

client.run(TOKEN)

