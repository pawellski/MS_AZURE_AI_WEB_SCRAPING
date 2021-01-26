window.onload = () => {

    document.getElementById('submit-btn').addEventListener("click", (e) => {
        e.preventDefault()
        submit()
    });
}

function submit() {
    console.log("click")
    let formData = new FormData(document.getElementById('form'))

}