const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const results = document.getElementById('results-row')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (mobile) => {
    $.ajax({
        type: 'POST',
        url: 'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'mobile': mobile,
        },
        success: (res) => {
            console.log(res)
            const data = res.data
            if (Array.isArray(data)) {
                data.forEach( mobile=> {
                    results += `
                    <a href="">
                        <div>
                            <img src="${mobile.image}"> <br><br>
                            <h5>Model : ${mobile.modelName}</h5>
                        </div>
                    `
                })
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', e=> {
    console.log(e.target.value)

    if (results.classList.contains('not-visible')){
        results.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)
})