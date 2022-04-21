const express = require("express");
const axios = require("axios");
const app = express();
const port = 3000;
const server = require("http").createServer(app);
const path = require("path");
const MongoClient = require("mongodb").MongoClient;
app.get("/", (req, res) => {
  res.sendFile(path.resolve(__dirname) + "/index.html");
});

app.get("/get/:val", (req, res) => {
  let options = {
    method: "get",
    url: "https://www.cbr-xml-daily.ru/daily_json.js",
    json: true,
  };

  console.log(req.params.val);

  let response = null;
  new Promise(async (resolve, reject) => {
    try {
      response = await axios("https://www.cbr-xml-daily.ru/daily_json.js");
    } catch (error) {
      response = null;

    }
    if (response) {
      const json = response.data;

      const url = "mongodb://localhost:5000";
      const clientMongo = new MongoClient("url");

      clientMongo.connect(function (err, client) {
        if (err) console.log(err);
        const db = client.db("currencies");
        const collection = db.collection("info");
        collection.insertOne(json);
      });

      let course = data["Valute"][curr]["Value"];
      res.send(course);
    }
  });
});

server.listen(port, function () {
  console.log(`listening on ${port}`);
});
