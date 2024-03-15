const texts = document.querySelector(".texts");

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = false;

let p = document.createElement("p");
let o = document.createElement("p")


recognition.addEventListener("result", (e) => {

  texts.appendChild(p);
  const text = Array.from(e.results)
  .map((result) => result[0])
  .map((result) => result.transcript)
  .join("");

  p.innerText = ">>> " + text;
  eel.tts("You said" + text);

  async function response() {

    texts.appendChild(o);
    let output = await eel.basicInfo(text.toLowerCase())();

    if (output == "exit") {

      window.close();
    }

    o.innerText = ">>> " + output;
    eel.tts(output);
  }

  response();

});




recognition.addEventListener("end", () => {
  recognition.start();
});

recognition.start();



