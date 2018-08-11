var count = 0;
 
function countClicks() {
  count = count + 1;
  var span = 
      document.getElementById("ccount");
  span.innerHTML = count;
}

var xmlHttp;
 
function gotResponse() {
  if(xmlHttp.readyState==4 && xmlHttp.status==200) {
    var span = document.getElementById("ccount");
    span.innerHTML = xmlHttp.responseText;
  }
}
 
function getFromServer() {
  xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = gotResponse;
  xmlHttp.open("GET", "http://localhost/getValue");
  xmlHttp.send();
}
