const express = require("express");
const axios = require("axios");
const app = express();
const port = 5050;
const server = require("http").createServer(app);
const path = require("path");
const cors = require("cors");

app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(express.static(path.resolve(__dirname) + "/public"));

app.use(cors());

app.get("/", (req, res) => {
  res.sendFile(path.resolve(__dirname) + "/index.html");
});

app.get("/get", (req, res) => {
  let response = null;
  new Promise(async (resolve, reject) => {
    try {
      response = await axios("https://www.cbr-xml-daily.ru/daily_json.js");
    } catch (error) {
      response = null;
    }
    if (response) {
      const json = response.data;
      const json_response = {
        date: json["Date"],
        value: json["Valute"],
      };
      res.send(json_response);
    }
  });
});

server.listen(port, function () {
  console.log(`Listening on ${port}`);
});
