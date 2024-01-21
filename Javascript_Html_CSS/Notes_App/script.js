
document.addEventListener('DOMContentLoaded', () => {
    const notesContainer = document.querySelector('.notes-container');
    let notes;

    function showNotes() {
        // localStorage.removeItem('notes');
        notesContainer.innerHTML = localStorage.getItem('notes');
    }

    function updateStorage() {
        localStorage.setItem('notes', notesContainer.innerHTML);
    }

    document.querySelector('.createBtn').addEventListener('mousedown', () => {
        document.querySelector('.createBtn').style.transform = "scale(0.9)";
    });

    document.querySelector('.createBtn').addEventListener('mouseup', () => {
        document.querySelector('.createBtn').style.transform = "scale(1)";

        let inputBox = document.createElement('p');
        let inputBoxImage = document.createElement('img');

        inputBox.className = "input-box";
        inputBox.setAttribute('contenteditable', 'true');
        inputBoxImage.src = "images/delete.png";
        inputBox.appendChild(inputBoxImage);
        notesContainer.insertBefore(inputBox, notesContainer.firstChild);
    });

    notesContainer.addEventListener('input', () => {
        updateStorage();
    });

    notesContainer.addEventListener('click', (e) => {
        if (e.target.tagName === 'IMG') {
            const note = e.target.parentElement;
            note.classList.add('removing');
            
            note.addEventListener('transitionend', () => {
                note.remove();
                updateStorage();
            });
        }
    });

    document.addEventListener('keydown', event => {
        if (event.key === "Enter") {
            document.execCommand("insertlinebreak");
            event.preventDefault();
            updateStorage();
        }
    })

    showNotes();
});