async function predictMarks() {
    const study = document.getElementById("study").value;
    const sleep = document.getElementById("sleep").value;
    const previous = document.getElementById("previous").value;

    const result = document.getElementById("result");

    try {
        const response = await fetch("https://your-backend-url.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                study_hours: study,
                sleep_hours: sleep,
                previous_score: previous
            })
        });

        const data = await response.json();

        if (response.ok) {
            result.innerText = "Predicted Marks: " + data.predicted_marks;
        } else {
            result.innerText = "Error: " + data.error;
        }

    } catch (error) {
        result.innerText = "Server not reachable!";
    }
}