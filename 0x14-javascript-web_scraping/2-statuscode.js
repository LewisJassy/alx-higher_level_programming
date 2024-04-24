#!/usr/bin/node

const process = require("process");
const request = require('request');
const server = process.argv[2];

request(server, function (error, response, body) {
	if (error != null) {
		console.error("error:", error);
	}
	else {
		console.log("code:", response.StatusCode);
	}
});

