document.querySelector('form').addEventListener('submit', function(event) {
  let name = document.getElementById('name').value;
  let email = document.getElementById('email').value;

  // Basic validation for empty fields
  if (name == "" || email == "") {
    alert("Please fill out all required fields.");
    event.preventDefault();
  } else {
    alert("Thank you for your submission!");
  }
});
