'use strict';

const express = require('express');
const path = require('path');
const staticPath = path.resolve(__dirname, '..', 'src');

const app = express();
const ip = 'http://localhost';
const port = 8080;

app.use('/', express.static(staticPath));

app.all('*', (req, res) => {
  const path_ = req.path === '/' ? 'index.html' : req.path
  res.contentType(path.basename(path_));
  console.log(req.path)
  res.sendFile(path.resolve(__dirname, '..', 'public/' + path_));
});

app.listen(port, () => {
  console.log(`listening at ${ip}:${port}`);
});
