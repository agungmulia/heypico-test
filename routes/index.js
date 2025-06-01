const express = require("express");

const app = new express.Router();

// use for versioning
app.use("/v0", require("./v0"));

module.exports = app;
