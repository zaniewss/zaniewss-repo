(function(){
    var data = [
        {
            name: 'open in browser',
            description: 'This allows you to open the current file in your default browser or application.',
            author: 'TechER',
            url: 'https://marketplace.visualstudio.com/items?itemName=techer.open-in-browser',
            downloads: 3292998,
            stars: 3.6,
            price: 0.00,
            selector: 'p1'
        },

        {
            name: 'Rainbow Brackets',
            description: 'A rainbow brackets extension for VS Code',
            author: '2gua',
            url: 'https://marketplace.visualstudio.com/items?itemName=2gua.rainbow-brackets',
            downloads: 811868,
            stars: 4.4,
            price: 0.00,
            selector: 'p2'
        },
        {
            name: 'Path Intellisense',
            description: 'Visual Studio Code plugin that autocompletes filenames',
            author: 'Christian Kohler',
            url: 'https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense',
            downloads: 4402337,
            stars: 4.8,
            price: 0.00,
            selector: 'p3'
        }
    ];

//Package Constructor Function
function Package(data) {
    this.name = data.name;
    this.description = data.description;
    this.author = data.author;
    this.url = data.url;
    this.downloads = data.downloads;
    this.stars = data.stars;
    this.selector = data.selector;

    this.getFormattedDownloads = function () {
        return this.downloads.toLocaleString();
    };

    this.getFormattedStars = function () {
        return this.stars.toLocaleString();
    };
}

//Utility Functions\\

//Returns todays date, formatted\\
var getTodaysDate = function(){
    var today = new Date();
    return today.toDateString();
};

//Returns DOM element by id, wrapping document.getElementById\\
var getEl = function (id) {
    return document.getElementById(id);
}

var writePackageInfo = function(package) {
    //Get Ref to Dom Elements\\
    var selector = package.selector,
        nameEl = getEl(selector + '-name'),
        descEl = getEl(selector + '-description'),
        authEl = getEl(selector + '-author'),
        downloadEl = getEl(selector + '-downloads'),
        starsEl = getEl(selector + '-stars');

    //Write content to elements\\
    nameEl.textContent = package.name;
    descEl.textContent = package.description;
    authEl.textContent = package.author;
    downloadEl.textContent = package.getFormattedDownloads();
    starsEl.textContent = package.getFormattedStars();
}

//Write date\\
dateEl = getEl('date');
dateEl.textContent - getTodaysDate();

//Write package data
var openinbrowser = new Package(data[0]);
writePackageInfo(openinbrowser);

//Write package data
var rainbowbrackets = new Package(data[1]);
writePackageInfo(rainbowbrackets);

//Write package data
var pathintel = new Package(data[2]);
writePackageInfo(pathintel);

}());
