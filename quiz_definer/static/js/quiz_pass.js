let pos = -1;
let res = 0;
var questions = JSON.parse(document.getElementById("p").children[0].textContent);

function answer(value){
    res += parseInt(value);
    pos++;
    if(pos >= questions.length){
        window.location.href = `${document.querySelector('h1').textContent}/${res}`;
        return 0;
    }
    const question = questions[pos];
    document.querySelector(".question").children[0].textContent = question['question'];
    const answers = question['answers'];
    const answersList = document.querySelectorAll(".answer");
    for(let i = 0; i < answers.length; i++){
        answersList[i].textContent = answers[i]['text'];
        answersList[i].onclick = function() { answer(answers[i]['value']); }
    }
}