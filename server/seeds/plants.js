
exports.seed = function(knex, Promise) {
  // Deletes ALL existing entries
  return knex('plants').del()
    .then(function () {
      // Inserts seed entries
      return knex('plants').insert([
        {
          id: 1,
          genus: 'metrosideros',
          species: 'M. polymorpha',
          common_name: 'ʻōhiʻa lehua',
          hawaiian_name: 'ʻōhiʻa lehua',
          story: 'very nice story here',
          use: 'various uses of this plant',
          endangered: 'endangered',
        }
      ]);
    });
};
