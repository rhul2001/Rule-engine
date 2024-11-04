from flask import Blueprint, request, jsonify
from backend.rule_engine import create_rule, evaluate_rule
from backend.database import save_rule

api = Blueprint('api', __name__)

@api.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule_string')
    ast = create_rule(rule_string)
    save_rule(rule_string, str(ast))
    return jsonify({'ast': str(ast)})

@api.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_string = request.json.get('rule_string')
    data = request.json.get('data')
    result = evaluate_rule(rule_string, data)
    return jsonify({'result': result})
