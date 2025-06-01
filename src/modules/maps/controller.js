class MapsControllerClass {
  constructor(service) {
    this.service = service;

    this.getPlaces = this.getPlaces.bind(this);
  }

  async getPlaces(req, res) {
    const { query, location } = req.query;

    if (!query || !location)
      return res.status(400).json({ error: "Missing query or location" });

    try {
      const places = await this.service.searchPlaces(query, location);
      res.json(places);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  }
}
exports.MapsControllerClass = MapsControllerClass;
