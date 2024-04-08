let loadUserData = () => {
	return (
		JSON.parse(localStorage.getItem("data")) || {
			loggedInUser: "null",
			loggedInName: "null"
		}
	);
};

let appState = loadUserData();

const getData = async () => {

	document.getElementById("displayHandle").innerText =
		`@${appState.loggedInUser}`;
	document.getElementById("displayName").innerText =
		`${appState.loggedInName}`;
}

getData();

let textArea = document.getElementById('contentsBox');
let charCountArea = document.getElementById('charCountArea');
let tweetList = []
let id = 0;

let countChar = () => {
    let remainingChar = 140 - textArea.value.length;
    
	charCountArea.innerHTML = remainingChar;
	charCountArea.style.color = remainingChar < 0 ? 'red' : 'white';
}

textArea.addEventListener('input', countChar);
