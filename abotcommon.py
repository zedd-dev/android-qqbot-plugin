class Context:
    def __init__(self, bot, contact, member, content):
        self.bot = bot
        self.contact = contact
        self.member = member
        self.content = content

def send(context, text):
    context.bot.SendTo(context.contact, text, resendOn1202=True)