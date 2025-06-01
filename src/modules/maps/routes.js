const express = require("express");
const router = express.Router();

const { MapsControllerClass } = require("./controller");
const { GoogleMapsService } = require("./service");

const MapsController = new MapsControllerClass(GoogleMapsService);

router.get("/places", MapsController.getPlaces);

module.exports = router;
