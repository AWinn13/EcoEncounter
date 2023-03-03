
// -----------------Land and Water hidden DIVS------------------------------------------------
function showDiv() {
    div = document.getElementById('forest_text');
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function showDiv1() {
    div = document.getElementById('grassland_text');
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function showDiv2() {
    div = document.getElementById('desert_text');
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function showDiv3() {
    div = document.getElementById('tundra_text');
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function showDiv4() {
    div = document.getElementById('wetland_text');
    if (div.style.display === "none"){
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}
function showDiv5() {
    div = document.getElementById('ocean_text');
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function showDiv6() {
    div = document.getElementById('river_text');
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function showDiv7() {
    div = document.getElementById('lake_text');
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function showDiv8() {
    div = document.getElementById('pond_text');
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}
// ------------------Light Box used CodePen Template as a reference-------------------

class Lightbox {
    constructor() {
        this.init()
    }

    init() {
        this.container = document.createElement('div');
        this.container.id = 'lightbox';
        document.body.appendChild(this.container);

        this.lightboxImg = document.createElement('img');
        this.container.appendChild(this.lightboxImg);

        this.addListeners();
    }

    addListeners() {
        const images = document.querySelectorAll('.gallery img');
        images.forEach(img => {
            img.addEventListener('click', () => this.galleryImgClicked(img))
        })

        this.container.addEventListener('click', () => {
            this.hideLightbox()
        })

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') this.hideLightbox()
        })
    }

    hideLightbox() {
        this.container.classList.remove('active')
    }

    galleryImgClicked = (img) => {
        this.lightboxImg.src = img.src;
        this.container.classList.add('active')
    }
}

const lightbox = new Lightbox()





