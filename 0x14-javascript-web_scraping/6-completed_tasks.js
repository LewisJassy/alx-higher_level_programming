#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const todos = JSON.parse(body);
  const usersCompleted = {};
  for (const todo of todos) {
    if (todo.completed === true) {
      if (todo.userId in usersCompleted) {
        usersCompleted[todo.userId] += 1;
      } else {
        usersCompleted[todo.userId] = 1;
      }
    }
  }
  console.log(usersCompleted);
});
