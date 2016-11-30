function openNav() {
            document.getElementById("mySidenav").style.width = "250px";
            document.getElementById("main").style.marginLeft = "250px";
        }
        
        function closeNav() {
            document.getElementById("mySidenav").style.width = "0";
            document.getElementById("main").style.marginLeft= "0";
        }
                    
        window.onload = function(){
            // Change this value to however many seconds you want to delay the text by.
            var theDelay = 1;
            var timer = setTimeout("showText()",theDelay*1000)
        }
        function showText(){
            document.getElementById("delayedText").style.visibility = "visible";
        }