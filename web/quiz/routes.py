from . import app
from flask import jsonify, make_response
from .data import db_session
from .data.categories import Category
from .data.questions import Question
import requests
import datetime
import json

@app.route('/api/get_questions/<count>')
def get_questions(count):
    db_sess = db_session.create_session()
    data = requests.get(f"https://jservice.io/api/random?count={count}").json()
    answer = (db_sess.query(Question).all() or [None])[-1]
    cnt = 0
    for item in data:
        category = Category(title=item['category']['title'])
        if not db_sess.query(Category).filter(Category.title==category.title).first():
            db_sess.add(category)
        format = '%Y-%m-%dT%H:%M:%S.%fZ'
        question_object = Question(question=item['question'],
                                   created_date=datetime.datetime.strptime(item['created_at'],
                                                                           format))
        if not db_sess.query(Question).filter(Question.question==question_object.question).first():
            category.questions.append(question_object)
    db_sess.commit()
    if answer:
        return make_response(jsonify(answer.to_dict()), 200)
    return make_response(jsonify({}), 200)
