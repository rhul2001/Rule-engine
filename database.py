import sqlite3

def save_rule(rule_string, ast):
    conn = sqlite3.connect('data/rules.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS rules (rule_string TEXT, ast TEXT)')
    cursor.execute('INSERT INTO rules (rule_string, ast) VALUES (?, ?)', (rule_string, ast))
    conn.commit()
    conn.close()
