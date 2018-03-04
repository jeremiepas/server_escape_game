namespace = '/'
global_socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
enigme_socket = io('/enigme');

function enigme(id, action, auto = "true"){
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
    classenigme = []
    classenigme[0] = document.getElementById('enigme_0').classList
    classenigme[1] = document.getElementById('enigme_1').classList
    classenigme[2] = document.getElementById('enigme_2').classList
    classenigme[3] = document.getElementById('enigme_3').classList
    for (var i = 0; i < classenigme.length; i++) {
      console.log(data.enigme[i])
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

    // $('form#echo').submit(function(event){
    //     test_socket.emit('echo', {data: $('#message').val()});
    //     return false;
    // });
    // document.getElementsByName("enigme-start").addEventListener("click", enigmestart);
    // document.getElementsByName("enigme-stop").addEventListener("click", enigmestop);
    // document.getElementsByName("enigme-mode").addEventListener("click", enigmemode);
    // document.getElementsByName("enigme-reload").addEventListener("click", enigmerelod);
}
