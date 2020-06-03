$(document).ready(function() {
    $('.sidenav').sidenav();

    $('.parallax').parallax();

    $('.materialboxed').materialbox();
});

$("#typer").typer({
    strings: [
        "today something happened",
        "and I'm so excited to share it!!!"
    ]
});

$("#typo").typer({
    strings: [
        "I'm your average Nigerian Student😫😑",
        "With a lot of trust issues🤣🤣",
        "But I love that you're reading my diary😆😬🤩",
        "I'm also have a lot of cray-cray🤪🤪😵",
        'and also dont touch my diary😂'
    ]
});
//Displaying Year in Photo
let date = new Date();
let year = date.getFullYear()
$("#date").html(year);

/*
//Dark Mode Test
function Dark(){
    var test = document.body;
    test.classList.toggle("dark-mode");
}
*/
