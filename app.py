from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<body style='padding: 50px; color: #777; font-size: 14px; font-family: Georgia, serif; font-weight: normal; text-align: center;'>" \
             "<h2 style='font-size: 3.5em; line-height: 1em; text-align: center; margin-top: 0; font-weight: normal;'>Pa d’en Sergi</h2>" \
             "<h3 style='font-size: 1.75em; margin-top: -1.5em; letter-spacing: 0.2em; text-align: center; font-weight: normal;'>(<i>Fet en silenci</i>)</h3>" \
             "<h4 style='font-size: 1.5em; text-align: center; margin: 0.5em; font-weight: normal;'><b>Whatsapp:</b> 650 751 854</br>" \
             "<h4 style='font-size: 1.5em; text-align: center; margin: 0.5em; font-weight: normal;'><b>Correu electrònic:</b> " \
               "<a style='color: #777; text-decoration: none' href='mailto:padensergi@gmail.com'>padensergi@gmail.com</a></h4>" \
             "<h4 style='font-size: 1.5em; text-align: center; margin: 0.5em; font-weight: normal;'><b>Adreça:</b> Carrer Sant Pere 18, 08470, Sant Celoni</h4>" \
             "<h4 style='font-size: 1.5em; text-align: center; margin: 0.5em; font-weight: normal;'><b>Horari:</b> de dilluns a divendres de 17 a 20h - Dissabtes i diumenges tancat</h4>" \
             "<div style='margin: 60px 0; padding: 0;'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535188/padensergi/jzzeeg65bhjlgavucw0w.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535186/padensergi/q3ii8mkdmjnts3trc5rq.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535188/padensergi/mb0tfzfsg2b00s7qpduw.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535187/padensergi/nzs2khssnencrnba1c09.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535187/padensergi/mgzu5pinqbexesygwbob.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535187/padensergi/ujaleza2iyr18tn1l1ge.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535186/padensergi/ll9uguj20y930zhhhyru.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535187/padensergi/ij5md57c8bzakjladxxx.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535186/padensergi/xbbqkyf2x7cct6aoieh2.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535188/padensergi/oxwoshlmoh5kdnigsuga.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535186/padensergi/vhpvawqg4140mcwc90af.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535188/padensergi/umrrcholp39di7rvemei.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535186/padensergi/ucjcnk5erh039yyikms7.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535187/padensergi/wqzx5wfwopv0ickwb0a3.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535187/padensergi/mpnyrmqtbqk2kmgvlfci.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535187/padensergi/fxuntylb5rwbbzpvjvri.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535187/padensergi/z669pkpwv7p7ozkuxkdc.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535188/padensergi/dgbtp2vk7dogfifipruy.jpg'>" \
               "<img style='margin: 0 0 -5px 0; padding: 0; width: 95%;' src='https://res.cloudinary.com/oiueei/image/upload/v1676535186/padensergi/anhfeei7bcfum8y7nogz.jpg'>" \
               "<p style='font-size: 1.5em; line-height: 1.5; text-align: center;'>" \
                 "<img src='https://res.cloudinary.com/oiueei/image/upload/v1676535188/padensergi/kotay6301efwrtaqffah.jpg' style='width:90px;margin:100px auto'>" \
               "</p>" \
             "</div>" \
           "</body>"
