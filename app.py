# importing files and required libraries 
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
# Create an app from Flask
app = Flask(__name__)
# Create an instance of the ChatBot class
bot = ChatBot("Candice")
#Create a new trainer for the Chatbot
trainer = ChatterBotCorpusTrainer(bot)
# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english')
#app routing is used to map the specific URL with the associated #function that is intended to perform some tasks. Such as to access #partcular page
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run()
