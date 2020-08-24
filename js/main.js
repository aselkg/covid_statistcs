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
    document.getElementById("word-s").innerHTML = data;
  });

  fetch("./usa.html")
  .then(response => {
    return response.text()
  })
  .then(data => {
    document.getElementById("usa-s").innerHTML = data;
  });

  fetch("./region.html")
  .then(response => {
    return response.text()
  })
  .then(data => {
    document.getElementById("region-s").innerHTML = data;
  });

  

  
  function openStat(evt, locName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(locName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  

  //Search angine
  function myFunction() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.querySelector("table");
    tr = table.getElementsByTagName("tr");
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
  }