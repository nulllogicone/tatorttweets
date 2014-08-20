var word_list = [
/* {text: "Lorem", weight: 13, link: "https://github.com/DukeLeNoir/jQCloud"}, */
{text: "kommt", weight: 41 , html: {"class": "vertical"}}, 
{text: "heutige", weight: 40 , html: {"class": "vertical"}}, 
{text: "sonntag", weight: 40}, 
{text: "handelt", weight: 37}, 
{text: "raffiniert", weight: 36 , html: {"class": "vertical"}}, 
{text: "abend", weight: 26}, 
{text: "uhr", weight: 25}, 
{text: "komischer", weight: 21}, 
{text: "halt", weight: 20 , html: {"class": "vertical"}}, 
{text: "mehmet", weight: 20 , html: {"class": "vertical"}}, 
{text: "ersten", weight: 19}, 
{text: "morgen", weight: 19 , html: {"class": "vertical"}}, 
{text: "glaube", weight: 18}, 
{text: "wegen", weight: 18 , html: {"class": "vertical"}}, 
{text: "migrationshintergrund", weight: 17}, 
{text: "neue", weight: 17 , html: {"class": "vertical"}}, 
{text: "bitte", weight: 16 , html: {"class": "vertical"}}, 
{text: "klischee", weight: 16 , html: {"class": "vertical"}}, 
{text: "gibts", weight: 15}, 
{text: "guten", weight: 15}, 
{text: "kamerun", weight: 15}, 
{text: "leiche", weight: 15 , html: {"class": "vertical"}}, 
{text: "irgendwie", weight: 14}, 
{text: "neuen", weight: 14}, 
{text: "diesmal", weight: 13}, 
{text: "statt", weight: 13 , html: {"class": "vertical"}}, 
{text: "titelthema", weight: 13}, 
{text: "echt", weight: 12}, 
{text: "sag", weight: 12}, 
{text: "sinn", weight: 12}

];
$(function() {
	$("#cloud").jQCloud(word_list);
});