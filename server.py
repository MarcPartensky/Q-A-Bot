#!/usr/bin/env python
"""
Restful api for using the transformers library in pypi.
This library could be used to do remote questions answering,
text summarization and will be used in my own website and discord bot.
"""
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

from transformers import pipeline

import html2text

nlp = pipeline("question-answering")
context_parser = reqparse.RequestParser()

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    """Implement flask restful resource for testing."""

    def get(self):
        """Return hello world"""
        return {'hello': 'world'}

contexts = {}

# class QuestionAnswering(Resource):
#     """Answer your questions given a context."""

#     def post(self, id=None):
#         """Post a context."""
#         if not id
#         id = len(contexts)
#         contexts[id] = parser.parse_args()
#         return id

#     def put(self, id):
#         """Change a context."""
#         contexts[id] = parser.parse_args()

#     def delete(self, id):
#         """Delete a context."""
#         del contexts[id]

#     def get(self, id, question:str):
#         """Answer a question about the context."""
#         return npl(question=question, context=contexts[id])

# class QuestionAnswering()

class Context(Resource):
    """Store of contexts."""
    def post(self, id=None):
        """Post a context."""
        if not id:
            id = len(contexts)
        contexts[id] = context_parser.parse_args()
        return id

    def get(self, id):
        """Return a context."""
        return contexts[id]

test_parser = reqparse.RequestParser()
test_parser.add_argument('context')
test_parser.add_argument('question')

class Ask(Resource):
    """Test transformers."""
    def post(self):
        """Ask a question about a context."""
        args = test_parser.parse_args()
        if 'context' in args:
            context = args['context']
        elif 'url' in args:
            url = args['url']
            text = requests.get(url).text
            context = h2t.handle(text)
        else:
            raise Exception
        if 'question' in args:
            response = nlp(args['question'], context)
        elif 'questions' in args:
            response = [npl(question, context) for question in args['questions']]
        else:
            raise Exception
        return response
# api.add_resource(QuestionAnswering, '/ask/<string:id>/')
# api.add_resource(Context, '/context/<string:id>')


api.add_resource(HelloWorld, '/')
api.add_resource(Ask, '/ask')

if __name__ == '__main__':
    app.run(debug=True)
