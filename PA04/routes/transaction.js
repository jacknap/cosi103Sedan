

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

// isLoggedIn = (req,res,next) => {
//   if (res.locals.loggedIn) {
//     next()
//   } else {
//     res.redirect('/login')
//   }
// }

// get the value associated to the key
router.get('/transactions',
  isLoggedIn,
  async (req, res, next) => {
    
    const sortBy = req.query.sortBy
    let items = [] 

    
      items = await TransactionItem.find({userId: req.userId});
      
      // items = await TransactionItem.populate(items,
      //         {path:'hee',
      //         select:['description','category', 'amount', 'date']})
      
      //res.json(items)      
      res.render('transactions', {items})
    


    //let items = []
    //const trans = await TransactionItem.find({});
    
    
    //items = await TransactionItem.find({})
    //res.json(trans)


  //res.render('transactions', {items})
  
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
    // const items = await ToDoItem.find({ userId: req.user._id })
    //   .sort({ completed: 1, priority: 1, createdAt: 1 });
    
    await trans.save();
    res.redirect('transactions')

});
router.get('/transactions/groupby',
  isLoggedIn,
  async (req, res, next) => {

    let items = await TransactionItem.find({userId: req.userId});   
    items = await TransactionItem.aggregate([
      {
        $group: {
          _id: "$category",
          total: { $sum: "$amount" }
        }
      },
      {
        $sort: { total: -1 }
      }
    ]); 
    //res.json(items)
    res.render('groupby', {items});
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
      const item = 
       await TransactionItem.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('edit2')
      //res.json(item)
});

router.post('/transactions/update',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,newdesc,newcat,newamount, newdate} = req.body;
      await TransactionItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {description: newdesc,category : newcat,amount :newamount,date  : newdate}} );
      res.redirect('/transactions')
});

  
module.exports = router;

// router.get('/transactions/table',
// isLoggedIn,
// async (req, res, next) => {
//     let results =
//           await TransactionItem.aggregate(
//               [ 

//                 {$group:{_id:'$description',
//                   total:{$count:{}}
//                   }},
//                 {$sort:{total:-1}},              
//               ])
            
//       results = 
//          await User.populate(results,
//                  {path:'_id',
//                  select:['description','category', 'amount', 'date']})

//       res.json(results)
//       res.render('table',{results})
// });


