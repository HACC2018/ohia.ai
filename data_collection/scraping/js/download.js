var webPage = require('webpage');
var page = webPage.create();
  
var fs = require('fs');
var path = 'js/page.html'

page.open('http://www.starrenvironmental.com/images/search/?q=Abelia+x+grandiflora', function (status) {
	var content = page.content;
	fs.write(path,content,'w')
	phantom.exit();
});
