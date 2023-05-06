"use strict";
const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var QueryItemSchema = Schema({
	input: String,
	output: String,

	userId: {type: ObjectId, ref: "user"},
});

module.exports = mongoose.model("QueryItem", QueryItemSchema);
