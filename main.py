import discord
from googletrans import Translator

#Thanks to the discord.py document and stackoverflow help
#A discord bot that target an user and replace all their message into japanese

#Process of different events
class EventSystem(discord.Client):
    #The bot is ready and connected
    async def on_ready(self):
        print(f'Logged! Name: {self.user}')
        
    #When the bot see a message passing    
    async def on_message(self, message):
        #print('message!!')
        #The event is only processed if the user sending the message is the right one
        if(message.author.id =='targerID'): 
            #print('you!!')
            #take the message and translate it into japanese thanks to the Translator initiated at the bottom part
            result = translator.translate(message.content, dest='ja', )
            #The message that we want to send is the Japanese translation and the original message for people to understand
            end_message = result.text + '(' + result.origin + ')'

            #If the original message wasn't a reply to someone
            if(message.reference == None):
                #We just send the final message
                await message.channel.send(end_message)
            #Otherwise it was a reply
            else:
                #We recover the message that was replied, with the reference id and the fetch fonction
                ref_message = await message.channel.fetch_message(message.reference.message_id)
                #then we make a reply ourselves to that message
                await ref_message.reply(end_message, mention_author = True)
            #In both cases we delete the message sent
            await message.delete()


#Initialisation
intents = discord.Intents.default()
intents.message_content = True
translator = Translator()

client = EventSystem(intents=intents)
client.run('botToken')