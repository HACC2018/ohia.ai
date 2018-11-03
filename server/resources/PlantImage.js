const router = require('express').Router();
const knex = require('../knex')();

const bookshelf = require('bookshelf')(knex);
bookshelf.plugin('pagination');

const PlantImage = bookshelf.Model.extend({
  tableName: 'plant_images',
  plant() {
    return this.belongsTo(Plant, 'plant_id');
  },
});
const Plant = bookshelf.Model.extend({
  tableName: 'plants',
  plantImages() {
    return this.hasMany(PlantImage);
  },
});

router.route('/plant-image/:id')
  .put(function(req, res) {
    // Get URL parameter
    const { id } = req.params;

    // Get plant image properties
    const {
      plant_id,
      identified,
      user_guess,
    } = req.body;

    // Update plant image
    return PlantImage
      .where('id', id)
      .fetch()
      .then((model) => {
        model
          .save({
            plant_id,
            identified,
            user_guess,
          })
          .then((plantImage) => {
            return res.json({ plantImage: plantImage.serialize() });
          });
      });
  });

module.exports = router;
