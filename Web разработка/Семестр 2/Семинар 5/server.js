const express = require('express');
const MongoClient = require("mongodb").MongoClient;
const app = express();
const port = 3000;
var server = require('http').createServer(app);

app.use(
  express.urlencoded({
    extended: true
  })
);

app.use(express.static('public'));

app.get('/scoring', function (req, res) {
  res.sendFile('C:/Users/dmitrb/Desktop/1002/Lab 2/public/index.html');
});

app.post('/scoring', (req, res) => {
  // console.log(req.body);

  // const url = "mongodb://localhost:3001";
  // const client = new MongoClient(url);

  // client.connect(function (err, client) {
  //   const db = client.db('clients');
  //   const collection = db.collection('info');
  //   let clientInformation = req.body;
  //   collection.insertOne(clientInformation, function (err, result) {
  //     if (err) {
  //       return console.log(err);
  //     }
  //     console.log(result);
  //     console.log(clientInformation);
  //     client.close();
  //   });
  // });

  res.send('OK');
});

server.listen(port, function () {
  console.log(`listening on ${port}`);
});