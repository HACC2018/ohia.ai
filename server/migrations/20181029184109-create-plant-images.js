const knex = require('knex');

exports.up = () => {
  knex.schema.createTable('plant_images', (table) => {
    table.increments('id').primary();
    table.foreign('plant_id').unique().references('plants.id');
  
    table.decimal('latitude', 15);
    table.decimal('longitude', 15);
    table.text('image_url');
    table.json('bounding_box');
  
    table.timestamps();
  });
};

exports.down = (knex) => {
  return knex.schema
    .dropTable('plant_images')
}