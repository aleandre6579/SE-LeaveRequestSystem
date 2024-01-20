async function sendRequest(method, url) {
    try {
        let res = await fetch(url, {method: method})
        location.reload()
    } catch (e) {
        console.log(e)
    }

}