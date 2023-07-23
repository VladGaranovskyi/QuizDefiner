function getQuestionText(i){
    return `
        <label class="form-label">Question ${i}</label>
        <input type="text" name="q${i}" class="form-control" placeholder="Question text">
        <br>
        <div class="input-group mb-3">
          <span class="input-group-text">Answer</span>
          <input type="text" class="form-control" name="q${i}a1Text">
          <span class="input-group-text">Value</span>
          <input type="number" class="form-control" name="q${i}a1Value">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">Answer</span>
          <input type="text" class="form-control" name="q${i}a2Text">
          <span class="input-group-text">Value</span>
          <input type="number" class="form-control" name="q${i}a2Value">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">Answer</span>
          <input type="text" class="form-control" name="q${i}a3Text">
          <span class="input-group-text">Value</span>
          <input type="number" class="form-control" name="q${i}a3Value">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">Answer</span>
          <input type="text" class="form-control" name="q${i}a4Text">
          <span class="input-group-text">Value</span>
          <input type="number" class="form-control" name="q${i}a4Value">
        </div>`;
}

function getRangeText(i){
    return `<span class="badge bg-primary">Result Range ${i}</span>
          <div class="input-group mb-3">
            <span class="input-group-text">Left</span>
            <input type="number" class="form-control" name="left${i}">
            <span class="input-group-text">Right</span>
            <input type="number" class="form-control" name="right${i}">
          </div>
          <span class="badge bg-primary">Result Message</span>
          <textarea class="form-control" name="message${i}" rows="3"></textarea>`;
}

function getCountOfDivs(container){
    let res = 0;
    for(let i = 0; i < container.children.length; i++){
        if(container.children[i].tagName == "DIV"){
            res++;
        }
    }
    return res;
}

function getMaxScore(){
    let res = 0;
    const container = document.getElementById("questions");
    for(let i = 0; i < container.children.length; i++){
        if(container.children[i].tagName == "DIV"){
            const child = container.children[i];
            const id = child.id.slice(-1);
            let max = child.querySelector(`input[name="q${id}a1Value"]`).value;
            for(let i = 2; i <= 4; i++){
                if(child.querySelector(`input[name="q${id}a${i}Value"]`).value > max){
                    max = child.querySelector(`input[name="q${id}a${i}Value"]`).value;
                }
            }
            res += parseInt(max);
        }
    }
    return res;
}

function getMinScore(){
    let res = 0;
    const container = document.getElementById("questions");
    for(let i = 0; i < container.children.length; i++){
        if(container.children[i].tagName == "DIV"){
            const child = container.children[i];
            const id = child.id.slice(-1);
            let min = child.querySelector(`input[name="q${id}a1Value"]`).value;
            for(let i = 2; i <= 4; i++){
                if(child.querySelector(`input[name="q${id}a${i}Value"]`).value < min){
                    min = child.querySelector(`input[name="q${id}a${i}Value"]`).value;
                }
            }
            res += parseInt(min);
        }
    }
    return res;
}

function createQuestions(){
    const count = document.getElementById("questionCount").value;
    const container = document.getElementById("questions");
    if(count > getCountOfDivs(container)){
        for(let i = getCountOfDivs(container); i < count; i++){
            var question = document.createElement("div")
            question.id = "question" + (i + 1);
            question.innerHTML = getQuestionText(i + 1);
            container.appendChild(document.createElement("hr"));
            container.appendChild(question);
        }
    }
    else if(count < getCountOfDivs(container)){
        for(let i = getCountOfDivs(container); i > count; i--){
            container.removeChild(document.getElementById(`question${i}`));
            container.removeChild(container.lastElementChild);
        }
    }
}

function createRanges(){
    const count = document.getElementById("rangesCount").value;
    const container = document.getElementById("ranges");
    const badge = document.getElementById("maxmin");
    badge.textContent = `Min: ${getMinScore()}; Max: ${getMaxScore()}`
    if(count > getCountOfDivs(container)){
        for(let i = getCountOfDivs(container); i < count; i++){
            var range = document.createElement("div")
            range.id = "range" + (i + 1);
            range.innerHTML = getRangeText(i + 1);
            container.appendChild(document.createElement("hr"));
            container.appendChild(range);
        }
    }
    else if(count < getCountOfDivs(container)){
        for(let i = getCountOfDivs(container); i > count; i--){
            container.removeChild(document.getElementById(`range${i}`));
            container.removeChild(container.lastElementChild);
        }
    }
}