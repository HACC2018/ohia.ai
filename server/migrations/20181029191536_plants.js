exports.up = function(knex, Promise) {
  return knex.schema.createTable('plants', (table) => {
    table.increments('id').primary();

    table.string('plant_name').notNullable().unique();
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
    table.text('uses');
    table.enu('endangered',
    [
      'Endangered',
      'Threatened',
      'Candidate for listing',
      'Species of concern',
      'Not listed by state',
    ]);

    table.timestamp('created_at').defaultTo(knex.fn.now());
    table.timestamp('updated_at').defaultTo(knex.fn.now());
  });
};

exports.down = function(knex, Promise) {
  return knex.schema
    .dropTable('plants');
};
