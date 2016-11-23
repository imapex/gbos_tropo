from tropo import Session, Tropo
from flask import Flask, request, make_response
from flask_restful import Resource, Api
import json
import facts
import random
app = Flask(__name__)
api = Api(app)


def get_fact():
    """
    Returns a random fact regarding a mythical giant ball of string
    :return: str of fact
    """
    pool = facts.pool
    return pool[random.randint(0, len(pool)-1)]


class WebAPI(Resource):
    def post(self):
        print "processing incoming request"

        # Initialize a tropo object
        t = Tropo()

        # Deserialize the request
        s = Session(json.dumps(request.json))

        if hasattr(s, 'parameters'):
            # Handle the case where this is a new visitor to the site, we will initiate an outbound
            # SMS session to the visitor
            number = s.parameters['numberToDial']
            print "sending welcome msg to {}".format(number)
            t.call(number, network="SMS")
            t.say('Welcome to the Giant Ball of String! Please respond with "fact" for additional information')
        else:
            # Handle other scenarios
            if s.initialText:
                # Handle the case where the user sends us a text message
                if 'fact' in s.initialText.lower():
                    t.say(get_fact())

                else:
                    t.say(['Welcome to the Giant Ball of String',
                           'You can request facts by responding with the keyword "fact"'
                           ])
        return make_response(t.RenderJson())
api.add_resource(WebAPI, '/api/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
