// FUNÇÃO NORMAL
//function sun(number1,number2){
//    return number1 + number2
//}
// ARROW FUNCTION
//const sun = (number1,number2)=>{
//    return number1 + number2
//}
// FUNÇÃO ANONIMA
//const sun = function(number1,number2){
//    return number1 + number2
//}

// ARROW FUNCTION SEM RETORNO
//const sun = (number1,number2) => number1 + number2

//ARROW FUNCTION SEM PARAMETROS
//const municipio = ()=> 'jucuri'
//const municipi2 = ()=>{
//    return 'pedra-branca'
//}
//console.log(municipi2())
//console.log(municipio())
//console.log(sun(3,23))

// TERCEIRA VARIAÇÃO DE ARROW FUNCION
//const dobro = (number)=>{
//    return number * 2
//}
//console.log(dobro(442))
// SEXTA VARIAÇÃO RETORNANDO UM JSON SEM RETORN DE ARROW FUNCION
// coloca-se os Parenteses ()
//const Person = ()=>{
//    return {name:'ze'}
//}
//console.log(getPerson())
//console.log(Person())

// O THIS DENTRO DE ARROW FUNCTIONS
// IIFE no arrow functio
(() =>{
    function Person (){
        
        this.ano = 0
        setInterval(()=>{
            this.ano = this.ano + 1
            //console.log('Qual e o this', this)
            //console.log('Qual e o ano ', this.ano)
        },1000)
    }
    const p1 = new Person()
})()

















