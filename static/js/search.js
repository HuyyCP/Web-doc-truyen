// init click behaviour
document.querySelectorAll('.genre-item').forEach((item) => {
    var itemId = item.getAttribute('data-id')
    var genresIncluded = document.querySelector('[name="genresIncluded"]')
    var genresExcluded = document.querySelector('[name="genresExcluded"]')
    
    item.addEventListener('click', () => {
        if (item.classList == 'genre-item empty-box') {
            item.classList = 'genre-item tick-box'
            genresIncluded.value += ',' + itemId
            genresIncluded.value = genresIncluded.value.replace(/^,/, '').replace(/,$/, '');
        } else if (item.classList == 'genre-item tick-box') {
            item.classList = 'genre-item cross-box'
            genresIncluded.value = ',' + genresIncluded.value + ','
            genresIncluded.value = genresIncluded.value.replace(',' + itemId + ',', ',').replace(/^,/, '').replace(/,$/, '');
            genresExcluded.value = genresExcluded.value + ',' + itemId
            genresExcluded.value = genresExcluded.value.replace(/^,/, '').replace(/,$/, '');
        } else if (item.classList == 'genre-item cross-box') {
        item.classList = 'genre-item empty-box'
            genresExcluded.value = ',' + genresExcluded.value + ','
            genresExcluded.value = genresExcluded.value.replace(',' + itemId + ',', ',').replace(/^,/, '').replace(/,$/, '');
        }
        // console.log('Include: ' + genresIncluded.value)
        // console.log('Exclude: ' + genresExcluded.value)
    })
})

// reset filter to empty
document.getElementById('resetFilter').addEventListener('click', () => {
    document.querySelectorAll('.genre-item').forEach((e) => {
        e.classList = 'genre-item empty-box'
    })
})


// submit search form
const form = document.getElementById('searchForm');
mangaBriefTemplate = document.getElementById('manga-brief')
mangasPreviewPane = document.querySelector('.trending__product')

form.addEventListener('submit', function(event) {
    event.preventDefault();
    mangasPreviewPane.innerHTML = ''

    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    }
    
    console.log(form.action)
    console.log(form.method)

    var genresIncluded = document.querySelector('[name="genresIncluded"]')
    var genresExcluded = document.querySelector('[name="genresExcluded"]')
    body = JSON.stringify({
        'genresIncluded': genresIncluded.value,
        'genresExcluded': genresExcluded.value,
    })

    fetch(form.action, {
        method: form.method,
        headers: headers,
        body: body,
    })
    .then(response => response.text())
    .then(result => {

        // đầnjango
        result = JSON.parse(result)
        // console.log(result)
        mangas = JSON.parse(result.mangas)
        // console.log(mangas);
        totalChapters = result.totalChapters
        // console.log(totalChapters);

        if (mangas.length == 0) {
            const p = document.createAttribute('span')
            p.textContent = 'No chapter'
            mangasPreviewPane.appendChild(p)
        } else {
            for(let i = 0; i < mangas.length; i++) {
                mangaBrief = mangaBriefTemplate.cloneNode(true)
                mangaBrief.classList.remove('hidden')
                mangaBrief.classList.add('manga-item')
                mangaBrief.querySelector('.product__item').querySelector('a').href =  `/manga/${mangas[i].fields.slug}`
                mangaBrief.querySelector('.product__item__pic').setAttribute('data-setbg', mangas[i].fields.avatarLink)
                mangaBrief.querySelector('.ep').textContent = totalChapters[i] + ' chapters'
                mangaBrief.querySelector('.ep').textContent = totalChapters[i] + ' chapters'
                let title = mangaBrief.querySelector('h5')
                title.innerHTML = `<a href=/manga/${mangas[i].fields.slug}>${ mangas[i].fields.title }</a>`
                mangasPreviewPane.appendChild(mangaBrief)
                
                $('.set-bg').each(function () {
                    var bg = $(this).data('setbg');
                    $(this).css('background-image', 'url(' + bg + ')');
                });
            }
        }
    })
    .catch(error => {
        console.error(error);
    });

    // console.log('Include: ' + genresIncluded.value)
    // console.log('Exclude: ' + genresExcluded.value)

});
