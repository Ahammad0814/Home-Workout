let staticUrl = '/static/';
let ColorElement;
let ButtonColorElement;
let innerHTML = '';
let SpecificNumber = 0;
let LData = document.querySelector('.Focus-Area-pointers').getAttribute('data-myvalue');
let DataArray = LData.split(',')
let Gender = localStorage.getItem('Gender');


if (Gender === 'Men'){
    document.querySelector('.Profile-pic').src = staticUrl + 'images/Men-Profile.jpg';
    ColorElement = 'rgb(0, 101, 255)';
}else if (Gender === 'Women'){
    document.querySelector('.Profile-pic').src = staticUrl + 'images/Women-Profile.png';
    ColorElement = 'rgba(249, 31, 100, 1)';
}
document.documentElement.style.setProperty('--Color', ColorElement);

function capitalizeEveryWord(str) {
    let capitalizeWords = [];
    let words = str.split(' ');

    for (let word of words) {
        let capitalizedWord = word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
        capitalizeWords.push(capitalizedWord);
    }
    return capitalizeWords.join(' ');
}
let titleElement = document.querySelector('.page-title');
let nameElement = document.querySelector('.page-name').innerHTML;

let title = nameElement.replace('&amp;','&');
titleElement.textContent = capitalizeEveryWord(title);

for (let i = 0; i < DataArray.length; i++){
    if (!isNaN(DataArray[i])){
        SpecificNumber = DataArray[i];
    } else {
        if (SpecificNumber > 0){
            if (SpecificNumber >= i){
                ButtonColorElement = 'rgb(0, 101, 255)';
            } else {
                ButtonColorElement = 'rgba(112,175,255,255)';
            }
        }else{
            ButtonColorElement = 'rgb(0, 101, 255)';
        }
        innerHTML += `<a><button style="background-color: ${ButtonColorElement};"></button>${DataArray[i]}</a>`;
    }
}
document.querySelector('.Focus-Area-pointers').innerHTML = innerHTML;

function forwardButton(element) {
    let buttonElement1 = document.querySelector('.forward-btn')
    let buttonElement2 = document.querySelector('.backward-btn')

    if (element === 'Forward'){
        buttonElement1.setAttribute('value','true');
        buttonElement2.setAttribute('value','false');
    }else if (element === 'Backward') {
        buttonElement1.setAttribute('value','false');
        buttonElement2.setAttribute('value','true');
    }
}


function ButtonColor() {
    let buttonElement1 = document.querySelector('.forward-btn')
    let buttonElement2 = document.querySelector('.backward-btn')

    let idxElement1 = document.querySelector('.current-data-idx');
    let idxElement2 = document.querySelector('.data-length');

    if (parseInt(idxElement2.innerHTML) === 1){
        buttonElement1.style.backgroundColor = 'lightgrey';
        buttonElement2.style.backgroundColor = 'lightgrey';
    }
    else if (parseInt(idxElement1.innerHTML) === parseInt(idxElement2.innerHTML)){
        buttonElement2.style.backgroundColor = 'lightgrey';
    }else if (parseInt(idxElement1.innerHTML) === 1){
        buttonElement1.style.backgroundColor = 'lightgrey';
    }
}
ButtonColor();

window.addEventListener('load', function(){
    window.speechSynthesis.cancel();
})

const buttonElement = document.querySelector('.Speak-Button');
const imgElement = document.querySelector('.Speak-btn-Img');

buttonElement.addEventListener('click', function(){
    if (buttonElement.value === 'Speak'){
        imgElement.src = staticUrl + 'images/SpeakerMute-Logo.png';
        buttonElement.value = 'Mute';

        const textToSpeak = Speak();
        const utterance = new SpeechSynthesisUtterance(textToSpeak);
        utterance.rate = 0.8;
        utterance.pitch = 1;
        utterance.volume = 1;
        utterance.voice = speechSynthesis.getVoices()[0];

        window.speechSynthesis.speak(utterance);

        utterance.addEventListener('end', function() {
            imgElement.src = staticUrl + 'images/Speaker-Logo.png';
            buttonElement.value = 'Speak';
        });
          
    } else if (buttonElement.value === 'Mute'){
        imgElement.src = staticUrl + 'images/Speaker-Logo.png';
        buttonElement.value = 'Speak';
        window.speechSynthesis.cancel();
    }
});

function Speak() {
    const textElement1 = document.querySelector('.text1').innerText;
    const textElement2 = document.querySelector('.text2').innerText;

    const textMerge = textElement1 + ' ' + textElement2;

    const textReplace = textMerge.replace('pronunciation1', 'pronunciation2');

    return textReplace;
}
