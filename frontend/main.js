const texts = document.querySelector(".texts");

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = false;

const container = document.querySelector(".container");


async function greet() {

  await eel.greet();
}

resp = greet();


recognition.addEventListener("result", async (e) => {


  let p = document.createElement("p");

  texts.appendChild(p);
  const text = Array.from(e.results)
    .map((result) => result[0])
    .map((result) => result.transcript)
    .join("");
  
  p.innerText = ">>> " + text;

  // Speak only after recognition is complete
  await eel.tts("You said" + text)();

  let output = await eel.basicInfo(text.toLowerCase())();

  if (output == "exit") {

    window.close();
  }
  
  if (output.toLowerCase().includes("open app") || output.toLowerCase().includes("close app")) {

    eel.osActives(output);
    return;
  }

  o.innerText = ">>> " + output;
  eel.tts(output)();
  eel.timeout(eel.reqTimeOut(output))

});

recognition.addEventListener("end", () => {

  recognition.start();
});

recognition.start();
