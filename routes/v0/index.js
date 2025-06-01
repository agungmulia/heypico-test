const express = require("express");

const app = new express.Router();

// directory for v0 version
app.use("/maps", require("../../src/modules/maps/routes.js"));

module.exports = app;
