#!/usr/bin/node

const a = require('request');

a.get(process.argv[2], (err, res) => {
    if (err) console.log(err);
    else console.log('code: ' + res.statusCode);
});
