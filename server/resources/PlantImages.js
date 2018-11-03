const router = require('express').Router();
const knex = require('../knex')();

const PlantImage = require('../models/PlantImage')(knex);

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

router.put(
  '/plant/:id',
  async (req, res, next) => {
    try {
      
    } catch (error) {
      next(error);
    }

    return next();
  },
);

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