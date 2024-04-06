const texts = document.querySelector(".texts");
const container = document.querySelector(".container");

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.interimResults = false;

const wakeWord = "hey focus"


eel.greet();  

recognition.addEventListener("result", async (e) => {


  let text = Array.from(e.results)
  .map((result) => result[0])
  .map((result) => result.transcript)
  .join("");

  if (text.startsWith(wakeWord)) {

    let p = document.createElement("p");
    texts.appendChild(p);
  

    p.innerText = ">>> " + text;
    text.replace(wakeWord + " ", "")

    if (text == "exit") {
      window.close();
    }

    else if (text == "start typing") {
      eel.type(text); 
    }

    // else if (text == "") {
    //   eel.openApp(text.replace("open app", ""));
    // }

    else {
      let output = await eel.basicInfo(text)();
      let o = document.createElement("p");
      o.innerText = ">>> " + output;
      texts.appendChild(o);
    
    }

  }

  
});

recognition.addEventListener("end", () => {
  recognition.start();
});

recognition.start();
