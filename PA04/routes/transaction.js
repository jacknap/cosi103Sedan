/*
  transaction.js -- Router for the TransactionTable
*/
const express = require('express');
const router = express.Router();
const TransactionItem = require('../models/TransactionItem')
const User = require('../models/User');
const { isLoggedIn } = require('./pwauth');

// isLoggedIn = (req,res,next) => {
//     if (res.locals.loggedIn) {
//       next()
//     } else {
//       res.redirect('/login')
//     }
//    }

// get the value associated to the key
router.get('/transactions/',
  isLoggedIn,
  async (req, res, next) => {
    let results =
    await TransactionItem.aggregate([
                  {$sort:{_id:1}},  
    ])
      
    results = 
    await User.populate(results,
           {path:'_id',
           select:['description','amount','category', 'date']})

    //res.json(results)
    //res.render('summarizeByUser',{results})

    res.render('transactions', {results});
});

router.post('/transactions', 
     
isLoggedIn,
  async (req, res, next) => {
    const trans = new TransactionItem(
        {description: req.body.description,
          amount: req.body.amount,
          category: req.body.category,
          date: req.body.date,
          userId: req.user._id
        })
    await trans.save();
    res.redirect('/transactions')
});

module.exports = router;