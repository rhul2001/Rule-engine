document.getElementById('ruleForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const rule = document.getElementById('rule').value;

    const response = await fetch('/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rule_string: rule })
    });

    const data = await response.json();
    alert('Rule Created: ' + JSON.stringify(data));
});

document.getElementById('dataForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const data = {
        age: parseInt(document.getElementById('age').value),
        department: document.getElementById('department').value,
        income: parseInt(document.getElementById('income').value),
        experience: parseInt(document.getElementById('experience').value),
    };

    const ruleString = document.getElementById('rule').value;
    const response = await fetch('/evaluate_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rule_string: ruleString, data })
    });

    const result = await response.json();
    document.getElementById('result').innerText = 'Eligibility: ' + result.result;
});
