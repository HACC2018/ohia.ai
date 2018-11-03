const fs = require('fs');

const router = require('express').Router();

// require and export all .js files in same directory as this file
fs.readdirSync(__dirname).forEach((value) => {
  if (value === 'index.js') {
    return;
  }

  if (fs.lstatSync(`${__dirname}/${value}`).isFile() && value.endsWith('.js')) {
    router.use('/', require(`./${value}`));
  }
});

module.exports = router;