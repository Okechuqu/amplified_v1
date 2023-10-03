// Question and Answers
function toggleAnswer(faqId) {
    var answerElement = document.getElementById('answer-' + faqId);
    answerElement.classList.toggle("active");
}


// Bootstrap Message
$(document).ready(function () {
    // Auto-close the success alert after 3 seconds (3000 milliseconds)
    $("#success-alert").delay(3000).fadeOut("slow");
  });