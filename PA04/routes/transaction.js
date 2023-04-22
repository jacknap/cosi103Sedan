/*
  transaction.js -- Router for the TransactionTable
*/
const express = require('express');
const router = express.Router();
const TransactionItem = require('../models/TransactionItem')
const User = require('../models/User');
const { isLoggedIn } = require('./pwauth');

// Display all transactions for the user
// TODO: sortBy feature
router.get('/transaction/',
  isLoggedIn,
  async (req, res, next) => {
	let transactions = await TransactionItem.find({userId:req.user._id})
	res.locals.transactions = transactions;
    res.render('transactions');
});

// Create a new transaction
router.post('/transaction/create', 
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
	res.redirect('/transaction')
});

// Delete a transaction
router.get('/transaction/delete/:transactionId',
  isLoggedIn,
  async (req, res, next) => {
	// TODO: add delete function (refer to todo example)
});

// Display the edit page for a transaction
router.get('/transaction/edit/:transactionId',
  isLoggedIn,
  async (req, res, next) => {
    const transaction = await TransactionItem.findById(req.params.transactionId);
    res.locals.transaction = transaction;
    res.render('editTransaction');
});

// Edit a transaction
router.post('/transaction/updateTransaction',
  isLoggedIn,
  async (req, res, next) => {
    const {transactionId, description, amount, category, date} = req.body;
    await TransactionItem.findOneAndUpdate(
    	{_id:transactionId},
        {$set: {description, amount, category, date}}
	);
    res.redirect('/transaction');
});

// Group by category
router.get('/transaction/byCategory',
  isLoggedIn,
  async (req, res, next) => {
    let results =
        await TransactionItem.aggregate([  
            {$group:{
				_id:'$category', 
				total:{$sum: '$amount'}}},
            {$sort:{total:-1}},              
        ]);
	res.locals.results = results;
	res.render("summarizeByCategory");
});

module.exports = router;