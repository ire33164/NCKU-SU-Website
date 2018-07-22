const Sequelize = require('sequelize')
const sequelize = new Sequelize('mydb', 'root', null, {
    dialect: 'mysql',
    host: 'localhost',
    define: {
      charset: 'utf8'
    }
});


const path = '/home/afcidk/db_learn/python_scripts/';

ff('Account_data.txt', 'AccountData');
ff('Article_data.txt', 'Articles');
ff('Proposal_data.txt', 'Proposals');
ff('Tag_data.txt', 'Tags');


function ff(s, t) {
    sequelize.query("load data local infile '" + path + s + "' into table " + t).then(res => {
        console.log(res);
    })
    .catch(err => {
        console.log(err);
    });
}
