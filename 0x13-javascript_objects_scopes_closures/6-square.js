#!/usr/bin/node
// Represents a class Square that inherits from Rectangle
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (!c) this.print();
    else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('c');
	}
        console.log('');
      }
    }
  }
};
