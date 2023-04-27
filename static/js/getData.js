async function getClubData() {
  const token = 'ufbclZ0RrXnlfvwxhuSfU9qRUG8yoYFw'; // Replace this with your actual token

  try {
    const response = await fetch("http://localhost:8000/api/api/clubs/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Token ${token}`,
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data);
      // Process the data here, e.g., create HTML elements and fill them with the received data
    } else {
      console.error("Failed to fetch club data");
    }
  } catch (error) {
    console.error("Error:", error.message);
  }
}

getClubData().then(r => console.log(r));
