module.exports = (knex) => {
  const bookshelf = require('bookshelf')(knex);
  bookshelf.plugin('pagination');
  const Plant = require('./Plant');

  return bookshelf.Model.extend({
    tableName: 'plant_images',
    plant() {
      return this.belongsTo(Plant, 'plant_id');
    },
  });
};
