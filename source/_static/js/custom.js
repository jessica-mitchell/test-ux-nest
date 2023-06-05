// When the user clicks on <div>, open the popup
//function myFunction() {
//  var popup = document.getElementById("myPopup");
//  popup.classList.toggle("show");
//}
// https://stackoverflow.com/questions/7312553/change-image-source-with-javascript
// chatgpt
//
//function showPopup(popupId) {
//  var popup = document.getElementById(popupId);
//  popup.style.visibility = "visible";
//}
//
//// Close the popups when clicking outside
//window.onclick = function(event) {
//  if (!event.target.matches('.popuptext') && !event.target.matches('area')) {
//    var popups = document.getElementsByClassName("popuptext");
//    for (var i = 0; i < popups.length; i++) {
//      var popup = popups[i];
//      popup.style.visibility = "hidden";
//    }
//  }
//};



var currentPopup = null;

function showPopup(popupId) {
  hideCurrentPopup();

  var popup = document.getElementById(popupId);
  popup.style.visibility = "visible";
  currentPopup = popup;
}

function hideCurrentPopup() {
  if (currentPopup) {
    currentPopup.style.visibility = "hidden";
    currentPopup = null;
  }
}

// Close the popups when clicking outside
window.onclick = function(event) {
  if (!event.target.matches('.popuptext') && !event.target.matches('area')) {
    hideCurrentPopup();
  }
};

