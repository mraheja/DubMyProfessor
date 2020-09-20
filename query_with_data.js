const fetch = require('node-fetch');
fs = require('fs');

fetch("https://mumble.stream/speak_spectrogram", {
  "headers": {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
  },
  "referrer": "https://vo.codes/",
  "referrerPolicy": "no-referrer-when-downgrade",
  "body": "{\"text\":\" Well, it means that sometimes when you're executing the body of a function and its the recursive function that might require you to apply that same function again.\",\"speaker\":\"david-attenborough\"}",
  "method": "POST",
  "mode": "cors"
}).then(response => response.json())
  .then(data => console.log(data));