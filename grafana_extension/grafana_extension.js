
var main_frame = document.createElement('iframe');
main_frame.style.backgroundColor = 'rgb(' + 10 + ',' + 10 + ',' + 10 + ')';
main_frame.style.height = "100%";
main_frame.style.width = "25%";
main_frame.style.position = "fixed";
main_frame.style.top = "0px";
main_frame.style.right = "0px";
main_frame.style.zIndex = "9000000000000000000";
main_frame.frameBorder = "none"; 
main_frame.onmouseover=openFrame
main_frame.onmouseleave=closeFrame
main_frame.style.opacity= "0";
document.body.appendChild(main_frame);

var btn_start = document.createElement('button');
btn_start.style.backgroundColor = 'rgb(' + 58 + ',' + 58 + ',' + 58 + ')';
btn_start.style.height = "15%";
btn_start.style.width = "15%";
btn_start.style.position = "fixed";
btn_start.style.top = "10%";
btn_start.style.right = "4%"; 
btn_start.style.zIndex = "9000000000000000000";
btn_start.frameBorder = "none";
btn_start.onmouseover=openFrame
btn_start.textContent = 'START';
btn_start.onclick=sendStart;
btn_start.style.opacity= "0";
document.body.appendChild(btn_start);

var btn_stop = document.createElement('button');
btn_stop.style.backgroundColor = 'rgb(' + 58 + ',' + 58 + ',' + 58 + ')';
btn_stop.style.height = "15%";
btn_stop.style.width = "15%";
btn_stop.style.position = "fixed";
btn_stop.style.top = "45%";
btn_stop.style.right = "4%";
btn_stop.style.zIndex = "9000000000000000000";
btn_stop.frameBorder = "none";
btn_stop.onmouseover=openFrame 
btn_stop.textContent = 'STOP';
btn_stop.onclick=sendStop;
btn_stop.style.opacity= "0";
document.body.appendChild(btn_stop);

var btn_history = document.createElement('button');
btn_history.style.backgroundColor = 'rgb(' + 58 + ',' + 58 + ',' + 58 + ')';
btn_history.style.height = "15%";
btn_history.style.width = "15%";
btn_history.style.position = "fixed";
btn_history.style.top = "80%";
btn_history.style.right = "4%";
btn_history.style.zIndex = "9000000000000000000";
btn_history.frameBorder = "none";
btn_history.onmouseover=openFrame 
btn_history.textContent = 'HISTORY';
btn_history.onclick=sendHistory;
btn_history.style.opacity= "0";
document.body.appendChild(btn_history);


function sendStart() {
  //funkcja wysyłająca informację o starcie do servera i ładująca nowo utworzoną tabelę do Grafany

  var exampleSocket = new WebSocket("ws://10.0.67.130:8091");
  
  //pobiera date i czas ktore sa nazwa tabeli
  var MyDate = new Date();

  var MyDateString = '';
  MyDate.setDate(MyDate.getDate());
  var tempoMonth = (MyDate.getMonth()+1);
  var tempoDate = (MyDate.getDate());
  if (tempoMonth < 10) tempoMonth = '0' + tempoMonth;
  if (tempoDate < 10) tempoDate = '0' + tempoDate;
  
  MyDateString = MyDate.getFullYear() + '-' + tempoMonth + '-' + tempoDate;
  
  var hour = MyDate.getHours();
  var min =MyDate.getMinutes();
  var sec = MyDate.getSeconds();
  if (hour < 10) hour = '0' + hour;
  if (min < 10) min = '0' + min;
  if (sec < 10) sec = '0' + sec;

  var time =hour+":"+min+":"+sec;
  
  //var nazwa="http://localhost:3000/d/oWbq1XvMz/akcelerometr?orgId=1&refresh=1s&var-nazwa="+MyDateString+"X"+time;
  
  var nazwa="http://localhost:3000/d/oWbq1XvMz/akcelerometr?orgId=1&refresh=1s&var-nazwa="+MyDateString+"X"+time;

  let stateObj={id:"100"};
  window.history.replaceState(stateObj,"Page 3",nazwa)
  
  //window.location.replace(nazwa);
  exampleSocket.close();
}

function sendStop() {
    var exampleSocket = new WebSocket("ws://10.0.67.130:8092");
    
    exampleSocket.close();
   
  }

function sendHistory() {
    var exampleSocket = new WebSocket("ws://10.0.67.130:8093");
    
    exampleSocket.close();
  }

function openFrame() {
  //funkcja zmienia ramkę i przyciski na widoczne
  main_frame.style.opacity= "1";
  btn_start.style.opacity= "1";
  btn_stop.style.opacity= "1";
  btn_history.style.opacity= "1";
}

function closeFrame() {
  //funkcja zmienia ramkę i przyciski na nie widoczne
  main_frame.style.opacity= "0";  
  btn_start.style.opacity= "0";
  btn_stop.style.opacity= "0";
  btn_history.style.opacity= "0";
}






