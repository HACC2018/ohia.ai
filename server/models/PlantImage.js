module.exports = (knex) => {
  const bookshelf = require('bookshelf')(knex);
  const Plant = require('./Plant');

  return bookshelf.Model.extend({
    tableName: 'plant_images',
    plant() {
      return this.belongsTo(Plant, 'plant_id');
    },
  });
};
