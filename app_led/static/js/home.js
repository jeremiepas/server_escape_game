namespace = '/'
global_socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
enigme_socket = io('/enigme');
porte_socket  = io('/porte');

function enigme(id, action, auto = "true"){
  porte_socket.emit(id, {action: action, auto: auto})
}

function porte(id, action, auto = "true") {
  porte_socket.emit(id, {action: action, auto: auto})
}

function ledemit(id, value) {
  led_socket.emit("led", {id: id, valiue: value})
}
function boucle(){
  enigme_socket.emit("info_enigme", 'test')
  porte_socket.emit("info_porte", 'test')
  setTimeout("boucle()",1000);
}

window.onload = function(){
  boucle();
  enigme_socket.on('info_enigme', function(str){
    data = JSON.parse(str);
    classenigme = []
    classenigme[0] = document.getElementById('enigme_0').classList
    classenigme[1] = document.getElementById('enigme_1').classList
    classenigme[2] = document.getElementById('enigme_2').classList
    classenigme[3] = document.getElementById('enigme_3').classList
    for (var i = 0; i < classenigme.length; i++) {
      if(data.enigme[i] == 1){
        classenigme[i].add("green");
        classenigme[i].remove("grey");
        classenigme[i].remove("red");
      } else if (data.enigme[i] == 0) {
        classenigme[i].add("red");
        classenigme[i].remove("grey");
        classenigme[i].remove("green");
      } else {
        classenigme[i].remove("red");
        classenigme[i].remove("grey");
        classenigme[i].add("green");
      }
    }
  });
  porte_socket.on('info_porte', function(str){
    data = JSON.parse(str);
    classenigme = []
    classenigme[0] = document.getElementById('porte_0').classList
    classenigme[1] = document.getElementById('porte_1').classList
    classenigme[2] = document.getElementById('porte_2').classList
    classenigme[3] = document.getElementById('porte_3').classList
    for (var i = 0; i < classenigme.length; i++) {
      console.log(data.porte[i])
      if(data.porte[i] == 1){
        classenigme[i].add("green");
        classenigme[i].remove("grey");
        classenigme[i].remove("red");
      } else if (data.porte[i] == 0) {
        classenigme[i].add("red");
        classenigme[i].remove("grey");
        classenigme[i].remove("green");
      } else {
        classenigme[i].remove("red");
        classenigme[i].remove("grey");
        classenigme[i].add("green");
      }
    }
  });
}
