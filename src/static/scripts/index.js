let baseURL = "http://127.0.0.1:5000/"
window.onload = () => {

    document.getElementById('submit-btn').addEventListener("click", (e) => {
        e.preventDefault()
        submit()
    });
}

async function submit() {
    console.log("click")
    let formData = new FormData(document.getElementById('form'))
    try{
        let result = await getResult(formData)
        document.write(result)
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
        return await res.text()
    } else {
        throw res.status
    }
}
