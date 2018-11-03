const router = require('express').Router();
const knex = require('../knex')();

const PlantImage = require('../models/PlantImage')(knex);

router.get(
  '/image/single/:plantId/',
  async (req, res, next) => {
    try {
      const { plantId } = req.params;

      const plant = await new PlantImage({ plant_id: plantId })
        .fetch();

      res.json(plant);
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