var word_list = [
{text: "@tatort", weight: 11}, 
{text: ";-)", weight: 10}, 
{text: "#stuttgart", weight: 9}, 
{text: "geht", weight: 9 , html: {"class": "vertical"}}, 
{text: "los", weight: 9 , html: {"class": "vertical"}}, 
{text: "sehen", weight: 9 , html: {"class": "vertical"}}, 
{text: "stuttgart", weight: 9}, 
{text: "#stromberg", weight: 7}, 
{text: "danke", weight: 6}, 
{text: "endlich", weight: 6 , html: {"class": "vertical"}}, 
{text: "schauen", weight: 6}, 
{text: "sonntag", weight: 6 , html: {"class": "vertical"}}, 
{text: "time", weight: 6 , html: {"class": "vertical"}}, 
{text: "stuttgarter", weight: 5 , html: {"class": "vertical"}}, 
{text: "zeit", weight: 5 , html: {"class": "vertical"}}, 
{text: "#knastort", weight: 4 , html: {"class": "vertical"}}, 
{text: "abspann", weight: 4 , html: {"class": "vertical"}}, 
{text: "beginnt", weight: 4 , html: {"class": "vertical"}}, 
{text: "bereit", weight: 4}, 
{text: "geht's", weight: 4 , html: {"class": "vertical"}}, 
{text: "glaub", weight: 4}, 
{text: "gucken", weight: 4}, 
{text: "müller", weight: 4 , html: {"class": "vertical"}}, 
{text: "ruhe", weight: 4}, 
{text: "twitter", weight: 4 , html: {"class": "vertical"}}, 
{text: "#wartenaufdentatort", weight: 3}, 
{text: "@daserste", weight: 3 , html: {"class": "vertical"}}, 
{text: "akku", weight: 3 , html: {"class": "vertical"}}, 
{text: "erstmal", weight: 3}, 
{text: "gespannt", weight: 3}, 
{text: "gibt's", weight: 3}, 
{text: "guckt", weight: 3 , html: {"class": "vertical"}}, 
{text: "gut", weight: 3 , html: {"class": "vertical"}}, 
{text: "kommt", weight: 3}, 
{text: "kurz", weight: 3}, 
{text: "minuten", weight: 3}, 
{text: "musik", weight: 3 , html: {"class": "vertical"}}, 
{text: "mörder", weight: 3}, 
{text: "schlecht", weight: 3}, 
{text: "schlossgarten", weight: 3 , html: {"class": "vertical"}}, 
{text: "seilbahn", weight: 3 , html: {"class": "vertical"}}, 
{text: "sofa", weight: 3}, 
{text: "spannend", weight: 3 , html: {"class": "vertical"}}, 
{text: "steht", weight: 3 , html: {"class": "vertical"}}, 
{text: "udo", weight: 3 , html: {"class": "vertical"}}, 
{text: "waldfriedhof", weight: 3}, 
{text: "woche", weight: 3 , html: {"class": "vertical"}}, 
{text: "zwei", weight: 3}, 
{text: "#ard", weight: 2}, 
{text: "#f1", weight: 2 , html: {"class": "vertical"}}, 
{text: "#formel1", weight: 2 , html: {"class": "vertical"}}, 
{text: "#jauch", weight: 2}, 
{text: "#jugendinden70ern", weight: 2}, 
{text: "#sonntag", weight: 2 , html: {"class": "vertical"}}, 
{text: "#udolindenberg", weight: 2 , html: {"class": "vertical"}}, 
{text: "#wglife", weight: 2 , html: {"class": "vertical"}}, 
{text: "57%", weight: 2}, 
{text: "@ardtext777", weight: 2 , html: {"class": "vertical"}}, 
{text: "@blinder_hasi", weight: 2 , html: {"class": "vertical"}}, 
{text: "\o/", weight: 2 , html: {"class": "vertical"}}, 
{text: "alternative", weight: 2}, 
{text: "beck", weight: 2 , html: {"class": "vertical"}}, 
{text: "bevor", weight: 2}, 
{text: "beweise", weight: 2}, 
{text: "bitte", weight: 2}, 
{text: "bootz", weight: 2}, 
{text: "bringt", weight: 2}, 
{text: "crime", weight: 2 , html: {"class": "vertical"}}, 
{text: "dabei", weight: 2}, 
{text: "dadaaa", weight: 2 , html: {"class": "vertical"}}, 
{text: "dürfen", weight: 2 , html: {"class": "vertical"}}, 
{text: "erster", weight: 2 , html: {"class": "vertical"}}, 
{text: "früher", weight: 2 , html: {"class": "vertical"}}, 
{text: "gehe", weight: 2 , html: {"class": "vertical"}}, 
{text: "gehen", weight: 2}, 
{text: "gemütlich", weight: 2 , html: {"class": "vertical"}}, 
{text: "gesehen", weight: 2 , html: {"class": "vertical"}}, 
{text: "gutes", weight: 2}, 
{text: "herrn", weight: 2}, 
{text: "heut", weight: 2 , html: {"class": "vertical"}}, 
{text: "holen", weight: 2 , html: {"class": "vertical"}}, 
{text: "kommissar", weight: 2}, 
{text: "langsam", weight: 2}, 
{text: "leiche", weight: 2}, 
{text: "let's", weight: 2}, 

];
$(function() {
$("#cloud").jQCloud(word_list);
});