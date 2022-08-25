function iniciar(){
    var nome_visitante = document.querySelectorAll('.show-mensagem h2')
    var mensagem_visitante = document.querySelectorAll('.show-mensagem span')
    var mostrar_msg = document.querySelector('.show-mensagem')

    var nomes_mensagens = []
    for (let n=0; n < nome_visitante.length; n++){
        nomes_mensagens.push([nome_visitante[n].innerText, mensagem_visitante[n].innerText])
    }
    mostrar_msg.innerHTML = ''
    
    console.log(nomes_mensagens[4])
}
window.addEventListener('load', iniciar)