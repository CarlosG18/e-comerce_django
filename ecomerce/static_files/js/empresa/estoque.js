const btns_plus = document.getElementsByClassName('plus')
const btns_remove = document.getElementsByClassName('remove')
const visor_qtd_produto = document.getElementsByClassName('qtd_produto')

const array_btns_plus = Array.from(btns_plus)
const array_btns_remove = Array.from(btns_remove)

array_btns_plus.forEach((btn, indicie) => {
    btn.addEventListener('click', () => {
        var visor = visor_qtd_produto[indicie]
        var value = parseInt(visor.value)
        value++
        visor.value = value
    })
})

array_btns_remove.forEach((btn, indicie) => {
    btn.addEventListener('click', () => {
        var visor = visor_qtd_produto[indicie]
        var value = parseInt(visor.value)
        if(value - 1 >= 0){
            value--
        }
        visor.value = value
    })
})