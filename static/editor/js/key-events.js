/* Initialize key events for certain fields
 * For example - Prevent enter -> next line on single line fields
 * Allow shitf+enter to shift to next line on multi-line fields
 * TODO:
 */

// Callback function
// Takes in 2 parametets
function enableNextLine(elem) {
    elem.onkeydown = ev => {
        if(ev.keyCode == shiftKeyCode) {
            elem.nextLine = true;
        }
    };

    elem.onkeyup = ev => {
        if(ev.keyCode == shiftKeyCode) {
            elem.nextLine = false;
        }
    };
}

function initializeTextBoxEvents(elem) {
    elem.onkeypress = ev => {
        if(ev.keyCode == enterKeyCode) {
            if(!elem.nextLine){
                elem.blur();
            }
        }
    };
}


Array.from(document.getElementsByClassName(multi_line_class)).map((elem, index) => {
    enableNextLine(elem);
});


Array.from(document.getElementsByClassName(text_box_class)).map((elem, index) => {
    initializeTextBoxEvents(elem);
});