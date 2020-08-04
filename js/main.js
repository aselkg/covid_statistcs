fetch("./header.html")
  .then(response => {
    return response.text()
  })
  .then(data => {
    document.querySelector("header").innerHTML = data;
  });

fetch("./footer.html")
  .then(response => {
    return response.text()
  })
  .then(data => {
    document.querySelector("footer").innerHTML = data;
  });

  fetch("./world.html")
  .then(response => {
    return response.text()
  })
  .then(data => {
    document.querySelector("main").innerHTML = data;
  });
  
  fetch("./country.html")
  .then(response => {
    return response.text()
  })
  .then(data => {
    document.querySelector(".main").innerHTML = data;
  });