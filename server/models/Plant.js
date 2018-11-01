const bookshelf = require('bookshelf');
const PlantImages = require('./PlantImage');

module.exports = bookshelf.Model.extend({
  tableName: 'plants',
  images() {
    return this.hasMany(PlantImages);
  }
})