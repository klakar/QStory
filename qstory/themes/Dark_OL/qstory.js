// Initiate global variables
var current_page = 0;

// create the navigation controls
function addNavigation() {
    var html_source = '<button onClick="previousPage()">Previous</button>';
    html_source += '<button onClick="nextPage()">Next</button>';
    html_source += '<button onClick="firstPage()">Reset</button>';
    document.getElementById('story_footer').innerHTML = html_source;
}

// update the story page
function doPage(page) {
    // Open Layers
    document.getElementById('story_header').innerHTML = story_title[page];
    document.getElementById('story_body').innerHTML = story_content[page];
    map.getView().setCenter(ol.proj.transform(story_location[page], 'EPSG:4326', 'EPSG:3857'));
    map.getView().setZoom(story_zoom[page]);

}

// advance story by one page
function nextPage() {
    current_page++;
    if (current_page == story_content.length) {
        current_page = 0;
    }
    doPage(current_page);
}

// go back one page in story
function previousPage() {
    current_page--;
    if (current_page == -1) {
        current_page = story_content.length - 1;
    }
    doPage(current_page);
}

// go to first story page == RESET
function firstPage() {
    current_page = 0;
    doPage(current_page);
}


// add navigation controls
addNavigation();

// set the start page
firstPage();
