#!/usr/bin/node
const request = require('request');

const webUrl = process.argv[2];

request(webUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId] === undefined) {
          completedTasksByUser[todo.userId] = 0;
        }
        completedTasksByUser[todo.userId] += 1;
      }
    });
    console.log(completedTasksByUser);
  }
});
