import nltk
from nltk.chat.util import  reflections
import train_dataset as td
from module4 import ChatBot
from googletrans import Translator
import random
import re


reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
    "application":"form",
    "college":"campus",
}

global inp_mth

class Chat:
    def __init__(self, pairs, reflections={}):
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()


    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):

        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response

    def respond(self, str):

        for (pattern, response) in self._pairs:
            match = pattern.match(str)


            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                return resp

    def converse(self, quit="quit"):
        user_input = ""
        translator=Translator()
        while user_input != quit:
            inp_mth=int(input("text/speech/?(1=speech,2=text): "))
            lang=input("'en'-English,'hi'-Hindi,'ja'-Japanese,'ml'-Malayalam: ")
            user_input = quit
            try:
                # user_input = input(">")
                if(inp_mth==1):
                    temp=ChatBot(name="Gojo")
                    user_input=translator.translate(ChatBot.speech_to_text( temp),src=lang,dest='en').text
                elif(inp_mth==2):
                    user_input=translator.translate(input("Enter text: "),src=lang,dest='en').text
                else:
                    print("Sorry, Wrong input was entered..")
                    return

            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                print(translator.translate(self.respond(user_input),dest=lang).text)

def chat():
    print("Hi! I am  Gojo Satoru made by Team Gojo....")
    chat1 = Chat(td.pairs, reflections)    
    chat1.converse()

if __name__ == "__main__":
    chat()