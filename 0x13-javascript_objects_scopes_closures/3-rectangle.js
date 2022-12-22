#!/usr/bin/node
/*
 * Represents a class Rectangle that defines a rectangle
 * If w or h is equal or less than 0, create an empty class
 * Create an instance method called print() that prints the rectangle
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
};
