const Sequelize = require('sequelize')
const sequelize = new Sequelize('mydb', 'root', 'ire33164', {
    dialect: 'mysql',
    host: 'localhost',
    define: {
      charset: 'utf8'
    }
});


const path = '/home/chia/Desktop/QQ/NCKU-SU-Website/test_script/';

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
