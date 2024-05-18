document.addEventListener('DOMContentLoaded', () => {

    // window.addEventListener('load', () => {
    //     showOverlay()
    // })

    window.addEventListener('beforeunload', () => {
        showOverlay()
    })
    
    // window.addEventListener('unload', () => {
    //     hideOverlay()
    // })

    function showOverlay() {
        document.querySelector('.overlay').style.display = 'flex'
    }

    function hideOverlay() {
        document.querySelector('.overlay').style.display = 'none'
    }
}) 