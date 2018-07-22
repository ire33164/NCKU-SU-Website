const { Router } = require('express')

const router = Router()
const loginOperation = require('../../model/query/login.js')
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false});

/* GET user listing. */
router.post('/user', urlencodedParser, (req, res) => {
    let username = req.body.username;
    let pwd = req.body.password;
    let status;

    loginOperation.login(username, pwd)
    .then( val =>{
        // 0 -> success
        // 1 -> wrong password
        // 2 -> wrong account
        res.send(val);
    });

})

/* GET developer by ID. */
router.get('/developers/:id', (req, res) => {
  const id = parseInt(req.params.id)
  if (id >= 0 && id < data.length) {
    res.json(data[id])
  } else {
    res.sendStatus(404)
  }
})

module.exports = router;
