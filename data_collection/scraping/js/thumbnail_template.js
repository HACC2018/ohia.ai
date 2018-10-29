var webPage = require('webpage');
var page = webPage.create();
  
var fs = require('fs');
var path = 'js/page.html';

page.open(REPLACEMENT_URL, function (status) {
	var content = page.content;
	fs.write(path,content,'w');
	phantom.exit();
});
