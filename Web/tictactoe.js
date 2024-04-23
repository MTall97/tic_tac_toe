let cases = [...document.getElementsByClassName("case")];
let tour = document.getElementById('player');
let score1 = document.getElementById('X');
let score2 = document.getElementById('O');
let nul = document.getElementById('nul');




let state = {
    joueurEnCours : 1,
    tour : 1,
    scoreJ1 : 0,
    scoreJ2 : 0,
    matchNul : 0,
    c1 : 0,
    c2 : 0,
    c3 : 0,
    c4 : 0,
    c5 : 0,
    c6 : 0,
    c7 : 0,
    c8 : 0,
    c9 : 0
};

const resetState = () => {
    state = {
    joueurEnCours : 1,
    tour : 1,
    scoreJ1 : parseInt(score1.textContent),
    scoreJ2 : parseInt(score2.textContent),
    matchNul : parseInt(nul.textContent),
   
    c1 : 0,
    c2 : 0,
    c3 : 0,
    c4 : 0,
    c5 : 0,
    c6 : 0,
    c7 : 0,
    c8 : 0,
    c9 : 0
    };
}

const win = () => {
    if (
        (state.c1 == state.c2 && state.c2 == state.c3 && state.c1 >0 ) ||
        (state.c1 == state.c4 && state.c4 == state.c7 && state.c1 >0 ) ||
        (state.c1 == state.c5 && state.c5 == state.c9 && state.c1 >0 ) ||
        (state.c2 == state.c5 && state.c5 == state.c8 && state.c2 >0 ) ||
        (state.c3 == state.c6 && state.c6 == state.c9 && state.c3 >0 ) ||
        (state.c3 == state.c5 && state.c5 == state.c7 && state.c3 >0 ) ||
        (state.c4 == state.c5 && state.c5 == state.c6 && state.c6 >0 ) ||
        (state.c7 == state.c8 && state.c8 == state.c9 && state.c9 >0 )
    ) {
        return true;

    } else if (
        state.c1 != 0 &&
        state.c2 != 0 &&
        state.c3 != 0 &&
        state.c4 != 0 &&
        state.c5 != 0 &&
        state.c6 != 0 &&
        state.c7 != 0 &&
        state.c8 != 0 &&
        state.c9 != 0 
    ) {
        return null;

    } else {
        return false;

    }
};



const play = (e) => {
    let idCase = e.target.id;
    if (state[idCase] != 0);
    state[idCase] = state.joueurEnCours;
    state.tour = state.joueurEnCours;
    //console.log(state.tour);

    let isWin = win();

    if( isWin ) {
        if (state.joueurEnCours == 1 ) {
            state.scoreJ1++;
            score1.textContent = state.scoreJ1;
            state.joueurEnCours = "X";
        } else if (state.joueurEnCours == 2 ) {
            state.scoreJ2++;
            score2.textContent = state.scoreJ2;
            state.joueurEnCours = "O";
        }

        alert("Le gagnant de la partie est " + state.joueurEnCours);
        //cases.forEach((c) => (c.textContent = ''));
       

    } else if (isWin == null) {
        state.matchNul++;
        nul.textContent = state.matchNul;
        alert("Match nul !!");
        //cases.forEach((c) => (c.textContent = ''));

    } else if (isWin == false) {
        if (state.joueurEnCours == 1) {
            e.target.textContent = 'X';
            state.joueurEnCours = 2;
            tour.textContent = "O";
            

        } else {
            e.target.textContent = 'O';
            state.joueurEnCours = 1;
            tour.textContent = "X";
        }
    }
};


const reset = () => {
    // Réinitialiser l'état du jeu ici
    resetState();
    cases.forEach((c) => (c.textContent = ''));
};


// Ajoutez le gestionnaire d'événements pour le bouton "Rejouer"
const rejouerButton = document.getElementById('rejouer');
rejouerButton.addEventListener('click', reset);



cases.forEach((el) => {
    el.addEventListener("click", play)
});