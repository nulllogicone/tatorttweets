var word_list = [
/* {text: "Lorem", weight: 13, link: "https://github.com/DukeLeNoir/jQCloud"}, */
{text: "janine", weight: 390 , html: {"class": "vertical"}}, 
{text: "gut", weight: 380 , html: {"class": "vertical"}}, 
{text: "vater", weight: 323}, 
{text: "mutter", weight: 320 , html: {"class": "vertical"}}, 
{text: "ende", weight: 310 , html: {"class": "vertical"}}, 
{text: "ballauf", weight: 281 , html: {"class": "vertical"}}, 
{text: "super", weight: 246 , html: {"class": "vertical"}}, 
{text: "guter", weight: 219}, 
{text: "kommt", weight: 190 , html: {"class": "vertical"}}, 
{text: "geht", weight: 175 , html: {"class": "vertical"}}, 
{text: "neue", weight: 171}, 
{text: "tochter", weight: 169}, 
{text: "gemacht", weight: 166}, 
{text: "echt", weight: 151}, 
{text: "kinder", weight: 132}, 
{text: "endlich", weight: 130}, 
{text: "frau", weight: 128}, 
{text: "wirklich", weight: 127 , html: {"class": "vertical"}}, 
{text: "dienstreise", weight: 115 , html: {"class": "vertical"}}, 
{text: "richtig", weight: 114}, 
{text: "eben", weight: 109 , html: {"class": "vertical"}}, 
{text: "kind", weight: 108}, 
{text: "fall", weight: 106}, 
{text: "handy", weight: 102 , html: {"class": "vertical"}}, 
{text: "eltern", weight: 101}, 
{text: "abend", weight: 100}, 
{text: "danke", weight: 97}, 
{text: "klar", weight: 96}, 
{text: "schenk", weight: 96}, 
{text: "seit", weight: 95 , html: {"class": "vertical"}}
];
$(function() {
	$("#cloud").jQCloud(word_list);
});