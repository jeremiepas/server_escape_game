namespace = '/'
global_socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
enigme_socket = io('/enigme');

function enigme(id, action, auto = "true"){
  console.log(id);
  enigme_socket.emit(id, {action: action, auto: auto})
}
function porte(id, action) {
  enigme_socket.emit("porte", {id: id, action: action})
}

function ledemit(id, value) {
  led_socket.emit("led", {id: id, valiue: value})
}
function boucle(){
  enigme_socket.emit("info", 'test')
  setTimeout("boucle()",1000);
}

window.onload = function(){
  boucle();
  enigme_socket.on('info', function(str){
    data = JSON.parse(str);
    classenigme_0 = document.getElementById('enigme_0').classList
    classenigme_1 = document.getElementById('enigme_1').classList

    if(data.enigme_0 == "1"){
      classenigme_0.add("green");
      classenigme_0.remove("grey");
      classenigme_0.remove("red");
    } else {
      classenigme_0.add("red");
      classenigme_0.remove("grey");
      classenigme_0.remove("green");
    }
    if(data.enigme_1 == "1"){
      classenigme_1.add("green");
      classenigme_1.remove("grey");
      classenigme_1.remove("red");
    } else {
      classenigme_1.add("red");
      classenigme_1.remove("grey");
      classenigme_1.remove("green");
    }
  });

    // $('form#echo').submit(function(event){
    //     test_socket.emit('echo', {data: $('#message').val()});
    //     return false;
    // });
    // document.getElementsByName("enigme-start").addEventListener("click", enigmestart);
    // document.getElementsByName("enigme-stop").addEventListener("click", enigmestop);
    // document.getElementsByName("enigme-mode").addEventListener("click", enigmemode);
    // document.getElementsByName("enigme-reload").addEventListener("click", enigmerelod);
}
