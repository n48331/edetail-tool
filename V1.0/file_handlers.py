import os


def generateCssJs(destination_folder):
    css = '''
    #mainWrapper {
        overflow: hidden;
        position: absolute;
        left: 0;
        top: 0;
        width: 1024px;
        height: 768px;
        background: url("../img/main.jpg");
        background-size: cover;
        background-repeat: no-repeat;
    }
    '''

    js = '''
    $(document).ready(function () {

    })
    '''

    css_file = open(f"{destination_folder}/css/style.css", "w+")
    css_file.write(css)
    css_file.close()
    js_file = open(f"{destination_folder}/js/slideScript.js", "w+")
    js_file.write(js)
    js_file.close()


def createHtml(folder_name, project_name, destination_folder, sl):
    js = '''
	<script type="text/javascript">
			$(function () {
				$('#mainWrapper').swipeEvents();  //Add main ID or CLASS
				$("#menu01, #menu02, #menu03, #menu, #menuHover, #menuList, #menu04, #ref, #spc, #pi").bind("touchmove", function (e) {  //Add all the links to prevent the touchmove
					e.preventDefault();
				});
			});
		</script>
	'''
    text = f'''
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<title>{project_name}</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
		<link rel="stylesheet" href="../shared/{project_name}_SharedResource/common/mainstyle.css">
		<link rel="stylesheet" href="css/style.css">
		<script type="text/javascript" src="../shared/{project_name}_SharedResource/common/config.js"></script>
		<script>
			currentSlide = "s{sl}";
			document.addEventListener("touchmove", function (e) {{ e.preventDefault() }});
		</script>
		<script src="../shared/{project_name}_SharedResource/common/framework.js" charset="utf-8"></script>
	</head>
	<body>
		<div id="mainWrapper">
        <div data-info="" data-slide="s" data-flow="f0" class="btn goToButton"></div>
		</div>
		<script src="../shared/{project_name}_SharedResource/common/adaptive/zepto.min.js"></script>
		<script src="../shared/{project_name}_SharedResource/common/adaptive/underscore-min.js"></script>
		<script src="../shared/{project_name}_SharedResource/common/adaptive/adaptive.js"></script>
		<script src="../shared/{project_name}_SharedResource/common/jquery-1.10.2.min.js"></script>
		<script src="../shared/{project_name}_SharedResource/common/jquery.swipe-events.js" charset="utf-8"></script>
		<script src="../shared/{project_name}_SharedResource/common/jquery.touchSwipe.min.js"></script>
		<script src="../shared/{project_name}_SharedResource/common/clm-library-1.4.js" charset="utf-8"></script>
		<script src="../shared/{project_name}_SharedResource/common/baseScript.js" charset="utf-8"></script>
		<script src="../shared/{project_name}_SharedResource/common/customScript.js" charset="utf-8"></script>
		<script src="js/slideScript.js" charset="utf-8"></script>
		{js}
	</body>
	</html>
	'''
    f = open(f"{destination_folder}/{folder_name}.html", "w+")
    f.write(text)
    f.close()


def renameSharedFiles(src, project_name):
    os.rename(f'{src}/SharedResource',
              f'{src}/{project_name}_SharedResource')
    os.rename(f'{src}/{project_name}_SharedResource/SharedResource.html',
              f'{src}/{project_name}_SharedResource/{project_name}_SharedResource.html')
    os.rename(f'{src}/{project_name}_SharedResource/full.jpg',
              f'{src}/{project_name}_SharedResource/{project_name}_SharedResource-full.jpg')
    os.rename(f'{src}/{project_name}_SharedResource/thumb.jpg',
              f'{src}/{project_name}_SharedResource/{project_name}_SharedResource-thumb.jpg')


def createConfig(project_name, slide_names, dest):
    # for name in slide_names:
    slides = ''
    s = ''
    for i in range(len(slide_names)):
        s += f'"s{str(i+1)}",'
        slides += f'''
        s{i+1}: {{
        name: "s{i+1}",
        zipFile: "{slide_names[i]}.zip",
        }},
        '''

    config = f'''var config = {{
        project: "{project_name}",
        slides: {{
        {slides}
        }},
        coreflow: {{
            /*First flow should have all the slides*/
            f0: {{
            content: [{s}],
            name: "Flow 0",
            }},
        
            }},

            }};

	'''
    f = open(f"{dest}/config.js", "w+")
    f.write(config)
    f.close()
