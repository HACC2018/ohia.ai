exports.up = function(knex, Promise) {
  return knex.schema.createTable('plant_images', (table) => {
    table.increments('id').primary();
    table.integer('plant_id').unsigned();
    table.foreign('plant_id').references('plants.id');
    
    table.boolean('identified').notNullable().defaultTo(false);
    table.decimal('latitude', 15);
    table.decimal('longitude', 15);
    table.text('image_url').notNullable();
    table.json('bounding_box');
  
    table.timestamps();
  });
};

exports.down = function(knex, Promise) {
  return knex.schema
    .dropTable('plant_images');
};
