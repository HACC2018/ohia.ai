const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello ohia.ai');
});

app.listen(port, () => {
  console.log(`Server for ohia.ai listening on port ${port}`);
});
