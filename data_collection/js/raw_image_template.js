var webPage = require('webpage');
var page = webPage.create();
  
var fs = require('fs');
var path = 'species.html'

page.open(REPLACEMENT_URL, function (status) {
	var content = page.content;
	fs.write(path,content,'w')
	phantom.exit();
});
