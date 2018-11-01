exports.up = function(knex, Promise) {
  return knex.schema.createTable('plants', (table) => {
    table.increments('id').primary();

    table.string('plant_name').notNullable();
    table.enu('status',
    [
      'Native',
      'Invasive',
      'Non-native',
    ]).notNullable();
    table.string('hawaiian_name');
    table.string('common_name');
    table.string('scientific_name').notNullable();
    table.string('genus').notNullable();
    table.string('species').notNullable();
    table.text('description');
    table.text('story');
    table.text('use');
    table.enu('endangered',
    [
      'Critically endangered',
      'Endangered',
      'Vulnerable',
      'Not endangered',
    ]);

    table.timestamps();
  });
};

exports.down = function(knex, Promise) {
  return knex.schema
    .dropTable('plants');
};
