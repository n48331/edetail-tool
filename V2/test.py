import random
import os
import shutil
def r(): return random.randint(0, 255)


destination_folder = f"./test/genCssJs"
source_folder = "./boiler_plate/slide"
if not os.path.exists(destination_folder):
    shutil.copytree(source_folder, destination_folder)

sl = 1
popups = 'Slide_4,Slide_4,Slide_4,Slide_4'
if (popups != None):
    popups = popups.split(',')
else:
    popups = ''


slides = 'Slide_4,Slide_4,Slide_4,Slide_4'
slides = slides.split(',')


print(len(slides),slides[0])


def generateCssJs(destination_folder,slides, popups, sl):
    popup_css = ''
    popup_js = ''
    for i in range(len(popups)):
        popup_css += f'''.s{sl}_popupbtn{i+1} {{
        background-color:{'#%02X%02X%02X' % (r(),r(),r())};
        opacity:.8;
        position: absolute;
        top: 50px;
        left: {30+i*45}px;
        height: 40px;
        width: 40px;
        cursor: pointer;
        }}

        .popup_box_{i+1} {{
            background: url("../img/{popups[i]}.jpg") no-repeat;
            background-size: 1024px 768px;
            position: absolute;
            width: 1024px;
            height: 768px;
            top: 0;
            display: none;
            left: 0;
        }}
        .popup_box_{i+1} .close {{
            background-color:red;
            opacity:.5;
            width: 45px;
            height: 45px;
            position: absolute;
            right: 51px;
            top: 62px;
            cursor: pointer;
        }}'''
        for i in range(len(popups)):
            popup_js += f'''	$(".s{sl}_popupbtn{i+1}").click(function(){{
            $(".popup_box_{i+1}").fadeIn();
            }});
            $(".popup_box_{i+1} .close").click(function(){{
                $(".popup_box_{i+1}").fadeOut();
            }});
        '''
    css = f'''#mainWrapper {{
        overflow: hidden;
        position: absolute;
        left: 0;
        top: 0;
        width: 1024px;
        height: 768px;
        
        {single_slide if len(slides)<1 else ''}
    }}
    {popup_css}
    '''

    js = f'''$(document).ready(function () {{
	 {popup_js}
    }})
    '''

    css_file = open(f"{destination_folder}/css/style.css",
                    "w+", encoding='utf-8')
    css_file.write(css)
    css_file.close()
    js_file = open(f"{destination_folder}/js/slideScript.js",
                   "w+", encoding='utf-8')
    js_file.write(js)
    js_file.close()
    print('test pass')

single_slide = f'''
 background: url("../img/{slides[0]}.jpg");
        background-size: cover;
        background-repeat: no-repeat;
'''
generateCssJs(destination_folder,slides, popups, sl)



css = f'''#mainWrapper {{
        overflow: hidden;
        position: absolute;
        left: 0;
        top: 0;
        width: 1024px;
        height: 768px;
        
    {single_slide if len(slides)<1 else ''}
       
    }}
    {'popup_css'}
    '''

from PIL import Image 
import PIL 
  
# creating a image object (main image) 
im1 = Image.open(r"test\genCssJs\img\main2.png") 
# Image.open(r"test\genCssJs\img\main.jpg").convert('RGB').save(r"test\genCssJs\img\main2.png")
print(im1.format)
# save a image using extension
