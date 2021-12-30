var input = document.querySelector('#whois')
var btn = document.querySelector('#search');
var idd = document.getElementById('id')
var langua = document.getElementById("language")
var names = document.getElementById("name")
var produ = document.getElementById('product')
btn.addEventListener('click',function(){
    fetch('/api/docs/hackers?name='+input.value)
    .then(res => res.json())
   
    .then(data =>{
        var idof = data[0]['id']
        var lang = data[0]['language']
        var nameof = data[0]['name']
        var prod = data[0]['product']
        names.innerHTML = `Name of hacker <span>${nameof}</span>`
        langua.innerHTML = `Programming languages <span>${lang}</span>`
        idd.innerHTML = `ID in server <span>${idof}</span>`
        produ.innerHTML = `Product developed <span>${prod}</span>`

    })
    .catch(err => alert('Hacker not found'))

})


      