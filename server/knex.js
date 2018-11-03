const config = require('./config');

module.exports = () => {
  return knex = require('knex')({
    client: 'pg',
    connection: {
      host: config.db.host,
      port: config.db.port,
      user: config.db.username,
      password: config.db.password,
      database: config.db.name,
      charset: 'utf8',
    },
  });
}