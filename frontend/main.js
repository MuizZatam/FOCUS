const wakeWord = "hey focus"; // Define your wake word here
const texts = document.querySelector(".texts");

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.interimResults = false;

const container = document.querySelector(".container");

let recognitionActive = false; // Variable to track if recognition is active
let typingActive = false; // Variable to track if typing mode is active

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
    eel.greet();
    return;
  }

  if (recognitionActive) {
    // Perform actions only when recognition is active
    if (!typingActive) {
      // If not in typing mode, process commands using basicInfo
      if (text.toLowerCase() == "start typing") {
        enterTypingMode(); // Enter typing mode if user says "start typing"
        return;
      }

      let output = await eel.basicInfo(text.toLowerCase())();
      if (output == "exit") {
        window.close();
      }
      if (output.toLowerCase().includes("open app") || output.toLowerCase().includes("close app")) {
        eel.osActives(output);
        return;
      }
      // Check if the response contains ">>>" indicating it's the recognition's own response
      if (!output.includes(">>>")) {
        // If it doesn't contain ">>>" it's a user's response, display it
        let o = document.createElement("p");
        o.innerText = ">>> " + output;
        texts.appendChild(o);
      }
      eel.tts(output)();
    } else {
      // If in typing mode, pass text to type function
      eel.type(text.toLowerCase())();
      if (text.toLowerCase() == "stop typing") {
        exitTypingMode(); // Exit typing mode if user says "stop typing"
      }
    }
  }
});

recognition.addEventListener("end", () => {
  // When recognition ends, set recognitionActive to false and restart recognition
  recognitionActive = false;
  startRecognition();
});

// Start recognition initially
startRecognition();

function startRecognition() {
  if (!recognitionActive) {
    recognition.start();
    recognitionActive = true;
  }
}

// Function to enter typing mode
function enterTypingMode() {
  typingActive = true;
}

// Function to exit typing mode
function exitTypingMode() {
  typingActive = false;
}
