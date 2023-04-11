const express = require("express");
const axios = require("axios");
const app = express();
const port = 5050;
const server = require("http").createServer(app);
const sqlite3 = require("sqlite3").verbose();
const path = require("path");
const cors = require("cors");
const db = new sqlite3.Database("cbr_daily.db");

db.serialize(function () {
  db.run("CREATE TABLE IF NOT EXISTS rates (rate TEXT, dt TEXT, change FLOAT)");
});

const insert_row = db.prepare(
  "INSERT INTO rates (rate, dt, change) VALUES (?,?,?)"
);

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
  var today = new Date();
  var dd = String(today.getDate() + 1).padStart(2, "0");
  var mm = String(today.getMonth() + 1).padStart(2, "0");
  var yyyy = today.getFullYear();
  today = yyyy + "-" + mm + "-" + dd;
  let response = null;
  db.all(
    `SELECT rate, dt, change FROM rates WHERE dt = ?`,
    [today],
    (err, results) => {
      if (typeof results !== "undefined") {
        console.log("from db");
        let rates = {};
        let date = results[0]["dt"];
        for (i = 0; i < results.length; i++) {
          rates[results[i]["rate"]] = results[i]["change"];
        }
        const json_response = {
          date: date,
          rates: rates,
        };
        res.send(json_response);
      } else {
        new Promise(async (resolve, reject) => {
          try {
            response = await axios("https://www.cbr-xml-daily.ru/latest.js");
          } catch (error) {
            response = null;
          }
          if (response) {
            const json = response.data;
            let date = json["date"];
            let new_rates = {};
            for (i = 0; i < Object.keys(json["rates"]).length; i++) {
              let name = Object.keys(json["rates"])[i];
              let value =
                1 / parseFloat(json["rates"][Object.keys(json["rates"])[i]]);
              insert_row.run(name, date, value);
              new_rates[name] = value;
            }
            const json_response = {
              date: date,
              rates: new_rates,
            };
            res.send(json_response);
          }
        });
      }
    }
  );
});

server.listen(port, function () {
  console.log(`Listening on ${port}`);
});
