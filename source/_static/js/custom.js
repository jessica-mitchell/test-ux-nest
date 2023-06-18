document.addEventListener("DOMContentLoaded", function() {
  const svgElements = document.querySelectorAll("#mySvg .clickable");
  const popups = document.querySelectorAll(".popuptext");

  svgElements.forEach(function(svgElement) {
    svgElement.addEventListener("click", function() {
      const svgElementId = svgElement.getAttribute("id");
      const popupId = getMatchingPopupId(svgElementId);

      if (popupId) {
        const popup = document.getElementById(popupId);
        togglePopup(popup);
      }
    });
  });

  document.addEventListener("click", function(event) {
    if (!event.target.closest("#mySvg")) {
      popups.forEach(function(popup) {
        hidePopup(popup);
      });
    }
  });

  function togglePopup(popup) {
    if (popup.classList.contains("visible")) {
      hidePopup(popup);
    } else {
      hideAllPopups();
      showPopup(popup);
    }
  }

  function hidePopup(popup) {
    popup.classList.remove("visible");
  }

  function showPopup(popup) {
    popup.classList.add("visible");
  }

  function hideAllPopups() {
    popups.forEach(function(popup) {
      hidePopup(popup);
    });
  }

  function getMatchingPopupId(svgElementId) {
    const idWord = svgElementId.replace(/[0-9]+$/, "");
    const matchingPopup = Array.from(popups).find(function(popup) {
      return popup.id === idWord;
    });

    console.log("ID Word:", idWord);
    console.log("Matching Popup:", matchingPopup);

    return matchingPopup ? matchingPopup.id : null;
  }
});

