#!/usr/bin/node

const rid = require('rid');

rid.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) console.log(err);
    else console.log(data);
});
