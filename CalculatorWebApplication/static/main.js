
function appendToExpression(value) {
    document.getElementById('expression').value += value;
}

function clearExpression() {
    document.getElementById('expression').value = '';
}

function backspace() {
    let expression = document.getElementById('expression').value;
    document.getElementById('expression').value = expression.slice(0, -1);
}

function calculate() {
    
    const expression = document.getElementById('expression').value;
    try {
        const result = eval(expression);
        document.getElementById('expression').value = result;
    } catch (error) {
        document.getElementById('expression').value = 'Error';
    }
}

document.addEventListener('keydown', function (event) {
    const key = event.key;

    event.preventDefault();

    if (key === 'Backspace') {
        backspace();
    } else if (/[\d+\-*/%.]/.test(key)) {
        appendToExpression(key);
    } else if (key === 'Enter') {
        calculate(); 
    }
});



