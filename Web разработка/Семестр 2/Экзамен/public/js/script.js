let rates = [];

async function getRate() {
  let url = window.location.href + "get";

  let response = await fetch(url);
  let data = await response.json();
  rates = data["rates"];
  let output = `<p>Валюта  <select id="rates_select" onchange=changeExchangeRate(this)><option disabled selected>Валюта</option>`;
  for (let i = 0; i < Object.keys(rates).length; i++) {
    let name = Object.keys(rates)[i];
    output += `<option value="${name}">${name}</option>`;
  }
  output += `</select></p>`;
  document.getElementById("main-table").innerHTML = output;
}

function changeExchangeRate(select) {
  let rate_name = select.options[select.selectedIndex].value;
  let rate_value = rates[rate_name];
  document.getElementById("exchange_rate").value = rate_value;
  console.log(rate_name, rate_value);
}

window.onload = async () => {
  await getRate();
};
