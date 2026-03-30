async function predictMarks() {
    const study = document.getElementById("study").value;
    const attendance = document.getElementById("attendance").value;
    const previous = document.getElementById("previous").value;
    const sleep = document.getElementById("sleep").value;

    const result = document.getElementById("result");

    if (!study || !attendance || !previous || !sleep) {
        result.innerText = "⚠️ Please fill all fields!";
        return;
    }

    try {
        const response = await fetch("https://student-marks-predictor1.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                study_hours: parseFloat(study),
                attendance: parseFloat(attendance),
                previous_score: parseFloat(previous),
                sleep_hours: parseFloat(sleep)
            })
        });

        const data = await response.json();

        if (response.ok) {
            result.innerText = "✅ Predicted Marks: " + data.predicted_marks;
        } else {
            result.innerText = "❌ Error: " + data.error;
        }

    } catch (error) {
        result.innerText = "🚫 Server not reachable!";
    }
}