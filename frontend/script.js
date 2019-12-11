/* eslint-env es6 */
/* eslint-disable */
const canvas = document.querySelector('#canvas');
const temp_canvas = document.querySelector('#canvas_temp');
const final = document.querySelector('#final');
const ctx = canvas.getContext('2d');
const penColor = document.querySelector('input[name="penColor"]');
const penWidth = document.querySelector('input[name="penWidth"]');
const saver = document.querySelector('#saver')


ctx.strokeStyle = '#000000';
ctx.lineJoin = 'round';
ctx.lineCap = 'round'
ctx.lineWidth = 5;
let pen = {
    x:0,
    y:0,
    down:false
}

let image = {
    x_h:-1,
    y_h:-1,
    x_l:800,
    y_l:600
}

// saver:addEventListener('dblclick', saveFile);
canvas.addEventListener('mousedown', penDown);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', noDown);
canvas.addEventListener('mouseout', noDown);

$(document).ready(function(){
    $('#resetCanvas').click(function(){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    })
    $('#saver').click(function(){
        saveFile()
    })
})



function draw(e){
    if(!pen.down) return;
    ctx.lineWidth = penWidth.value;
    //console.log("Pen width " + ctx.lineWidth);
    ctx.strokeStyle = penColor.value;
    ctx.beginPath();
    ctx.moveTo(pen.x, pen.y);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
    [pen.x, pen.y] = [e.offsetX, e.offsetY];
    if(pen.x > image.x_h) image.x_h = pen.x;
    if(pen.x < image.x_l) image.x_l = pen.x;
    if(pen.y > image.y_h) image.y_h = pen.y;
    if(pen.y < image.y_l) image.y_l = pen.y;
}

function noDown(){
    pen.down = false;
}

function penDown(e){
    pen.down = true;
    [pen.x, pen.y] = [e.offsetX, e.offsetY];
    
}



function saveFile(){

    $('#processing').removeClass('d-none')
    //console.log(image.x_h);
    //console.log(image.x_l);
    //console.log(image.y_h);
    //console.log(image.y_l);
    image_height = image.y_h - image.y_l;
    image_width = image.x_h - image.x_l;
    if(image_height > image_width){
        image_width = image_height;
    }
    else{
        image_height = image_width;
    }
    
    threshold = 20;
    var scale = 28/(image_height + 2 * threshold);
    //console.log("Scale " + scale.toString());
    
    let _image = canvas.toDataURL();
    var bitmap_image = ctx.getImageData(image.x_l-threshold, image.y_l-threshold, image_width + 2*threshold, image_height + 2*threshold);
    var newCanvas = $(temp_canvas).attr("width", bitmap_image.width).attr("height", bitmap_image.height)[0];
    newCanvas.getContext("2d").putImageData(bitmap_image, 0, 0);
    var resized_image = newCanvas.getContext("2d").getImageData(0, 0, bitmap_image.width, bitmap_image.height);
    newCanvas.height = 0;
    newCanvas.width = 0;
    console.log(resized_image.data.length);
    img_string = "";
    for(let i = 0; i < resized_image.data.length; i++){
        img_string += resized_image.data[i] + ",";
    }
    
    console.log(img_string);
    var dict = {
        'img': JSON.stringify(img_string),
    };
    
    var p = document.getElementById('story');
    url = 'http://localhost:9000/api/doodle2name';
    $.ajax({
         url:url,
         type:'POST',
         data: dict,
         success:function(json){
             output = JSON.parse(json).data;
             p.innerHTML = output;
             
            $('#processing').addClass('d-none')
         },
         error:function(){
             $('#modal').show()
             $('#processing').addClass('d-none')
         }      
    });
    
    
    //console.log(dict);
    //gettext_GPT();
    
}

function gettext_GPT(){
    
    var p = document.getElementById('story');
    url = 'http://localhost:9000/api/doodle2story';
    
    $.ajax({
         url:url,
         success:function(json){
             // do stuff with json (in this case an array)
             //console.log(json);
             output = JSON.parse(json).data;
             
             p.innerHTML = output;
         },
         error:function(){
             alert("Error");
         }      
    });
}


