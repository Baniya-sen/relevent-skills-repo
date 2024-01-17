const taskInput = document.getElementById('input-box');
const listContainer = document.getElementById('list-container');
const addBtn = document.querySelector("button");

addBtn.addEventListener('mousedown', () => {
    addBtn.style.transform = "scale(0.9)";
});

addBtn.addEventListener('mouseup', () => {
    addBtn.style.transform = "scale(1)";

    if (taskInput.value === '') {
        alert('Please enter a task');
    } else {
        var li = document.createElement("li");
        var span = document.createElement("span");

        li.innerHTML = taskInput.value;
        span.innerHTML = "\u00d7";
        
        li.appendChild(span);
        listContainer.appendChild(li);
    }

    taskInput.value = "";
    saveData();
});

listContainer.addEventListener('click', function(e) {
    if (e.target.tagName === "LI") {
        e.target.classList.toggle("checked");
        saveData();
    } else if (e.target.tagName === "SPAN") {
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function saveData() {
    localStorage.setItem("data", listContainer.innerHTML);
}

function getTasks() {
    listContainer.innerHTML = localStorage.getItem("data");
}

getTasks();
