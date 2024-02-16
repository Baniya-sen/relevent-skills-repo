let gameBoard;
let currentPlayer;
let aiTurn = false;
let gameOver = false;
const board = document.getElementById('board');
const resetBtn = document.getElementById('resetBtn');
const description = document.querySelector(".description p");

function choosePlayer(player) {
    get_board();
    currentPlayer = player;
    document.getElementById("player-selection").style.display = "none";
    setTimeout(() => {
        document.getElementById("board-container").style.display = "block";
    }, 290);
}

async function get_board() {
    // Fetch initial board state
    const response = await fetch('/board');
    if (response.ok) {
        const data = await response.json();
        gameBoard = data.board;
        displayBoard(data.board);
        if (currentPlayer === 'O') {
            aiMove(data.board)
        }
    } else {
        alert('Error: Failed to load board');
    }
}

function displayBoard(boardState) {
    board.innerHTML = '';
    description.textContent = "Make your move..."
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cell = document.createElement('div');
            cell.classList.add('square');
            if (boardState[i][j] !== null) {
                cell.textContent = boardState[i][j];
                cell.classList.add(boardState[i][j] === 'X' ? 'player-X' : 'player-O');
            } else {
                cell.dataset.x = i;
                cell.dataset.y = j;
                if (!aiTurn) {
                    cell.addEventListener('click', handleMove);
                }
            }
            board.appendChild(cell);
        }
        const breakLine = document.createElement('br');
        board.appendChild(breakLine);
    }
    // Disable all buttons if the game is over
    if (gameOver) {
        const squares = document.querySelectorAll('.square');
        squares.forEach(square => square.removeEventListener('click', handleMove));
}
}

async function handleMove(e) {
    if (gameOver) return;

    const cell = e.target;
    if (!cell.dataset.x || !cell.dataset.y) return;
    const x = parseInt(cell.dataset.x);
    const y = parseInt(cell.dataset.y);
    const move = { x, y };

    // Disable all other cells when a move is made
    const squares = document.querySelectorAll('.square');
    squares.forEach(square => {
        if (square !== cell) {
            square.removeEventListener('click', handleMove);
        }
    });

    const response = await fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(move),
    });
    if (response.ok) {
        const data = await response.json();
        gameBoard = data.board;
        displayBoard(gameBoard);
        if (data.winner) {
            showReset(data.winner);
        } else {
            aiTurn = true;
            description.textContent = "AI thinking...";
            aiMove(data.board);
            // Enable all cells after a small delay
            setTimeout(() => {
                squares.forEach(square => {
                    if (square !== cell) {
                        square.addEventListener('click', handleMove);
                    }
                });
            }, 500);
        }
    } else {
        alert('Error: Invalid move');
    }
}

async function aiMove(boardState) {
    const squares = document.querySelectorAll('.square');
    squares.forEach(square => square.removeEventListener('click', handleMove));

    aiTurn = false;

    const response = await fetch('/aiplay', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ boardState }),
    });
    if (response.ok) {
        const data = await response.json();
        gameBoard = data.board;
        displayBoard(gameBoard);
        if (data.winner) {
            gameOver = true;
            showReset(data.winner)
        } else {
            description.textContent = "Make your move...";
        }
    } else {
        alert('Error: Invalid move');
    }

    squares.forEach(square => square.addEventListener('click', handleMove));
}

function showReset(winnerInfo) {
    description.style.fontSize = '1.4rem';
    if (winnerInfo === 'draw') {
        description.textContent = "Draw!";
    } else {
        description.textContent = "You Loose! " + winnerInfo + " Won.";
    }
    document.getElementById('play-again').style.display = 'block';
    document.getElementById('board-container').classList.add('game-over');
}

async function resetGame() {
    const response = await fetch('/reset');
    if (response.ok) {
        document.getElementById("player-selection").style.display = "block";
        document.getElementById("board-container").style.display = "none";
        document.getElementById('play-again').style.display = "none";
        document.getElementById('board-container').classList.remove('game-over');
        description.textContent = "See if you could beat AI?";
        gameOver = false;
    } else {
        alert('Error: Failed to reset game');
    }
}