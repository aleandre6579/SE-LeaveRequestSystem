async function sendRequest(method, url) {
    try {
        let res = await fetch(url, {method: method}).then(data => data.json()).then(res => res)
        console.log(res)
        if ('delete_success' in res)
            location.reload()
    } catch (e) {
        console.log(e)
    }

}
