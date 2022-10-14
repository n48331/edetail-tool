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

        /*$('.bottompopup').unbind().bind('touchstart tap', function () {
            $('#infopopup').show();
            $('#mainWrapper').addClass("not_to_swipe");
        });
        $('#infoclose').unbind().bind('touchstart tap', function () {
            $('#infopopup').hide();
            $('#mainWrapper').removeClass("not_to_swipe");
            return false;
        });*/
        
    })
    '''

    os.makedirs(os.path.dirname(
        f"{destination_folder}/css/"), exist_ok=True)
    os.makedirs(os.path.dirname(
        f"{destination_folder}/js/"), exist_ok=True)
    css_file = open(f"{destination_folder}/css/style.css", "w+")
    css_file.write(css)
    css_file.close()
    js_file = open(f"{destination_folder}/js/slideScript.js", "w+")
    js_file.write(js)
    js_file.close()


def createHtml(project_name, destination_folder):
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
			currentSlide = "s1";
			document.addEventListener("touchmove", function (e) {{ e.preventDefault() }});
		</script>
		<script src="../shared/{project_name}_SharedResource/common/framework.js" charset="utf-8"></script>
	</head>
	<body>
		<div id="mainWrapper">

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
    f = open(f"{destination_folder}/{project_name}.html", "w+")
    f.write(text)
    f.close()
