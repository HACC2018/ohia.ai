
exports.seed = (knex, Promise) => {
  // Deletes ALL existing entries
  return knex('plant_images').del()
    .then(function () {
      // Inserts seed entries
      return knex('plant_images').insert([
      ]);
    });
};
