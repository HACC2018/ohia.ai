const bookshelf = require('bookshelf');
const Plant = require('./Plant');

module.exports = bookshelf.Model.extend({
  tableName: 'plant_images',
  plant() {
    return this.belongsTo(Plant);
  }
})