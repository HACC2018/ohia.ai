const router = require('express').Router();
const knex = require('../knex')();

const Plant = require('../models/Plant')(knex);

router.get(
  '/plants/:limit/:offset',
  async (req, res, next) => {
    try {
      const { limit, offset } = req.params;

      const plant = await new Plant()
        .fetchPage({
          limit,
          offset,
        });

      res.json(plant);
    } catch (error) {
      next(error);
    }

    return next();
  },
);

router.get(
  '/plant/:id',
  async (req, res, next) => {
    try {
      // Get URL paramter
      const { id } = req.params;

      // Fetch plant by ID from database
      const plant = await new Plant({ id })
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