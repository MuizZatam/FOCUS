const texts = document.querySelector(".texts");

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = false;

const container = document.querySelector(".container");


eel.greet()

recognition.addEventListener("result", (e) => {


  let p = document.createElement("p");

  texts.appendChild(p);
  const text = Array.from(e.results)
  .map((result) => result[0])
  .map((result) => result.transcript)
  .join("");
  
  p.innerText = ">>> " + text;
  
  eel.tts("You said" + text)();
  eel.timeout(eel.reqTimeOut(text))

  
  async function response() {
  
    let o = document.createElement("p");
  
    texts.appendChild(o);
    let output = await eel.basicInfo(text.toLowerCase())();
  
    if (output == "exit") {
  
      window.close();
    }
  
    o.innerText = ">>> " + output;
    eel.tts(output);
    eel.timeout(eel.reqTimeOut(output))

  }
  
  response();  
  
});

recognition.addEventListener("end", () => {

  recognition.start();
});

recognition.start();