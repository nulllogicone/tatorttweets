var word_list = [
/* {text: "Lorem", weight: 13, link: "https://github.com/DukeLeNoir/jQCloud"}, */
{text: "apothekerin", weight: 213 , html: {"class": "vertical"}}, 
{text: "franz", weight: 199 , html: {"class": "vertical"}}, 
{text: "leitmayr", weight: 192 , html: {"class": "vertical"}}, 
{text: "ende", weight: 181}, 
{text: "batic", weight: 179 , html: {"class": "vertical"}}, 
{text: "gut", weight: 167}, 
{text: "frau", weight: 160 , html: {"class": "vertical"}}, 
{text: "neue", weight: 149}, 
{text: "herr", weight: 131 , html: {"class": "vertical"}}, 
{text: "kommt", weight: 128 , html: {"class": "vertical"}}, 
{text: "kroetz", weight: 105 , html: {"class": "vertical"}}, 
{text: "geht", weight: 104}, 
{text: "tot", weight: 104}, 
{text: "hansen", weight: 103}, 
{text: "kommissar", weight: 102}, 
{text: "katze", weight: 101 , html: {"class": "vertical"}}, 
{text: "bayern", weight: 98 , html: {"class": "vertical"}}, 
{text: "mann", weight: 94 , html: {"class": "vertical"}}, 
{text: "kalli", weight: 84 , html: {"class": "vertical"}}, 
{text: "einfach", weight: 78 , html: {"class": "vertical"}}, 
{text: "endlich", weight: 77}, 
{text: "blut", weight: 76 , html: {"class": "vertical"}}, 
{text: "mike", weight: 75}, 
{text: "schnell", weight: 74}, 
{text: "alte", weight: 72 , html: {"class": "vertical"}}, 
{text: "guter", weight: 72}, 
{text: "irgendwie", weight: 72 , html: {"class": "vertical"}}, 
{text: "fall", weight: 70}, 
{text: "assistent", weight: 69}, 
{text: "gollum", weight: 67}
];
$(function() {
	$("#cloud").jQCloud(word_list);
});