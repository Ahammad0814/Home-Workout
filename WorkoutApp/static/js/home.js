let MenBeginnerData = [
    ['images/B_Abs.jpg','ABS','16'],['images/B_Chest.png','CHEST','11'],['images/B_Arm.jpg','ARM','19'],['images/B_Back.jpg','SHOULDER & BACK','17'],['images/B_Leg.jpg','LEG','15']
]
let MenIntermediateData = [
    ['images/I_Abs.png','ABS','21'],['images/I_Chest.jpg','CHEST','14'],['images/I_Arm.jpg','ARM','25'],['images/I_Back.png','SHOULDER & BACK','17'],['images/I_Leg.jpg','LEG','22']
]
let MenAdvancedData = [
    ['images/A_Abs.jpg','ABS','21'],['images/A_Chest.jpg','CHEST','14'],['images/A_Arm.jpg','ARM','25'],['images/A_Back.jpg','SHOULDER & BACK','17'],['images/A_Leg.jpg','LEG','40']
]

let WomenBeginnerData = [
    ['images/W_B_Abs.jpg','ABS','16'],['images/W_B_Chest.jpeg','CHEST','11'],['images/W_B_Arm.png','ARM','19'],['images/W_B_Back.jpg','SHOULDER & BACK','23'],['images/W_B_Leg.png','LEG','15']
]
let WomenIntermediateData = [
    ['images/W_I_Abs.jpg','ABS','21'],['images/W_I_Chest.jpg','CHEST','14'],['images/W_I_Arm.png','ARM','25'],['images/W_I_Back.png','SHOULDER & BACK','17'],['images/W_I_Leg.png','LEG','22']
]
let WomenAdvancedData = [
    ['images/W_A_Abs.jpg','ABS','21'],['images/W_A_Chest.png','CHEST','14'],['images/W_A_Arm.png','ARM','25'],['images/W_A_Back.png','SHOULDER & BACK','17'],['images/W_A_Leg.png','LEG','40']
] 


let LevelData;
let InnerHtmlData = '';
let Level;
let LevelImg;
let staticUrl = '/static/';
let Gender = localStorage.getItem('Gender');
let BeginnerData;
let IntermediateData;
let AdvancedData;
if (Gender === 'Men'){
    BeginnerData = MenBeginnerData;
    IntermediateData = MenIntermediateData;
    AdvancedData = MenAdvancedData;
    document.querySelector('.Profile-pic').src = staticUrl + 'images/Men-Profile.jpg';
    document.documentElement.style.setProperty('--color', 'rgb(0, 101, 255)');
}
else if (Gender === 'Women'){
    BeginnerData = WomenBeginnerData;
    IntermediateData = WomenIntermediateData;
    AdvancedData = WomenAdvancedData;
    document.querySelector('.Profile-pic').src = staticUrl + 'images/Women-Profile.png';
    document.documentElement.style.setProperty('--color', 'rgba(249, 31, 100, 1)');
}

let containerCount = 0;
for (let Total = 0; Total < 3; Total++) {
    if (Total === 0) {
        Level = 'BEGINNER';
        LevelData = BeginnerData;
        LevelImg = 'images/B1.png';
    } else if (Total === 1) {
        Level = 'INTERMEDIATE';
        LevelData = IntermediateData;
        LevelImg = 'images/I1.png';
    } else if (Total === 2) {
        Level = 'ADVANCED';
        LevelData = AdvancedData;
        LevelImg = 'images/A1.png';
    }

    InnerHtmlData += `<div class="begi-div1">
                    <h2>${Level}</h2>`;
    for (let Data = 0; Data < LevelData.length; Data++) {
        InnerHtmlData +=
            `<a class="Container Container-${containerCount}"><img class="img img-${Data}" src="${staticUrl + LevelData[Data][0] }"><img class="B1 B1-${Data}" src="${staticUrl + LevelImg}">
            <h3>${LevelData[Data][1]} ${Level}</h3><p>${LevelData[Data][2]} EXERCISES</p></a>`;
        containerCount +=1
    }   
    InnerHtmlData += `</div>`;
}
document.querySelector('.home-main-div').innerHTML = InnerHtmlData;


function SideMiniBar() {
    let txtElement = document.querySelector('.sidebar-txt');
    let divElement = document.querySelector('.SideBar');
    console.log(txtElement.getAttribute('value'))

    if (txtElement.getAttribute('value') === 'Close'){
        divElement.style.width = '300px';
        txtElement.style.visibility = 'visible';
        txtElement.setAttribute('value','Open');

    }else if (txtElement.getAttribute('value') === 'Open'){
        txtElement.style.visibility = 'hidden';
        divElement.style.width = '0px';
        txtElement.setAttribute('value','Close');
    }
}