
exports.seed = (knex, Promise) => {
  // Deletes ALL existing entries
  return knex('plants').del()
    .then(function () {
      // Inserts seed entries
      return knex('plants').insert([
      ]);
    });
};
