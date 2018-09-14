const db = require('../sqldb')
const account = db.models.account;

/*
 * login function
 * return value:(string)
 *  0  -> login success, without admin
 *  1  -> login success, with admin
 *  -1 -> login failed
 */
function login(username, passwd) {
    
  return account.findOne({
    where: {
        studentId: username
    },
    attributes: ['password', 'permission']
  })
  .then( res => {
    hashed = res.dataValues.password;
    return {
        perm: res.dataValues.permission,
        hashed: hashed
    };
  })
  .then( res => {
    return account.verifyPwd(passwd, res.hashed)
    .then( val => {
      if (val) {
        console.log("in /model/query/login.js: permission: " + res.perm);
        return res.perm;
      }
      else {
        return "-1"
      }
    })
  });
}

/*
 * set account status to verified email
 */
function verify(studentId) {
  db.sequelize.transaction( t=> {
    account.update(
      { verified: true },
      { where: {studentId: studentId} }
    )
    .then( () => {
        console.log("verified in model/query/account.js");
    });
  })
}

/*
 * create a totally new account
 */
function createAccount(data) {
  let passwd = '';

  account.hashFunc(data.password)
  .then( p => {
      passwd = p;
  })
  .then( () => {
    db.sequelize.transaction( t=> {
      console.log(data.username);
      account.create({
        studentId: data.username,
        email: data.email,
        password: passwd,
        name: data.name,
      })
    });
  });
}

/*
 * get email by studentId, used in "forgot password"
 */
function getEmail(id) {
  return new Promise( (resolve, reject) => {
    account.findById(id)
    .then( res => {
      resolve(res.getDataValue('email'));
    });
  });
}

/*
 * change password by studentId, used in "forgot password"
 */
function changepwd(id, newpwd) {

  let passwd = '';

  // get hashed value
  account.hashFunc(newpwd)
  .then( p => {
    passwd = p;
  })
  .then( () => {
    db.sequelize.transaction( t => {
      // update password
      account.update(
        { password: passwd },
        { where: {studentId: id} }
      )
      .then( res=> {
        console.log(res);
      })
      .catch( err=> {
        console.log(err);
      });
    });
  })
  .catch( err=> {
    console.log(err);
  });
  
}

module.exports = {
  /* account */
  login: login,
  create: createAccount,
  verify: verify,

  /* password */
  getEmail: getEmail,
  changepwd: changepwd
};