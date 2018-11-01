module.exports = (knex) => {
  const bookshelf = require('bookshelf')(knex);
  const PlantImages = require('./PlantImage');

  return bookshelf.Model.extend({
    tableName: 'plants',
    images() {
      return this.hasMany(PlantImages);
    },
  });
};
