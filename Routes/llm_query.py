from flask import Blueprint, render_template, request
from LLM.main import get_question_answer

llm_query = Blueprint('llm-query', __name__)


@llm_query.route('/view/llm-query', methods=['GET'])
def get_query_view():
    return render_template('llm-query.html')


@llm_query.route('/api/llm-books', methods=['GET'])
def question_answer():
    question = request.args.get('question')
    answer = get_question_answer(question)
    return answer
