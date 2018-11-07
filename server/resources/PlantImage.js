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

router.get(
  '/images/single/:plantId/',
  async (req, res, next) => {
    try {
      const { plantId } = req.params;

      const plantImage = await new PlantImage({ plant_id: plantId })
        .fetch();

      res.json(plantImage);
    } catch (error) {
      next(error);
    }

    return next();
  },
);

router.get(
  '/images/:plantId/',
  async (req, res, next) => {
    try {
      const { plantId } = req.params;

      const plantImage = await new PlantImage()
        .where('plant_id', plantId)
        .where('identified', true)
        .fetchPage({
          limit: 10,
          columns: ['image_url']
        });

      res.json(plantImage);
    } catch (error) {
      next(error);
    }

    return next();
  },
);

router.post(
  '/plant',
  async (req, res, next) => {
    try {
      
    } catch (error) {
      next(error);
    }

    return next();
  },
);

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

router.delete(
  '/plant/:id',
  async (req, res, next) => {
    try {
      
    } catch (error) {
      next(error);
    }

    return next();
  },
);

module.exports = router;
