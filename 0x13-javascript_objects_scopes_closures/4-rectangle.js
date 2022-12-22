#!/usr/bin/node
/*
 * Represents a class Rectangle that defines a rectangle
 * If w or h is equal or less than 0, create an empty class
 * Create an instance method called print() that prints the rectangle
 * Create an instance method called rotate() that exchanges
 * the width and height of the rectangle
 * Create an instance method called double() that multiplies
 * the width and height of the rectangle by 2
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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
