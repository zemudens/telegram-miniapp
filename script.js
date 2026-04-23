const tg = window.Telegram.WebApp;
tg.expand();

function sendData() {
  const text = document.getElementById("text").value;
  tg.sendData(text);
}