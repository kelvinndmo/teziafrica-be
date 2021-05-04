document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#input").addEventListener("keydown", function(e) {
        if (e.code === "Enter") {
            let input = inputField.value;
            console.log(`I typed '${input}'`)
            
        }
    });
    });
    function compare(triggerArray, replyArray, text) {
        let item;
        for (let x = 0; x < triggerArray.length; x++) {
          for (let y = 0; y < replyArray.length; y++) {
            if (triggerArray[x][y] == text) {
              items = replyArray[x];
              item = items[Math.floor(Math.random() * items.length)];
            }
          }
        }
        return item;
      }
      function output(input) {
        let product;
        let text = input.toLowerCase().replace(/[^\w\s\d]/gi, "");
        text = text
          .replace(/ a /g, " ")
          .replace(/i feel /g, "")
          .replace(/whats/g, "what is")
          .replace(/please /g, "")
          .replace(/ please/g, "");
      
      //compare arrays
      //then search keyword
      //then random alternative
      
        if (compare(trigger, reply, text)) {
          product = compare(trigger, reply, text);
        } else if (text.match(/robot/gi)) {
          product = robot[Math.floor(Math.random() * robot.length)];
        } else {
          product = alternative[Math.floor(Math.random() * alternative.length)];
        }
      
        //update DOM
        addChat(input, product);
      }
      const robot = ["How do you do, fellow human", "I am not a bot"];

      function addChat(input, product) {
        const mainDiv = document.getElementById("main");
        let userDiv = document.createElement("div");
        userDiv.id = "user";
        userDiv.innerHTML = `You: <span id="user-response">${input}</span>`;
        mainDiv.appendChild(userDiv);
      
        let botDiv = document.createElement("div");
        botDiv.id = "bot";
        botDiv.innerHTML = `Chatbot: <span id="bot-response">${product}</span>`;
        mainDiv.appendChild(botDiv);
        speak(product);
      }
      