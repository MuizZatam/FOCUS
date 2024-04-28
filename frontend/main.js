const texts = document.querySelector(".texts");
const container = document.querySelector(".container");

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.interimResults = false;

const wakeWord = "hey focus"


eel.greet();  
// eel.mouse();

recognition.addEventListener("result", async (e) => {


  let text = Array.from(e.results)
  .map((result) => result[0])
  .map((result) => result.transcript)
  .join("");

  if (text.startsWith(wakeWord)) {

    let p = document.createElement("p");
    texts.appendChild(p);
  

    p.innerText = ">>> " + text;
    
    let command = text.replace(wakeWord + " ", "");
    command = command.toLowerCase()

    if (command == "exit") {
      window.close();
    }

    else if (command == "start typing") {
      eel.type(command); 
    }

    else if (text.includes("write a letter")) {
      let email = await eel.draftEmail(text)();
    
      if (text.includes("header")) {
        let headerImg = document.createElement("img");
        headerImg.setAttribute("src", "./email/sampleheader.png");
        headerImg.setAttribute("style", "margin-bottom: -40px")
        texts.appendChild(headerImg);
      }
    
      let emailParagraph = document.createElement("p");
      emailParagraph.innerText = email;
      emailParagraph.setAttribute("style", "margin-top: 0px")
      emailParagraph.setAttribute("style", "width:600px")
      texts.appendChild(emailParagraph);
    
      if (text.includes("footer")) {
        let footerImg = document.createElement("img");
        footerImg.setAttribute("src", "./email/samplefooter.png");
        footerImg.setAttribute("style", "width: 600px");
        footerImg.setAttribute("style", "margin-top: -19px");
        texts.appendChild(footerImg);
      }
    }

    else {
      let output = await eel.basicInfo(command)();
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
