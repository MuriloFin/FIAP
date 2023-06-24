function calcular(conta){
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);
    var resultado;


if (conta === 'soma') {
    resultado = num1 + num2;
} else if (conta === 'subtracao'){
    resultado = num1 - num2;    
} else if (conta === 'multiplicacao'){
    resultado = num1 * num2;
} else if (conta === 'divisao') {
    if (num2 === 0) {
        alert('Não é possível efetuar a divisão por zero')
    } else {
        resultado = num1 / num2;
    }
}
document.getElementById('resultado').innerHTML = "O resultado é: " + resultado;
}
