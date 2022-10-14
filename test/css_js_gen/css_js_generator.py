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
