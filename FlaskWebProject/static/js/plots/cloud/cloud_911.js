var word_list = [
{text: "gut", weight: 293 , html: {"class": "vertical"}}, 
{text: "@tatort", weight: 257 , html: {"class": "vertical"}}, 
{text: "ende", weight: 254 , html: {"class": "vertical"}}, 
{text: "ballauf", weight: 236 , html: {"class": "vertical"}}, 
{text: "köln", weight: 231 , html: {"class": "vertical"}}, 
{text: "mutter", weight: 225 , html: {"class": "vertical"}}, 
{text: "janine", weight: 206}, 
{text: "vater", weight: 185}, 
{text: "guter", weight: 174 , html: {"class": "vertical"}}, 
{text: "#jauch", weight: 156}, 
{text: "neue", weight: 148 , html: {"class": "vertical"}}, 
{text: "kölner", weight: 137}, 
{text: "geht", weight: 134}, 
{text: "tochter", weight: 130}, 
{text: "böse", weight: 124 , html: {"class": "vertical"}}, 
{text: "super", weight: 122}, 
{text: "echt", weight: 120}, 
{text: "kommt", weight: 111 , html: {"class": "vertical"}}, 
{text: "hätte", weight: 107 , html: {"class": "vertical"}}, 
{text: "frau", weight: 105 , html: {"class": "vertical"}}, 
{text: "richtig", weight: 105 , html: {"class": "vertical"}}, 
{text: "endlich", weight: 96}, 
{text: "kinder", weight: 96}, 
{text: "wirklich", weight: 96 , html: {"class": "vertical"}}, 
{text: "wäre", weight: 93}, 
{text: "#köln", weight: 91}, 
{text: "eben", weight: 86 , html: {"class": "vertical"}}, 
{text: "häslich", weight: 84}, 
{text: "eltern", weight: 80 , html: {"class": "vertical"}}, 
{text: "einfach", weight: 79}, 
{text: "schenk", weight: 78}, 
{text: "schön", weight: 78}, 
{text: "assistentin", weight: 75}, 
{text: "#ard777", weight: 74}, 
{text: "danke", weight: 72 , html: {"class": "vertical"}}, 
{text: "bitte", weight: 71 , html: {"class": "vertical"}}, 
{text: "gute", weight: 71 , html: {"class": "vertical"}}, 
{text: "kind", weight: 71}, 
{text: "seit", weight: 70}, 
{text: "u-bahn", weight: 69 , html: {"class": "vertical"}}, 
{text: "speech", weight: 66}, 
{text: "arsch", weight: 65 , html: {"class": "vertical"}}, 
{text: "klar", weight: 63 , html: {"class": "vertical"}}, 
{text: "#ballauf", weight: 62 , html: {"class": "vertical"}}, 
{text: "abend", weight: 62 , html: {"class": "vertical"}}, 
{text: "thema", weight: 62}, 
{text: "nie", weight: 61}, 
{text: "@daserste", weight: 60 , html: {"class": "vertical"}}, 
{text: "minuten", weight: 60 , html: {"class": "vertical"}}, 
{text: "besser", weight: 59}, 
{text: "irgendwie", weight: 58}, 
{text: "sieht", weight: 58}, 
{text: "geige", weight: 56}, 
{text: "leider", weight: 56}, 
{text: "sagen", weight: 56}, 
{text: "fall", weight: 55 , html: {"class": "vertical"}}, 
{text: "handy", weight: 55 , html: {"class": "vertical"}}, 
{text: "currywurst", weight: 54 , html: {"class": "vertical"}}, 
{text: "mag", weight: 54 , html: {"class": "vertical"}}, 
{text: "muttertag", weight: 53 , html: {"class": "vertical"}}, 
{text: "kleine", weight: 52}, 
{text: "mädchen", weight: 52}, 
{text: "sehen", weight: 52 , html: {"class": "vertical"}}, 
{text: "spannend", weight: 51}, 
{text: "max", weight: 50 , html: {"class": "vertical"}}, 
{text: "twitter", weight: 50}, 
{text: "zeit", weight: 50 , html: {"class": "vertical"}}, 
{text: "bestimmt", weight: 49 , html: {"class": "vertical"}}, 
{text: "junge", weight: 49}, 
{text: "nen", weight: 49}, 
{text: "wow", weight: 49}, 
{text: ";-)", weight: 48}, 
{text: "anfang", weight: 48}, 
{text: "haftrichterin", weight: 48 , html: {"class": "vertical"}}, 
{text: "darf", weight: 47}, 
{text: "heutigen", weight: 47}, 
{text: "klasse", weight: 47 , html: {"class": "vertical"}}, 
{text: "opfer", weight: 47}, 
{text: "#ard", weight: 46}, 
{text: "krass", weight: 46 , html: {"class": "vertical"}}, 
{text: "lieber", weight: 46 , html: {"class": "vertical"}}, 
{text: "übrigens", weight: 46 , html: {"class": "vertical"}}, 
{text: "freddy", weight: 45 , html: {"class": "vertical"}}, 
{text: "lassen", weight: 45 , html: {"class": "vertical"}}, 
{text: "lol", weight: 45 , html: {"class": "vertical"}}, 

];
$(function() {
$("#cloud").jQCloud(word_list);
});