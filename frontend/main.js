const wakeWord = "hey assistant"; // Define your wake word here
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

  // Check if the wake word is present in the transcribed text
  if (text.toLowerCase().includes(wakeWord.toLowerCase())) {
    // Wake word detected, greet the user
    await eel.tts("Hello, how can I assist you?")();

    let output = await eel.basicInfo(text.toLowerCase().replace(wakeWord.toLowerCase(), "").trim())();

    if (output == "exit") {
      window.close();
    }

    if (output.toLowerCase().includes("open app") || output.toLowerCase().includes("close app")) {
      eel.osActives(output);
      return;
    }

    if (text.toLowerCase() == "start typing") {

      eel.type(text)
    }

    o.innerText = ">>> " + output;
    eel.tts(output)();
    eel.timeout(eel.reqTimeOut(output))
  } else {
    // Wake word not detected, restart the speech recognition
    recognition.start();
  }
});

recognition.addEventListener("end", () => {
  recognition.start();
});

recognition.start();