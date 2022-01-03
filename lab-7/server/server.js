'use strict';

const express = require('express');
const path = require('path');
// const htmlPath = path.resolve(__dirname, '..', 'public/index.html');
const staticPath = path.resolve(__dirname, '..', 'src');

const app = express();
const ip = 'http://localhost';
const port = 8080;

app.use('/', express.static(staticPath));

// app.get('/', (req, res) => {
//   console.log(req)
//   // let type = text/plain
//   // res.contentType(path.basename(req.query));
//   // express.static.mime.define({'text/plain': ['md']});
//   // let type = 'text/plain';
//   // console.log(req.);
//   // if (req.path.endsWith('.js')) {
//   //   type = 'application/javascript';
//   // }
//   // if (req.path === '/' || req.path.endsWith('.html')) {
//   //   type = 'text/html';
//   // }
//   // res.setHeader('Content-Type', type);
//   res.setHeader('Access-Control-Allow-Origin', '*')
//   res.sendFile(htmlPath)

// });

app.all('*', (req, res) => {
  // res.setHeader('Content-Type', 'application/javascript');
  const path_ = req.path === '/' ? 'index.html' : req.path
  res.contentType(path.basename(path_));
  console.log(req.path)
  // res.setHeader('Content-Type', 'text/html');
  // res.setHeader('Content-Type', type);
  res.sendFile(path.resolve(__dirname, '..', 'public/' + path_));
});

app.listen(port, () => {
  console.log(`listening at ${ip}:${port}`);
});
