const bookshelf = require('bookshelf');
const Plant = require('./Plant');

module.exports = bookshelf.Model.extend({
  tableName: 'plantImages',
  plant() {
    return this.belongsTo(Plant);
  }
})