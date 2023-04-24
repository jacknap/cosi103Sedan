

const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var transactionItemSchema = new Schema( {
  description: String,
  amount: Number,
  category: String,
  date: Date,
  //userId: {type:ObjectId, ref:'user' }
} );

const TransactionItem = mongoose.model('Transaction', transactionItemSchema);
/*
  transaction.js -- Router for the TransactionTable
*/
const express = require('express');
const router = express.Router();
//const Transaction = require('../models/TransactionItem')
const User = require('../models/User');
const { isLoggedIn } = require('./pwauth');


router.get('/transactions',
  isLoggedIn,
  async (req, res, next) => {
    
    const sortBy = req.query.sortBy
    let items = []  
      items = await TransactionItem.find({userId: req.userId});
      
      
         
      res.render('transactions', {items})
  
});

router.post('/transactions', 
isLoggedIn,
  async (req, res, next) => {
    const trans = new TransactionItem(
      { description:req.body.description,
        amount: req.body.amount,
        category: req.body.category,
        date: req.body.date,
        userId: req.user._id
      })
 
    
    await trans.save();
    res.redirect('transactions')

});
router.get('/transactions/groupby',
  isLoggedIn,
  async (req, res, next) => {
    let results =
        await TransactionItem.aggregate([  
          {$match: {userId: req.User}},
            {$group:{_id:'$category', total:{$sum: '$amount'}}},
            {$sort:{total:-1}},              
        ]);
	res.locals.results = results;
	res.render("groupby");
});


router.get('/transactions/byCategory',
  isLoggedIn,
  async (req, res, next) => {
    
    let items = await TransactionItem.find({userId: req.User}).sort({category:1});      
      res.render('transactions', {items})
  });

router.get('/transactions/byAmount',
  isLoggedIn,
  async (req, res, next) => {
    
    let items = await TransactionItem.find({userId: req.User}).sort({amount:1});      
      res.render('transactions', {items})
  });

router.get('/transactions/byDescription',
  isLoggedIn,
  async (req, res, next) => {
    
    let items = await TransactionItem.find({userId: req.User}).sort({description:1});      
      res.render('transactions', {items})
  });

router.get('/transactions/byDate',
  isLoggedIn,
  async (req, res, next) => {
    
    let items = await TransactionItem.find({userId: req.User}).sort({date:1});      
      res.render('transactions', {items})
  });

router.get('/transactions/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /todo/remove/:itemId")
      await TransactionItem.deleteOne({_id:req.params.itemId});
      res.redirect('/transactions')
});

router.get('/transactions/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /todo/edit/:itemId")
      const items = 
       await TransactionItem.findById(req.params.itemId);
      res.locals.items = items
      res.render('edit2')
    
});


router.post('/transactions/update',
  isLoggedIn,
  async (req, res, next) => {


      const {itemId,newdesc,newcat,newamount, newdate} = req.body;
      newitem = await TransactionItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {description: newdesc,category : newcat,amount :newamount,date  : newdate}} );

      //await newitem.save();
        
      res.redirect('/transactions')
});

  
module.exports = router;




