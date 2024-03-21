const texts = document.querySelector(".texts");

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = false;

const container = document.querySelector(".container");

let recognizing = false;


recognition.addEventListener("result", (e) => {

  if (!recognizing) {

    let p = document.createElement("p");

    texts.appendChild(p);
    const text = Array.from(e.results)
    .map((result) => result[0])
    .map((result) => result.transcript)
    .join("");
  
    p.innerText = ">>> " + text;
  
    eel.tts("You said" + text)();
  
    async function response() {
  
      let o = document.createElement("p");
  
      texts.appendChild(o);
      let output = await eel.basicInfo(text.toLowerCase())();
  
      if (output == "exit") {
  
        window.close();
      }
  
      o.innerText = ">>> " + output;
      eel.tts(output);
      recognizing = false;
    }
  
    response();  
  }
});

eel.timeout();
recognition.addEventListener("end", () => {

  recognition.start();
});

recognition.start();