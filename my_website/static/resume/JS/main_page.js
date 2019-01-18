// alert('Welcome to my virtual resume, enjoy!');


var header = document.getElementsByName('strong');



header.addEventListener('mouseover', function(){

    function getRandomColor(){
      var letters = "0123456789ABCDEF";
      var color = '#';
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random()*16)];
      }
      return color;

    }

  // Simple function for clarity
    function changeHeaderColor(){
      colorInput = getRandomColor();
      header.style.color = colorInput;
      // setInterval("changeHeaderColor()",500);
    }
    header.style.color = changeHeaderColor();
  });

header.addEventListener("mouseout", function(){
  header.textContent = "Jacob Cansler's";
  header.style.color = 'black';
})


//////////////////////////////////////////////////////////////////////////////

// $(skill).css("text-align", "center");
// // $(skill).css("margin", "auto")
//
// $(threestar).css("color", "gold");
// // $(twostar).css("color", "gold")
// $(fourstar).css("color", "gold");
// $(fivestar).css("color", "gold");
// $(strong).css("text-align", "center");
