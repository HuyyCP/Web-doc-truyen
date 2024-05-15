// listManga = document.currentScript.getAttribute('list-manga')
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('uploadMangaButton').addEventListener('click', (e) => {
        e.preventDefault()
        window.location.href = '/manga/upload'
    })
    
    console.log(listManga)
    console.log(JSON.stringify(listManga[0]))
    console.log(document.querySelectorAll('.add-chapter'))
    document.querySelectorAll('.add-chapter').forEach((element, index) => {
        element.addEventListener('click', (e) => {
            e.preventDefault()
            window.location.href = `/manga/${listManga[index].slug}/add-chapter`
            console.log(`/manga/${listManga[index].slug}/add-chapter`)
        })
    })

})