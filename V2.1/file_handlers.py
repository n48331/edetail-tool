import os
from PIL import Image
import random


def r(): return random.randint(0, 255)

#Buttons
def goToButton(x=1):
    goToButtons = ''
    for i in range(x):
        goToButtons += f'<div class="gotoBtn{i+1} goToButton" data-slide="s" data-flow="f0" data-info=""></div>\n'
    return goToButtons


def goToHomeButton(x=1):
    goToHomeButtons = ''
    for i in range(x):
        goToHomeButtons += f'<div class="Btn{i+1} goToHomeButton" data-flow="f0" data-slide="s" sub_slide=""></div>\n'
    return goToHomeButtons


def gotoSubParent(x=1):
    return '<div class="close" onclick="app.gotoSubParent()"></div>\n'

def carousalBtn(x=1):
    carousalBtns = ''
    for i in range(x):
        carousalBtns += f'<div class="slideBtn{i+1}" data-target="#carousel-example-generic" data-slide-to="{i+1}"></div>\n'
    return carousalBtns


def slideCss(slides):
    carousal = ''
    single_slide = f'''
        background: url("../img/{slides[0]}");
        background-size: cover;
        background-repeat: no-repeat;
        '''
    css = f'''#mainWrapper {{
        overflow: hidden;
        position: absolute;
        left: 0;
        top: 0;
        width: 1024px;
        height: 768px;
        {single_slide if len(slides)<=1 else ''}
    }}
    '''
    if len(slides)>1:
        carousal = '''
    .body_main {
    width: 1024px;
    height: 768px;
    position: absolute;
    top: 0px;
    left: 0px;
    }
    '''
        for index,slide in enumerate(slides):
            carousal +=f'''
            .section-{index+1} {{
    position: relative;
    left: 0;
    top: 0;
    width: 1024px;
    height: 768px;
    background: url("../img/{slide}");
    background-size: cover;
    background-repeat: no-repeat;
}}
            ''' 
        
    return css+carousal

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
            background: url("../img/{popups[i]}") no-repeat;
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
        # TODO add carousal css and config

    css = slideCss(slides) + popup_css
   

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

# TODO Add slides as parameter,take a copy of this file

def makeCarousal(slides):
    innerHtml=''
    for idx,slide in enumerate(slides):
        innerHtml+=f'''
        <div class="item{' active' if idx==0 else ''}">
			<section class="section-{idx+1}">
				<div class="body_main">
				</div>
			</section>
		</div>
        '''
    return f'''
    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel" data-interval="false"
			data-wrap="false">
			<div class="carousel-inner" role="listbox">
            {innerHtml}
            </div>
	</div>
    '''

def createHtml(id, folder_name, destination_folder, sl,slides, popupCount,buttons):
    carousal = makeCarousal(slides) if len(slides)>1 else ''
    popup = ''
    if (popupCount == None):
        popupCount = 0
    for i in range(popupCount):
        popup += f'''<div class="s{sl}_popupbtn{i+1}">{i+1}</div>
        <div class="popup_box_{i+1} noSwipe">
            <div class="close"></div>
        </div>'''
    all_buttons = CreateButtons(buttons)
    js = '''
	
	'''
    text = f'''<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<title>{id}</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="../shared/{id}_SharedResource/common/mainstyle.css">
		<link rel="stylesheet" href="css/style.css">
        <!-- Carousel external files -->
	<link rel="stylesheet" href="../shared/{id}_SharedResource/common/carousel/css/bootstrap.min.css">
	<link rel="stylesheet" href="../shared/{id}_SharedResource/common/carousel/css/carousel-style.css">
	<!-- Carousel external files -->
		<script type="text/javascript" src="../shared/{id}_SharedResource/common/config.js"></script>
		<script>
			currentSlide = "s{sl}";
			document.addEventListener("touchmove", function (e) {{ e.preventDefault() }});
		</script>
		<script src="../shared/{id}_SharedResource/common/framework.js" charset="utf-8"></script>
	</head>
	<body>
		<div id="mainWrapper">
       
		{carousal}
        {popup}

        {all_buttons}
		</div>
		<script src="../shared/{id}_SharedResource/common/adaptive/zepto.min.js"></script>
		<script src="../shared/{id}_SharedResource/common/adaptive/underscore-min.js"></script>
		<script src="../shared/{id}_SharedResource/common/adaptive/adaptive.js"></script>
		<script src="../shared/{id}_SharedResource/common/jquery-1.10.2.min.js"></script>
		<script src="../shared/{id}_SharedResource/common/jquery.swipe-events.js" charset="utf-8"></script>
		<script src="../shared/{id}_SharedResource/common/jquery.touchSwipe.min.js"></script>
		<script src="../shared/{id}_SharedResource/common/clm-library-1.4.js" charset="utf-8"></script>
		<script src="../shared/{id}_SharedResource/common/baseScript.js" charset="utf-8"></script>
		<script src="../shared/{id}_SharedResource/common/customScript.js" charset="utf-8"></script>
        <script src="../shared/{id}_SharedResource/common/carousel/js/carouselScript.js" charset="utf-8"></script>
	<script src="../shared/{id}_SharedResource/common/carousel/js/bootstrap.min.js"></script>
		<script src="js/slideScript.js" charset="utf-8"></script>
		{js}
	</body>
	</html>
	'''
    f = open(f"{destination_folder}/{folder_name}.html",
             "w+", encoding='utf-8')
    f.write(text)
    f.close()


def generateSharedHtml(project_id, src):
    html = f'''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{project_id}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../shared/{project_id}_SharedResource/common/mainstyle.css">
        <link rel="stylesheet" href="css/style.css">
        <script>
            document.addEventListener("touchmove",function(e){{e.preventDefault()}});
        </script>
    </head>

    <body>
        <div id="mainWrapper">
            
        </div>
        <script src="../shared/{project_id}_SharedResource/common/jquery-1.10.2.min.js"></script>
        <script src="../shared/{project_id}_SharedResource/common/jquery.swipe-events.js" charset="utf-8"></script>
        <script src="../shared/{project_id}_SharedResource/common/jquery.touchSwipe.min.js"></script> 
        <script src="../shared/{project_id}_SharedResource/common/clm-library-1.4.js" charset="utf-8"></script> 
        <script type="text/javascript" src="common/config.js"></script>
        <script src="js/slideScript.js" charset="utf-8"></script>
    </body>

    </html>'''
    # os.rename(f'{src}/{project_name}_SharedResource/SharedResource.html',
    #               f'{src}/{project_name}_SharedResource/{project_name}_SharedResource.html')
    f = open(f"{src}", "w+", encoding='utf-8')
    f.write(html)
    f.close()


def renameSharedFiles(src, project_id, img_name):
    if not os.path.exists(f'{src}/{project_id}_SharedResource'):
        os.rename(f'{src}/SharedResource',
                  f'{src}/{project_id}_SharedResource')
    imageResize(img_name, (1024, 768),
                f'{src}/{project_id}_SharedResource/{project_id}_SharedResource-full.jpg')
    imageResize(img_name, (200, 150),
                f'{src}/{project_id}_SharedResource/{project_id}_SharedResource-thumb.jpg')
    return f'{src}/{project_id}_SharedResource/{project_id}_SharedResource.html'


def createConfig(project_name,carousal_slides, slide_names, dest):
    slides_zip = ''
    s = []
    for i in range(len(slide_names)):
        s.append(f"s{str(i+1)}")
        
        slides_zip += f'''
        s{i+1}: {{
        name: "s{i+1}",
        zipFile: "{slide_names[i]}.zip",
        }},
        '''

    config = f'''var config = {{
        project: "{project_name}",
        slides: {{
        {slides_zip}
        }},
        coreflow: {{
            /*First flow should have all the slides*/
            f0: {{
            content: {s},
            name: "Flow 0",
            }},      
            }},
             "carSlide": {carousal_slides},
            }};

	'''
    f = open(f"{dest}/config.js", "w+", encoding='utf-8')
    f.write(config)
    f.close()


def imageResize(image, size, dest):
    
    img =  Image.open(f'{image}')
    img.convert('RGB').resize(size).save(f'{dest}')
    return 'Image resized'

def CreateButtons(buttons):
    all_buttons=''
    for button in buttons:
        all_buttons+=eval(button)
    return all_buttons