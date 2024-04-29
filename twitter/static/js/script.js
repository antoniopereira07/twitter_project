// Pegar o textarea e a área de contagem de caracteres
let textArea = document.getElementById('contentsBox');
let charCountArea = document.getElementById('charCountArea');
let tweetList = []
let id = 0;

// Função para contar os caracteres
let countChar = () => {
	let remainingChar = 140 - textArea.value.length;
	
	if (remainingChar < 0) {
        charCountArea.innerHTML = remainingChar;
        charCountArea.style.color = 'red';
    } else {
        charCountArea.innerHTML = remainingChar;
        charCountArea.style.color = 'white';
    }
}

// Adicionar um ouvinte de evento para o input do textarea
textArea.addEventListener('input', countChar);
