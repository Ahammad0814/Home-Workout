let ColorElement;
let State;

ColorElement = localStorage.getItem('Color');

function genderImgChange(element) {
    let imageElement1 = document.querySelector('.gender-img1');
    let imageElement2 = document.querySelector('.gender-img2');
    let buttonElement = document.querySelector('.gender-select-button');

    buttonElement.style.visibility = 'visible'

    if (element === 1) {
        imageElement1.style.opacity = '1';
        imageElement1.setAttribute('src', staticUrl + 'images/Men background.png')
        imageElement2.setAttribute('src', staticUrl + 'images/Women.png')
        imageElement2.style.opacity = '0.5'
        imageElement1.setAttribute('data-selected', 'true') 
        imageElement2.setAttribute('data-selected', 'false') 
        localStorage.setItem('Gender','Men')

    }else if (element === 2) {
        imageElement2.style.opacity = '1';
        imageElement1.setAttribute('src', staticUrl + 'images/Men.png')
        imageElement2.setAttribute('src', staticUrl + 'images/Women background.png')
        imageElement1.style.opacity = '0.5'
        imageElement2.setAttribute('data-selected', 'true')
        imageElement1.setAttribute('data-selected', 'false')
        localStorage.setItem('Gender','Women')
    }
    buttonElement.value = 'true';
    DefaultColor();
    localStorage.setItem('Color', ColorElement)
    document.documentElement.style.setProperty('--Color', ColorElement);
}

function genderSelected() {
    let buttonElement = document.querySelector('.gender-select-button')
    let divElement = document.querySelector('.main-div')
    let levelElement = document.querySelector('.select-level');
    let backwardElement = document.querySelector('.Backward');

    document.querySelector('.Backward').style.visibility = 'visible';
    
    if (buttonElement.value === 'true') {
        divElement.style.left = '-700px';
        divElement.style.transform = 'scale(0)';
        setTimeout(function() {
            levelElement.style.transform = 'scale(1)';
            levelElement.style.left = '0';
        }, 400)
    }
    backwardElement.setAttribute('data-selected', '1')
}

function DefaultColor() {
    let imageElement1 = document.querySelector('.gender-img1');
    let imageElement2 = document.querySelector('.gender-img2');

    if (imageElement1.getAttribute('data-selected') === 'true') {
        ColorElement = 'rgb(0, 101, 255)';
    } else if (imageElement2.getAttribute('data-selected') === 'true') {
        ColorElement = 'rgba(249, 31, 100, 1)';
    } else {
        ColorElement = 'lightgrey';
    }
}

DefaultColor()

function LevelButtonSelect(element) {
    let levelElement1 = document.querySelector('.level-btn1');
    let levelElement2 = document.querySelector('.level-btn2');
    let levelElement3 = document.querySelector('.level-btn3');
    let levelButton = document.querySelector('.level-btn');
    let submitElement = document.querySelector('.level-btn');

    levelButton.style.visibility = 'visible'

    submitElement.value = 'true';
    levelButton.style.backgroundColor = ColorElement;

    levelElement1.style.backgroundColor = '#ffff';
    levelElement1.style.color = 'black';
    levelElement2.style.backgroundColor = '#ffff';
    levelElement2.style.color = 'black';
    levelElement3.style.backgroundColor = '#ffff';
    levelElement3.style.color = 'black';

    if (element === 1) {
        levelElement1.style.backgroundColor = ColorElement;
        levelElement1.style.color = '#ffff';
    } else if (element === 2) {
        levelElement2.style.backgroundColor = ColorElement;
        levelElement2.style.color = '#ffff';
    } else if (element === 3) {
        levelElement3.style.backgroundColor = ColorElement;
        levelElement3.style.color = '#ffff';
    }
    document.querySelector('.level-btn').value = 'true';
}

function Backward() {
    let divElement = document.querySelector('.main-div');
    let levelElement = document.querySelector('.select-level');
    let backwardElement = document.querySelector('.Backward');
    let measurementElement = document.querySelector('.measurements-div');
    
    if (backwardElement.getAttribute('data-selected') === '1'){
        document.querySelector('.Backward').style.visibility = 'hidden';
        levelElement.style.transform = 'scale(0)';
        levelElement.style.left = '580px';
        setTimeout(function() {
            divElement.style.left = '8px';
            divElement.style.transform = 'scale(1)';
        }, 400)
    }else if (backwardElement.getAttribute('data-selected') === '2'){
        measurementElement.style.left = '540px';
        measurementElement.style.transform = 'scale(0)';
        setTimeout(function() {
            levelElement.style.left = '0';
            levelElement.style.transform = 'scale(1)';
        }, 400)
        backwardElement.setAttribute('data-selected', '1')
    }
}

let kgElement = document.querySelector('.kg-btn');
let lbElement = document.querySelector('.lb-btn');
let cmElement = document.querySelector('.cm-btn');
let ftElement = document.querySelector('.ft-btn');

function measurementKeys(element) {

    if (element === 'kg' || element === 'cm'){
        measurementColor()
    }else if (element === 'lb' || element === 'ft') {
        kgElement.style.backgroundColor = '#ffff';
        kgElement.style.color = 'black'
        cmElement.style.backgroundColor = '#ffff';
        cmElement.style.color = 'black'
        lbElement.style.backgroundColor = ColorElement
        lbElement.style.color = '#ffff'
        ftElement.style.backgroundColor = ColorElement
        ftElement.style.color = '#ffff'
    }
}

function measurementColor() {
    kgElement.style.backgroundColor = ColorElement;
    kgElement.style.color = '#ffff'
    cmElement.style.backgroundColor = ColorElement;
    cmElement.style.color = '#ffff'
    lbElement.style.backgroundColor = '#ffff'
    lbElement.style.color = 'black'
    ftElement.style.backgroundColor = '#ffff'
    ftElement.style.color = 'black'
}

function levelSubmit() {
    let levelElement = document.querySelector('.select-level');
    let measurementElement = document.querySelector('.measurements-div');
    let backwardElement = document.querySelector('.Backward');
    let submitElement = document.querySelector('.level-btn');

    if (submitElement.value === 'true') {
        levelElement.style.left = '-580px';
        levelElement.style.transform = 'scale(0)';
        setTimeout(function() {
            measurementElement.style.left = '0';
            measurementElement.style.transform = 'scale(1)';
        }, 400)
        measurementColor()
        backwardElement.setAttribute('data-selected', '2')
    }
}

function Measurementbtn() {
    let buttonElement = document.querySelector('.measurements-submit-btn')
    buttonElement.style.backgroundColor = ColorElement;
    buttonElement.style.visibility = 'visible';
}
