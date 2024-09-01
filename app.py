from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

ai_quotes = [
    {
        "id": 0,
        "author": "Aleksei Ivanov",
        "qoute": "Hi, I am Aleksei" +
                    "Kto ty?"
    },
    {
        "id": 1,
        "author": "Katy Ivanova",
        "qoute": "Prosto fraza"
    },
    #Далее, наверно, будут цитаты из интернета
    {
        "id": 2,
        "author": "Kevin Kelly",
        "quote": "The business plans of the next 10,000 startups are easy to forecast: " +
                 "Take X and add AI."
    },
    {
        "id": 3,
        "author": "Stephen Hawking",
        "quote": "The development of full artificial intelligence could " +
                 "spell the end of the human race… " +
                 "It would take off on its own, and re-design " +
                 "itself at an ever increasing rate. " +
                 "Humans, who are limited by slow biological evolution, " +
                 "couldn't compete, and would be superseded."
    },
    {
        "id": 4,
        "author": "Claude Shannon",
        "quote": "I visualize a time when we will be to robots what " +
                 "dogs are to humans, " +
                 "and I’m rooting for the machines."
    },
    {
        "id": 5,
        "author": "Elon Musk",
        "quote": "The pace of progress in artificial intelligence " +
                 "(I’m not referring to narrow AI) " +
                 "is incredibly fast. Unless you have direct " +
                 "exposure to groups like Deepmind, " +
                 "you have no idea how fast — it is growing " +
                 "at a pace close to exponential. " +
                 "The risk of something seriously dangerous " +
                 "happening is in the five-year timeframe." +
                 "10 years at most."
    },
    {
        "id": 6,
        "author": "Geoffrey Hinton",
        "quote": "I have always been convinced that the only way " +
                 "to get artificial intelligence to work " +
                 "is to do the computation in a way similar to the human brain. " +
                 "That is the goal I have been pursuing. We are making progress, " +
                 "though we still have lots to learn about " +
                 "how the brain actually works."
    },
    {
        "id": 7,
        "author": "Pedro Domingos",
        "quote": "People worry that computers will " +
                 "get too smart and take over the world, " +
                 "but the real problem is that they're too stupid " +
                 "and they've already taken over the world."
    },
    {
        "id": 8,
        "author": "Alan Turing",
        "quote": "It seems probable that once the machine thinking " +
                 "method had started, it would not take long " +
                 "to outstrip our feeble powers… " +
                 "They would be able to converse " +
                 "with each other to sharpen their wits. " +
                 "At some stage therefore, we should " +
                 "have to expect the machines to take control."
    },
    {
        "id": 9,
        "author": "Ray Kurzweil",
        "quote": "Artificial intelligence will reach " +
                 "human levels by around 2029. " +
                 "Follow that out further to, say, 2045, " +
                 "we will have multiplied the intelligence, " +
                 "the human biological machine intelligence " +
                 "of our civilization a billion-fold."
    },
    {
        "id": 10,
        "author": "Sebastian Thrun",
        "quote": "Nobody phrases it this way, but I think " +
                 "that artificial intelligence " +
                 "is almost a humanities discipline. It's really an attempt " +
                 "to understand human intelligence and human cognition."
    },
    {
        "id": 11,
        "author": "Andrew Ng",
        "quote": "We're making this analogy that AI is the new electricity." +
                 "Electricity transformed industries: agriculture, " +
                 "transportation, communication, manufacturing."
    }
]
class Qoute(Resource):
    def get(self, id = 0):
        if id == 0:
            return random.choice(ai_quotes), 200
        for qoute in ai_quotes:
            if(qoute["id"] == id):
                return qoute, 200
        return "Qoute not found", 404
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("qoute")
        params = parser.parse_args()
        for qoute in ai_quotes:
            if(id == qoute["id"]):
                return f"Qoute with id {id} alredy exists", 400
        qoute = {
            "id": int(id),
            "author": params["author"],
            "qoute": params["qoute"]
        }
        ai_quotes.append(qoute)
        return qoute, 201
    def put(self, id):
        parser = reqparse.RequestParser
        parser.add_argument("author")
        parser.add_argument("qoute")
        params = parser.parse_args()
        for qoute in ai_quotes:
            if(id == qoute["id"]):
                qoute["author"] = params["author"]
                qoute["qoute"] = params["qoute"]
                return qoute, 200
        qoute = {
            "id": id,
            "author": params["author"],
            "qoute": params["qoute"]
        }
        ai_quotes.append(qoute)
        return qoute, 201
    def delete(self, id):
        global ai_quotes
        ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
        return f"Qoute with id {id} id deleted.", 200

api.add_resource(Qoute, "/ai-qoute", "/ai-qoute/", "/ai-qoute/<int:id>")
if __name__ == '__name__':
    app.run(debug=True)