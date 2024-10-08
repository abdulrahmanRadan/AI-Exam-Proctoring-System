document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Dummy login function
    if (username === "admin" && password === "password") {
      document.getElementById("login").style.display = "none";
      document.getElementById("dashboard").style.display = "block";
    } else {
      alert("Invalid credentials");
    }
  });

// Function to fetch and display alerts
function fetchAlerts() {
  // Dummy implementation for fetching alerts
  const alerts = [
    { id: 1, message: "Suspicious behavior detected for student 123" },
    { id: 2, message: "Student 456 left the exam room" },
  ];

  const alertList = document.getElementById("alertList");
  alertList.innerHTML = "";
  alerts.forEach((alert) => {
    const li = document.createElement("li");
    li.textContent = alert.message;
    alertList.appendChild(li);
  });
}

// Fetch alerts every 5 seconds
setInterval(fetchAlerts, 5000);
