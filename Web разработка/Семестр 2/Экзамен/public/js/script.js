async function getRate() {
  let url = window.location.href + "get";

  let response = await fetch(url);
  let data = await response.json();
  let course = data["value"];
  let output = `<tr><th>Валюта</th><th>Курс сегодня</th><th>Курс вчера</th></tr>`;
  for (let i = 0; i < Object.keys(course).length; i++) {
    let name = Object.keys(course)[i];
    output += `<tr><td>${
      course[name]["Nominal"] + " " + course[name]["Name"]
    }</td><td>${course[name]["Value"]}</td><td>${
      course[name]["Previous"]
    }</td></tr>`;
  }
  document.getElementById("main-table").innerHTML = output;
}

window.onload = async () => {
  await getRate();
};
