module.exports = (knex) => {
  const bookshelf = require('bookshelf')(knex);
  bookshelf.plugin('pagination');
  const PlantImages = require('./PlantImage');

  return bookshelf.Model.extend({
    tableName: 'plants',
    images() {
      return this.hasMany(PlantImages);
    },
  });
};
