const Sequelize = require('sequelize')
const sequelize = new Sequelize('mydb', 'root', 'ire33164', {
    dialect: 'mysql',
    host: 'localhost',
    define: {
      charset: 'utf8'
    }
});


const path = '/home/chia/Desktop/QQ/NCKU-SU-Website/test_script/';

ff('accounts');
ff('articleTags');
ff('articles');
ff('collections');
ff('discusses');
ff('polls');
ff('proposalAgrees');
ff('proposalClasses');
ff('proposalTags');
ff('proposals');
ff('tags');
ff('replies');


function ff(s) {
    sequelize.query("load data local infile '" + path + s + ".data" + "' into table " + s).then(res => {
        console.log("processing..." + s);
        console.log(res);
    })
    .catch(err => {
        console.log(err);
    });
}
