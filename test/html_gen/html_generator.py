
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
