const btn = document.getElementById('btn');

btn = onclick = function(){
    this.alert('The btn was clicked, and the task is to show this dialog box');

};





const select = document.getElementById('city');

select.addEventListener('change', function(){ // En setionnant un element 
    val = document.getElementById('city').value;

    test = document.getElementById('value').innerHTML = val;
});

const area = document.getElementById('area');

area.addEventListener('keypress', function(){
    val = document.getElementById('key').innerHTML = area.value;
})

const focus = document.getElementById('focus');

focus.addEventListener('focus', function(){ //en entrer de input
    focus.style.background = 'green';
})

focus.addEventListener('blur', function(){ // en sortie de input
    focus.style.background = "yellow";
})

/********************************** */

window.addEventListener('resize', function(){
    document.getElementById('.winW').innerHTML = window.innerWidth;
    document.getElementById('.winH').innerHTML = window.innerHeight;
})
