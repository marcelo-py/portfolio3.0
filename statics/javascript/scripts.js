var currentMensageIndex = 0,
    time = 5000,
    objt_nome = document.querySelectorAll('.show-mensagem h2'),
    objt_msg = mensagem_visitante = document.querySelectorAll('.show-mensagem span')
    max_obj = objt_nome.length,
    hora = new Date().getHours()
    ano = new Date().getFullYear(),

    nome_footer = document.querySelector('footer span')


nome_footer.innerHTML += ` ${ano}`

function nextMensagem(){

    objt_nome[currentMensageIndex].classList.remove('selected')
    objt_msg[currentMensageIndex].classList.remove('selected')
    currentMensageIndex ++

    if (currentMensageIndex >= max_obj){
        currentMensageIndex = 0
    }

    objt_nome[currentMensageIndex].classList.add('selected')
    objt_msg[currentMensageIndex].classList.add('selected')
}


function iniciar(){
    setInterval(() => {
        nextMensagem()
    }, time)
    
    if (hora >= 5 && hora < 12){
        objt_nome[0].innerHTML = 'Bom Dia!'
    } else if (hora >= 12 && hora < 18){
        objt_nome[0].innerHTML = 'Boa Tarde!'
    } else if (hora >= 18 && hora <= 23){
        objt_nome[0].innerHTML = 'Boa Noite!'
    } else{
        objt_nome[0].innerHTML = 'Boa Madruga!'
    }
}


window.addEventListener('load', iniciar)