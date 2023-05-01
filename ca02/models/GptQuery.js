'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var gptQuerySchema = Schema({
  query: String,
  date: Date,
  userId: {type:ObjectId, ref:'user' }
});

module.exports = mongoose.model('GptQuery', gptQuerySchema);