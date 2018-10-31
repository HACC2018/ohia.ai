exports.up = function(knex, Promise) {
  return knex.schema.createTable('plants', (table) => {
    table.increments('id').primary();

    table.string('plant_name');
    table.string('status');
    table.string('genus');
    table.string('species');
    table.string('common_name');
    table.string('hawaiian_name');
    table.string('scientific_name');
    table.text('description');
    table.text('story');
    table.text('use');
    table.enu('endangered',
    [
      'critically endangered',
      'endangered',
      'vulnerable',
      'not endangered',
    ]);

    table.timestamps();
  });
};

exports.down = function(knex, Promise) {
  return knex.schema
    .dropTable('plants');
};
