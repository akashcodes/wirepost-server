

/* Initialize key events for certain fields
 * For example - Prevent enter -> next line on single line fields
 * Allow shitf+enter to shift to next line on multi-line fields
 * TODO:
 */

document.getElementById(para_button).onmousedown = ev => {
    // Add new paragraph
    console.log(ev.srcElement.parentNode);
    ev.srcElement.parentNode.insertBefore(createTextBox(), ev.srcElement);
};

function createTextBox(placeholder="Insert Text Here", multiline=true) {
    var textBox = document.createElement('p');

    initializeTextBoxEvents(textBox);

    if(multiline) {
        textBox.className = text_box_class+" "+multi_line_class;
        enableNextLine(textBox);
    } else {
        textBox.classList = text_box_class+" "+single_line_class;
    }
    
    textBox.setAttribute('data-placeholder', placeholder);
    textBox.setAttribute('contenteditable', true);

    return textBox;
}