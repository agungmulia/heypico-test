const { GoogleMapsService } = require("./googleMapsService");

const Axios = require("axios");

module.exports = {
  GoogleMapsService: new GoogleMapsService(
    process.env.GOOGLE_MAPS_API_KEY,
    Axios
  ),
};
