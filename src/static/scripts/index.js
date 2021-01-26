let baseURL = "https://find-my-button.azurewebsites.net/"
window.onload = () => {

    document.getElementById('submit-btn').addEventListener("click", (e) => {
        e.preventDefault()
        submit()
    });
}

function submit() {
    console.log("click")
    let formData = new FormData(document.getElementById('form'))
    try{
        let result = await getResult(formData)
        console.log("Działa")
    } catch (err) {
        console.log(err)
    }
    
}

async function getResult(formData){
    let requestURL = baseURL + "url"
    let requestParam = {
        method: "POST",
        body: formData,
    };

    let res = await fetch(requestURL, requestParam)
    if (res.status === 200) {
        return res.body
    } else {
        throw res.status
    }
}